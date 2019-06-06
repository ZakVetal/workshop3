from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormLocalPlaces).delete()
session.query(ormUser).delete()


# populate database with new rows


Bob = ormUser( user_locale='49.6976804,29.3422215,8')



Boba = ormUser( user_locale='50.2015433,28.6346132,11.5')


Boban = ormUser( user_locale='49.9664237,29.4257384,14')




Local1=ormLocalPlaces(local_place_name = 'Киев')
Local2=ormLocalPlaces(local_place_name = 'Житомир')
Local3=ormLocalPlaces(local_place_name = 'Буча')

# create relations
Bob.orm_localplaces.append(Киев)
Bob.orm_localplaces.append(Житомир)
Bob.orm_localplaces.append(Буча)

Bob.orm_localplaces.append(Киев)

Boba.orm_localplaces.append(Житомир)

# insert into database
session.add_all([Boba,Bob,Boban,Local1,Local2,Local3])
    
    session.commit()
