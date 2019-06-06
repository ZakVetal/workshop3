from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    user_phone = Column(String(13), primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_email = Column(String(40))


    orm_message = relationship('ormMessage', secondary='orm_board')


class ormMessage(Base):
    __tablename__ = 'orm_message'
    time_send = Column(Data, primary_key=True)
    text_message = Column(String(40), nullable=False)
 
    orm_users = relationship('ormUser', secondary='orm_board')


class ormBoard(Base):
    __tablename__ = 'orm_board'
    add_time = Column(Data, primary_key=True)
    time_send_fk =Column(Data,ForeignKey('orm_message.time_send'), primary_key=True)
    user_phone_fk =Column(String(13),  ForeignKey('orm_user.user_phone'),primary_key=True)
    text_board =Column(String(40), nullable=False)
