from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class ormSchedule(Base):

    __tablename__ = 'orm_schedules'

    schedule_data = Column(Date, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('orm_teachers.teacher_id'))
    group_name = Column(String(6), ForeignKey('orm_groups.group_name'))
    group = relationship("ormGroup", back_populates="teachers")
    teacher = relationship("ormTeacher", back_populates="groups")


class ormGroup(Base):

    __tablename__ = 'orm_groups'

    group_name = Column(String(6), primary_key=True)
    teachers = relationship("ormSchedule", back_populates="group")



class ormTeacher(Base):

    __tablename__ = 'orm_teachers'

    teacher_id = Column(Integer,primary_key = True)
    teacher_name = Column(String(10), nullable=False)
    teacher_surname = Column(String(15), nullable=False)
    teacher_birthday = Column(Date, nullable=False)
    teacher_patronymict = Column(String(15), nullable=False)
    groups = relationship("ormSchedule", back_populates="teacher")


