import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.db_setup import Base, Project, User, ProjectUser, File, DB_STRING

# Utility Methods


def add_file(name, type, project_name):
    project_id = session.query(Project).filter(Project.name == project_name).one().id
    session.add(File(name=name, type=type, project_id=project_id))


def add_project_user(project_name, user_name):
    project_id = session.query(Project).filter(Project.name == project_name).one().id
    user_id = session.query(User).filter(User.name.startswith(user_name)).one().id
    session.add(ProjectUser(project_id=project_id, user_id=user_id))

# Main Script


db_engine = create_engine(DB_STRING)

# delete and recreate all tables from scratch
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# create db session
Session = sessionmaker(db_engine)
session = Session()

# add data

session.add(Project(name="Paint Everything", start_date=datetime.datetime(2018, 6, 14)))
session.add(Project(name="Sarah's Book Reviews", start_date=datetime.datetime(2019, 8, 10)))
session.add(Project(name="Candy Warehouse", start_date=datetime.datetime(2019, 5, 21)))
session.add(Project(name="Mighty Mighty Meatballs", start_date=datetime.datetime(2019, 11, 30)))
session.add(Project(name="2020 Voter Correction", start_date=datetime.datetime(2020, 2, 13)))
session.commit()

session.add(User(name="Brian Newman", email="brian_n@comcast.net"))
session.add(User(name="Macy Shillings", email="macy@gmail.com"))
session.add(User(name="Patrick Tesler", email="patrickt@comcast.net"))
session.add(User(name="Emily Bradley", email="emma_s_bradley@xyphol.com"))
session.add(User(name="Quin Border", email="a_q_border@gmail.com"))
session.commit()

add_file("colors", "Java", "Paint Everything")
add_file("brush", "Java", "Paint Everything")
add_file("Hamlet", "Text", "Sarah's Book Reviews")
add_file("management", "C", "Sarah's Book Reviews")
add_file("Gumdrops", "PNG", "Candy Warehouse")
add_file("Jelly Beans", "PNG", "Candy Warehouse")
add_file("Chocolate", "PNG", "Candy Warehouse")
add_file("Peppermints", "PNG", "Candy Warehouse")
add_file("yumness_handler", "C#", "Candy Warehouse")
add_file("might", "SH Script", "Mighty Mighty Meatballs")
add_file("ball_o_meat", "Windows Media Video", "Mighty Mighty Meatballs")
add_file("election_hacker", "Python", "2020 Voter Correction")
session.commit()

add_project_user("Paint Everything", "Macy")
add_project_user("Sarah's Book Reviews", "Emily")
add_project_user("Candy Warehouse", "Brian")
add_project_user("Mighty Mighty Meatballs", "Patrick")
add_project_user("2020 Voter Correction", "Quin")
add_project_user("Paint Everything", "Emily")
add_project_user("Candy Warehouse", "Patrick")
session.commit()

# Print data for easy verification

result = session.query(Project)
for project in result:
    print(project.id, project.name, project.start_date)

print("")

result = session.query(User)
for user in result:
    print(user.id, user.name, user.email)

print("")

result = session.query(File)
for file in result:
    print(file.id, file.name, file.type, file.project_id)

print("")

result = session.query(ProjectUser)
for pu in result:
    print(pu.project_id, pu.user_id)

# Close session

session.close()
