from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class orm_User(Base):
    __tablename__ = 'orm_user'
    user_id=Column(Integer, primary_key=True)
    user_name = Column(Integer, primary_key=True)
    user_password = Column(String(20), nullable=False)
    user_surname = Column(String(40), nullable=False)

    orm_complaint = relationship('orm_complaint', secondary='orm_user_complaint')


class orm_Complaint(Base):
    __tablename__ = 'orm_Complaint'
    complaint_id=Column(Integer, primary_key=True)
    complaint_date = Column(String(20))
    complaint_answer = Column(String(500))
    complaint_txt = Column(String(300))


    orm_user = relationship('orm_user', secondary='orm_user_complaint')


class orm_user_complaint(Base):
    __tablename__ = 'orm_user_complaint'

    user_id = Column(Integer, ForeignKey('orm_user.user_id'), primary_key=True)
    discipline_id=Column(String(255),ForeignKey('orm_Complaint.complaint_id'),primary_key = True)