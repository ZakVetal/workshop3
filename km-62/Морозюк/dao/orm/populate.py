from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormGroupHasMembers).delete()
session.query(ormGroup).delete()
session.query(ormUser).delete()


# populate database with new rows
Bob = ormUser( user_name="Bob",
               user_birthday='9-OCT-1992',
               user_email='bob@gmail.com',
               user_department='hr',
               user_registration='10-SEP-2010'
               )

Boba = ormUser(  user_name="Boba",
               user_birthday='9-OCT-1982',
               user_email='boba@gmail.com',
               user_department='manager',
               user_registration='10-SEP-2008'
               )

Boban = ormUser( user_name="Boban",
                 user_birthday='12-MAY-1995',
                 user_email='boban@gmail.com',
                 user_department='hr',
                 user_registration='10-SEP-2015'
               )

Biba = ormUser( user_name="Biba",
                 user_birthday='12-MAY-1997',
                 user_email='biba@gmail.com',
                 user_department='admin',
                 user_registration='10-SEP-2013'
               )

hr = ormGroup(group_name="hr", group_count_users=2)
memasiki = ormGroup(group_name="memasiki", group_count_users=3)

# create relations
hr.orm_users.append(Bob)
hr.orm_users.append(Boban)

memasiki.orm_users.append(Bob)
memasiki.orm_users.append(Boban)
memasiki.orm_users.append(Biba)


# insert into database
session.add_all([hr,memasiki,Boban,Boba,Bob,Biba])

session.commit()