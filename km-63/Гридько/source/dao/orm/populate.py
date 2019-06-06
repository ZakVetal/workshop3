from dao.orm.model import *
from dao.db import *

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order

#session.query(ormFunctionVariable).delete()

#session.query(ormTypeData).delete()
#session.query(ormData).delete()
session.query(ormTest).delete()


# populate database with new rows

Sasha = ormUser(user_name = 'Sasha',
                role = 'teatcher')
func = ormFunction(function_name = 'sum',
                   function_type= 'int',
                   user_name_fk = 'Sasha')
variable = ormFunctionVariable(variable_name = 'a',
                               type_variable='int',
                                function_name_fk = 'sum'
                                 )



# create relations





# insert into database
session.add_all([Sasha,func,variable])

session.commit()