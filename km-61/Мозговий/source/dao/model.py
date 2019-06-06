from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Doc(Base):
    __tablename__ = 'Doc'
    Doc_name = Column(String(256), primary_key=True)
    DocCreationDate = Column(Date, primary_key=True)
    DocAuthor_name = Column(String(256), primary_key=True)
    DocDescription = Column(String(256))
    orm_branch = relationship('Branch')


class Branch(Base):
    __tablename__ = 'Branch'
    Doc_name = Column(String(256), ForeignKey('Doc.Doc_name'), primary_key=True)
    DocCreationDate = Column(Date, ForeignKey('Doc.DocCreationDate'), primary_key=True)
    DocAuthor_name = Column(String(256), ForeignKey('Doc.DocAuthor_name'), primary_key=True)
    Branch_name = Column(String(256), primary_key=True)
    MainBranch_name = Column(String(256), primary_key=True)
    BranchCreationDate = Column(Date, primary_key=True)
    BranchAuthor_name = Column(String(256), primary_key=True)
    orm_change = relationship('Change')


class Change(Base):
    __tablename__ = 'Change'

    Doc_name = Column(String(256), ForeignKey('Branch.Doc_name'), primary_key=True)
    DocCreationDate = Column(Date, ForeignKey('Branch.DocCreationDate'), primary_key=True)
    DocAuthor_name = Column(String(256), ForeignKey('Branch.DocAuthor_name'), primary_key=True)
    Branch_name = Column(String(256), ForeignKey('Branch.Branch_name'), primary_key=True)
    MainBranch_name = Column(String(256), ForeignKey('Branch.MainBranch_name'), primary_key=True)
    BranchCreationDate = Column(Date, ForeignKey('Branch.BranchCreationDate'), primary_key=True)
    BranchAuthor_name = Column(String(256), ForeignKey('Branch.BranchAuthor_name '), primary_key=True)
    Change_name = Column(String(256), primary_key=True)
    ChangeCreationDate = Column(Date, primary_key=True)
    ChangeAuthor_name = Column(String(256), primary_key=True)
    DocDescription = Column(String(256))
