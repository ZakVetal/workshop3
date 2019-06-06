from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from dao.db import OracleDb

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'
    user_name = Column(String(20), primary_key=True)
    role = Column(String(20))
    func = relationship("ormFunction",back_populates="child")






class ormFunction(Base):
    __tablename__ = 'orm_function'
    function_name = Column(String(40), primary_key=True)
    function_type = Column(String(20))
    user_name_fk = Column(String(20),ForeignKey('orm_user.user_name'))
    child = relationship("ormUser", back_populates="func")
    parent = relationship("ormFunctionVariable",back_populates="childVariable")


class ormFunctionVariable(Base):
    __tablename__ = 'orm_variable'

    variable_name = Column(String(40), primary_key=True)
    type_variable = Column(String(40))
    function_name_fk = Column(String(40),ForeignKey('orm_function.function_name'))
    childVariable = relationship("ormFunction",back_populates="parent")
    parentVariable = relationship("ormData",back_populates="childData")




class ormData(Base):
    __tablename__ = 'orm_data'
    data = Column(Date, primary_key=True)
    value = Column(String(40))
    variable_name_fk = Column(String(40), ForeignKey('orm_variable.variable_name'))
    childData = relationship("ormFunctionVariable", back_populates="parentVariable")
    test_fk = Column(String(40), ForeignKey('orm_test.test_name'))
    parentData = relationship("ormTest", back_populates="childTest")


class ormTest(Base):
    __tablename__ = 'orm_test'
    test_name = Column(String(40),primary_key=True)
    result = Column(String(40))
    childTest = relationship("ormData", back_populates="parentData")


db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)