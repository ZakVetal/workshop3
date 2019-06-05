from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(63), nullable=False)
    user_name = Column(String(20), nullable=False)
    user_first_name = Column(String(63), nullable=False)
    user_last_name = Column(String(63), nullable=False)

    orm_events = relationship('ormEvent', secondary='orm_attendance')


class ormEvent(Base):
    __tablename__ = 'orm_event'

    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(40), nullable=False)
    event_date = Column(Date, nullable=False)
    orm_users = relationship('ormUser', secondary='orm_attendance')


class ormUserAttendedEvent(Base):
    __tablename__ = 'orm_attendance'
    user_id = Column(Integer, ForeignKey('orm_user.user_id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('orm_event.event_id'), primary_key=True)
