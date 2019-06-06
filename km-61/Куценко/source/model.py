from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_phone = Column(Integer, primary_key=True)
    user_birthday = Column(Date, nullable=False)

    user_d = relationship('user', secondary='user_data')


class date(Base):
    __tablename__ = 'date'
    date = Column(Date, nullable=False)
    user_id = Column(Integer, primary_key=True)
    place_id = Column(Integer, primary_key=False)
    g_date = relationship('date', secondary='g_date')


class place(Base):
    __tablename__ = 'place'

    place_id = Column(Integer, primary_key=False)
    place_name = Column(String(20), nullable=False)
