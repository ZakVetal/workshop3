import datetime

from dao.orm.model import *
from dao.db import *

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order

#session.query(ormFunctionVariable).delete()

#session.query(ormTypeData).delete()
#session.query(ormData).delete()



# populate database with new rows


'''test = ormTest(test_name='testb',
               result='4')
variable = ormVariable(variable_name='b',
                       variable_type='int')'''
now = datetime.datetime.now()
data = ormData(data= now,
                       value= '4',
                       variable_name_fk= 'b',
                       test_fk='testb')

session.add_all([data])

session.commit()



# create relations





# insert into database


session.commit()