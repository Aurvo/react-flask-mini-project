from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.db_setup import Project, ProjectUser, User, File, DB_STRING

db_engine = create_engine(DB_STRING)
Session = sessionmaker(db_engine)


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def get_projects():
    with get_session() as session:
        return session.query(Project)
