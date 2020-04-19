import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    start_date = Column(DateTime, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class ProjectUser(Base):
    __tablename__ = 'project_user'

    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True, autoincrement=False)
    user_id = Column(Integer, ForeignKey('project.id'), primary_key=True, autoincrement=False)


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(30), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'))
