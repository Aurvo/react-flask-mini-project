from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    start_date = Column(DateTime, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': str(self.start_date)
        }


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


class ProjectUser(Base):
    __tablename__ = 'project_user'

    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True, autoincrement=False)
    user_id = Column(Integer, ForeignKey('project.id'), primary_key=True, autoincrement=False)

    @property
    def serialize(self):
        return {
            'project_id': self.project_id,
            'user_id': self.user_id,
        }


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(30), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'project_id': self.project_id
        }


DB_STRING = 'postgresql://postgres:abc@localhost:5432'

