from model import *
from dao.db import OracleDb
'''import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username="BD",
        password="123123",
        hostname="localhost",
        port="1521",
        database="orcl",
    )
)

Session = sessionmaker(bind=engine)
session = Session()
'''
db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUser).delete()
session.query(ormTodo).delete()
session.query(ormUserTodo).delete()


# populate database with new rows

Ivan = ormUser(
    user_email = 'ioann@gmail.com',
    user_name = 'Ivan',
    user_phone = '380717237123',
)

Zhenya = ormUser(
    user_email='zhenya@gmail.com',
    user_name='Zhenya',
    user_phone='38012312312',
)
homework = ormTodo(
    todo_name = 'homework',
    todo_deadline = '06-JUL-2019',
    user_important = 9
)
cooking = ormTodo(
    todo_name = 'cooking',
    todo_deadline = '05-JUL-2019',
    user_important = 5
)

Ivan.orm_todo.append(homework)
Zhenya.orm_todo.append(cooking)
# insert into database
session.add_all([Ivan,Zhenya,homework,cooking])
session.commit()