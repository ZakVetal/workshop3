from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):

    __tablename__ = 'orm_user'

    user_email = Column(String(40), primary_key=True)
    user_name = Column(String(6), nullable=False)
    user_phone = Column(Integer, nullable=False)

    orm_todo = relationship('ormTodo', secondary='orm_user_todo')

class ormTodo(Base):

    __tablename__ = 'orm_todo'

    todo_name = Column(String(40), primary_key=True)
    todo_deadline = Column(Date, nullable=False)
    user_important = Column(Integer, nullable=False)

    orm_users = relationship('ormUser', secondary='orm_user_todo')

class ormUserTodo(Base):

    __tablename__ = 'orm_user_todo'

    user_email = Column(String(40), primary_key=True)
    todo_name = Column(String(40), primary_key=True)