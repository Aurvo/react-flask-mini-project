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


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def get_data(args):
    # determine table to query from args
    table_class = nameToClassDict[args.get('area')];
    if not table_class:
        raise NameError("table does not exist")

    with get_session() as session:
        # begin forming query
        query = session.query(table_class)

        # update query with filters if applicable
        query = handle_filter(query, table_class, args.getlist('fields[]'), args.getlist('values[]'))

        # sort rows if applicable
        sorted_col = args.get('order_by')
        if sorted_col:
            direction_method = desc if args.get('desc') else asc
            query = query.order_by(direction_method(sorted_col))

        # convert query to list
        rows = [row.serialize for row in query]

        # pagination - get the appropriate portion of the list
        rows = handle_pagination(rows, args.get('page'), args.get('rows_per_page'))

        # return
        return rows


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


def handle_pagination(rows, page_num, rows_per_page):
    # convert args to ints, handle Nones, handle defaults
    try:
        page_num = 1 if not page_num else int(page_num)
        rows_per_page = 5 if not rows_per_page else int(rows_per_page)
    except ValueError:
        # invalid parameters - don't do pagination
        return rows

    start_index = (page_num - 1) * rows_per_page
    end_index = min(start_index + rows_per_page, len(rows))
    return rows[start_index:end_index]
