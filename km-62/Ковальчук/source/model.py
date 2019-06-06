from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    email = Column(String(255), primary_key=True)
    id = Column(Integer(10), nullable=False)
    full_name = Column(String(255), nullable=False)
    
    orm_Document= relationship('ormDocument', secondary='orm_user_Document')


class ormDocument(Base):
    __tablename__ = 'orm_Document'
    path_file = Column(String(255), primary_key=True)
    name_file = Column(Integer(10), nullable=False)
    description = Column(String(255))


    orm_users = relationship('ormUser', secondary='orm_user_Document')


class ormUserDocument(Base):
    __tablename__ = 'orm_user_Document'

    email = Column(String(255),ForeignKey('orm_user.email'),primary_key = True)
    path_file = Column(String(255), ForeignKey('orm_Document.path_file'), primary_key=True)
