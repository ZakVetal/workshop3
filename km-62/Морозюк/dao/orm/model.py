from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_department = Column(String(40))
    user_email = Column(String(40))
    user_birthday = Column(Date, nullable=False)
    user_registration = Column(Date, nullable=False)

    orm_skills = relationship('ormGroup', secondary='orm_user_group')


class ormGroup(Base):
    __tablename__ = 'orm_group'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(40), nullable=False)
    group_count_users = Column(Integer)
    orm_users = relationship('ormUser', secondary='orm_user_group')


class ormGroupHasMembers(Base):
    __tablename__ = 'orm_user_group'

    user_id = Column(Integer,ForeignKey('orm_user.user_id'),primary_key=True)

    group_id = Column(Integer, ForeignKey('orm_group.group_id'), primary_key=True)


