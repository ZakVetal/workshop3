from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class OrmFile(Base):
    __tablename__ = 'orm_file'

    file_id = Column(Integer, primary_key=True)
    file_name = Column(String(20), nullable=False)
    file_type = Column(String(6), nullable=False)
    file_context = Column(String(40))
    file_date = Column(Date, nullable=False)
    file_owner_id = Column(Integer, ForeignKey('orm_user.user_id'), nullable=True)

    orm_file = relationship('OrmUser', secondary='orm_file_editor')


class OrmUser(Base):
    __tablename__ = 'orm_user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(40))
    user_login = Column(String(20), nullable=False)

    orm_owner = relationship('OrmFile')
    orm_editor = relationship('OrmFile', secondary='orm_file_editor')


class OrmFileEditor(Base):
    __tablename__ = 'orm_file_editor'

    user_id = Column(Integer, ForeignKey('orm_user.user_id'), primary_key=True)
    file_id = Column(Integer, ForeignKey('orm_file.file_id'), primary_key=True)
