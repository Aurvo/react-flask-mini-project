from contextlib import contextmanager
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from backend.database.db_setup import Project, ProjectUser, User, File, DB_STRING

db_engine = create_engine(DB_STRING)
Session = sessionmaker(db_engine)

nameToClassDict = {
    'Project': Project,
    'ProjectUser': ProjectUser,
    'User': User,
    'File': File
}

ROWS_PER_PAGE = 5


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def get_data(args):
    # Accepted URL Parameters:
    # area: the class model of the table to query (as a string, or course)
    # order_by: the field to order by (asc by default)
    # desc: if both order_by and desc are present, orders date in descending order
    # fields[]: fields to filter--length must equal the length of values[]
    # values[]: values to filter (each must correspond with a field--i.e same position)
    # page: the page number (site is paginated)
    # rows_per_page: data items per page
    # project_id: the corresponding project id for each data item (if applicable)

    # determine table to query from args
    table_class = nameToClassDict[args.get('area')];
    if not table_class:
        return []

    with get_session() as session:
        # begin forming query
        query = session.query(table_class)

        # handle project_id constraint
        project_id = args.get('project_id')
        if project_id and project_id.isdigit():
            project_id = int(project_id)
            if table_class == File:
                query = query.filter(table_class.project_id == project_id)
            elif table_class == User:
                # sql alchemy uses the defined relationships in db_setup to know what to join on
                query = query.join(ProjectUser).filter(ProjectUser.project_id == project_id)
            # does nothing if queried table is not File or User

        # update query with filters if applicable
        query = handle_filter(query, table_class, args.getlist('fields[]'), args.getlist('values[]'))

        # sort rows if applicable
        sorted_col = args.get('order_by')
        if sorted_col:
            direction_method = desc if args.get('desc') else asc
            query = query.order_by(direction_method(sorted_col))

        # convert query to list
        rows = [row.serialize for row in query]
        # manually add in project_id for user rows because that table doesn't have that field
        if table_class == User and project_id:
            for row in rows:
                row['project_id'] = project_id;

        # pagination - get the appropriate portion of the list
        rows, page_info_dict = handle_pagination(rows, args.get('page'))

        # return
        return rows, page_info_dict


def handle_filter(query, table_class, filter_fields, filter_values):
    if len(filter_fields) != len(filter_values):
        # invalid query, return 0 rows
        return query.filter(False)

    new_query = query
    for i in range(len(filter_fields)):
        field = filter_fields[i]
        value = filter_values[i]
        new_query = add_filter(new_query, table_class, field, value)

    return new_query


def add_filter(query, table_class, field, value):
    sql_alchemy_field = getattr(table_class, field)
    sql_field_type = str(sql_alchemy_field.property.columns[0].type)
    if 'INT' in sql_field_type:
        new_query = query.filter(getattr(table_class, field) == int(value))
    else:
        new_query = query.filter(getattr(table_class, field).like(f"%{value}%"))

    return new_query


def handle_pagination(rows, page_num):
    original_length = len(rows)
    # convert args to ints, handle Nones, handle defaults
    try:
        page_num = 1 if not page_num else int(page_num)
    except ValueError:
        # invalid parameters - don't do pagination
        return rows

    start_index = (page_num - 1) * ROWS_PER_PAGE
    end_index = min(start_index + ROWS_PER_PAGE, len(rows))
    return rows[start_index:end_index], {
        'page': page_num if page_num <= original_length // ROWS_PER_PAGE + 1 else 1,
        'sizePerPage': ROWS_PER_PAGE,
        'totalSize': original_length
    }
