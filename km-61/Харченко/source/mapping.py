from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormNews(Base):
    __tablename__ = 'orm_News'

    new_id = Column(Integer, primary_key=True)
    news_name = Column(String(30), nullable=False)
    text = Column(String(10000), nullable=False)
    sourse = Column(String(30), nullable=False)

    orm_class = relationship('ormclass', secondary='orm_New_has_class')


class ormclass(Base):
    __tablename__ = 'orm_class'
    class_name = Column(String(15), primary_key=True)

    orm_News = relationship('ormNews', secondary='orm_New_has_class')


class ormNewHasClass(Base):
    __tablename__ = 'orm_New_has_class'

    new_id = Column(Integer,ForeignKey('orm_News.new_id'),primary_key = True)
    sclass_name = Column(String(15), ForeignKey('orm_class.class_name'), primary_key=True)
    
class ormDate(Base):
    __tablename__ = 'orm_Date'
    nick = Column(String(15), primary_key=True)
    new_id = Column(Integer, primary_key=True)
    date_read = Column(Date, nullable=False)