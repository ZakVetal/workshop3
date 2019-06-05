from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUserAttendedEvent).delete()
session.query(ormEvent).delete()
session.query(ormUser).delete()


session.add_all([
    ormUser(user_name='johnsmith', user_email='john@gmail.com', user_first_name='John', user_last_name='Smith'),
    ormUser(user_name='topsy', user_email='top@gmail.com', user_first_name='Topsy', user_last_name='Daiver'),
    ormUser(user_name='clark', user_email='kent@gmail.com', user_first_name='Clark', user_last_name='Kent'),
    ormUser(user_name='Ann', user_email='ann@gmail.com', user_first_name='Ann', user_last_name='Smith'),
    ormEvent(event_name='Atlas', event_date='10-OCT-2018', ),
    ormEvent(event_name='Zahid', event_date='10-SEP-2010', ),
    ormEvent(event_name='Sziget', event_date='10-FEB-2010', ),
])

event = session.query(ormEvent).first()
event.orm_users.append(session.query(ormUser).first())

session.commit()
