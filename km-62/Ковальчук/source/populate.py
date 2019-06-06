from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUserDocument).delete()
session.query(ormDocument).delete()
session.query(ormUser).delete()


# populate database with new rows

Julia = ormUser( email='julia@gmail.com',
				full_name='Julia',
               id='324'               
               )



Vovo = ormUser( email='Vova@gmail.com',
				full_name='Vova',
               id='54'               
               )


Anna = ormUser( email='Anna@gmail.com',
				full_name='Anna',
               id='32'               
               )


Java = ormDocument(patch_file='Java')
Oracle = ormDocument(patch_file='Oracle')

# create relations
Bob.orm_Documents.append(Java)
Bob.orm_Documents.append(Oracle)

Boba.orm_Documents.append(Java)

Boban.orm_Documents.append(Oracle)

# insert into database
session.add_all([Java,Julia,Boban,Vova,Anna])

session.commit()
