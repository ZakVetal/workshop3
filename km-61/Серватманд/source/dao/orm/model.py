from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class orm_User_Name(Base):
    __tablename__ = 'orm_user_data'

    user_student_card_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    user_surname = Column(String(40), nullable=False)

    orm_network = relationship('orm_network', secondary='ORM_USER_USE_NETWORK')


class orm_Discipline(Base):
    __tablename__ = 'ORM_NETWORK_NAME'
    discipline_id=Column(Integer, primary_key=True)
    discipline_name = Column(String(20))
    discipline_amount = Column(String(20))
    discipline_mark = Column(String(3))


    orm_user = relationship('orm_User_Name', secondary='orm_user_Discipline')


class ormUserDiscipline(Base):
    __tablename__ = 'ORM_USER_USE_NETWORK'

    user_id = Column(Integer, ForeignKey('orm_user_data.user_student_card_id'), primary_key=True)
    discipline_id=Column(String(255),ForeignKey('orm_Discipline.discipline_id'),primary_key = True)