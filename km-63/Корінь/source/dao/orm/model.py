from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from dao.db import OracleDb

Base = declarative_base()





class ormVariable(Base):
    __tablename__ = 'orm_variable'

    variable_name = Column(String(40), primary_key=True)
    variable_type = Column(String(40))
    variableRelationShip = relationship("ormData", back_populates="variable_relationship")


class ormData(Base):
    __tablename__ = 'orm_data'
    data = Column(Date, primary_key=True)
    value = Column(String(40))
    variable_name_fk = Column(String(40), ForeignKey('orm_variable.variable_name'))

    test_fk = Column(String(40), ForeignKey('orm_test.test_name'))
    test_relationship = relationship("ormTest", back_populates="testRelationship")
    variable_relationship = relationship("ormVariable", back_populates="variableRelationShip")

class ormTest(Base):
    __tablename__ = 'orm_test'
    test_name = Column(String(40),primary_key=True)
    result = Column(String(40))
    testRelationship = relationship("ormData", back_populates="test_relationship")


db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)