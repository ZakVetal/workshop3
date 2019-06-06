from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'Student'
    Student_id = Column(String(100), primary_key=True)
    Student_name = Column(String(100), nullable=False)
    Student_group = Column(String(100), nullable=False)
    Student_email = Column(String(100), nullable=False)


class File(Base):
    __tablename__ = 'File'
    Student_id = Column(String(100), ForeignKey('Student.Student_id'), primary_key=True)
    File_title = Column(String(100), primary_key=True)
    File_format = Column(String(100), nullable=False)
    Student = relationship('Student_id')


class Mark(Base):
    __tablename__ = 'Change'

    Student_id = Column(String(100), ForeignKey('Student.Student_id'), primary_key=True)
    File_title = Column(String(100), ForeignKey('File.File_title'), primary_key=True)
    Mark = Column(Integer)
    Mark_date = Column(Date, primary_key=True)
    Student = relationship('Student_id')
    File = relationship('File_title')
