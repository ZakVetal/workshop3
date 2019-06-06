from dao.db import OracleDb
from dao.orm.entities import *

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session

# clear all tables in right order
session.query(OrmFileEditor).delete()
session.query(OrmFile).delete()
session.query(OrmUser).delete()

# populate database with new rows

ich = OrmUser(user_name="ich",
              user_login='mich')

du = OrmUser(user_name="du",
             user_login='dich')

er = OrmUser(user_name="er",
             user_login='ihm')

sie = OrmUser(user_name="sie",
              user_login='ihr')

Sie = OrmUser(user_name="Sie",
              user_login='ihnen')

test = OrmFile(file_name='test',
               file_type='doc',
               file_context='this is test',
               file_date='10-OCT-1999')

hi = OrmFile(file_name='hello',
             file_type='txt',
             file_context='hello world',
             file_date='20-OCT-2000')

bye = OrmFile(file_name='good bye',
              file_type='txt',
              file_context='klik klak',
              file_date='20-OCT-2000')

file = OrmFile(file_name='cursach',
               file_type='doc',
               file_context='aaaaaaaaa stop it',
               file_date='20-OCT-2016')

file1 = OrmFile(file_name='hallo',
                file_type='doc',
                file_context='ich heisse eugene',
                file_date='20-OCT-2016')

file2 = OrmFile(file_name='gomgomgom',
                file_type='doc',
                file_context='good night in museum',
                file_date='20-OCT-2016')

# create relations
er.orm_editor.append(hi)
er.orm_editor.append(test)
er.orm_owner.append(test)

ich.orm_editor.append(test)
ich.orm_owner.append(file)

du.orm_editor.append(file1)
du.orm_editor.append(bye)
du.orm_owner.append(file1)

sie.orm_editor.append(file2)
sie.orm_owner.append(hi)
sie.orm_owner.append(bye)
sie.orm_owner.append(file2)

Sie.orm_editor.append(file)
Sie.orm_editor.append(test)

# insert into database
session.add_all([ich, er, du, sie, Sie, test, hi, bye, file, file1, file2])

session.commit()
