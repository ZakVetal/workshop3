from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    
    user_locale = Column(String(40), nullable=False)
    

    orm_users = relationship('ormUser', secondary='orm_user_locale')


class Place(Base):
   __tablename__ = 'orm_Place'
    user_locale = Column(varchar(40), primary_key=True)
    places_date = Column(Date, nullable=False)
   
class ormPhoto2(Base):
     __tablename__ = 'orm_Photo2'
      photo2_name = Column(varchar(40), primary_key=True)
      photo2_date = Column(Date, nullable=False)
 class ormPhoto1(Base):
     __tablename__ = 'orm_Photo1'
      photo1_name = Column(varchar(40), primary_key=True)
      user_locale = Column(varchar(40),ForeignKey('orm_user.user_locale'), nullable=False)
      photo1_date = Column(Date, nullable=False)       

   
     user_locale = Column(String(40), ForeignKey('orm_user.user_locale'), primary_key=True)
