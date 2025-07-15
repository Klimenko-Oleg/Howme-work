from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from db_utils import engine

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    group = Column(String)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', " \
               f"group='{self.group}')>"


Base.metadata.create_all(bind=engine)
