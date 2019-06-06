from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUser).delete()
session.query(ormMessage).delete()
session.query(ormBoard).delete()

# populate database with new rows

Katia = ormUser( user_name="Katia",
               user_email='kat@gmail.com',
               user_phone='0672867955',
               )



Bob = ormUser( user_name="Bob",
               user_email='bob@gmail.com',
               user_phone='0978612345',
               )


Jack = ormUser( user_name="Jack",
               user_email='	ze2019@gmail.com',
               user_phone='0685896954',
               )



KatiaM = ormMessage(text_mes='Message1')
BobM = ormMessage(text_mes='Message2')
JackM = ormMessage(text_mes='Message3')

# create relations
Katia.orm_message.append(KatiaM)
Bob.orm_message.append(BobM)

Jack.orm_message.append(JackM)



# insert into database
session.add_all([KatiaM,BobM,JackM,Katia,Bob,Jack])

session.commit()
