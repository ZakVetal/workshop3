from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session


Test1 = ormUser( user_name="test1",
               user_student_card_id="1111test1",
               user_surname='test1'
               )

Test2 = ormUser( user_name="test2",
               user_student_card_id="2222test2",
               user_surname='test2'
               )
Test3 = ormUser( user_name="test3",
               user_student_card_id="3333test3",
               user_surname='test3'
               )




discipline1 = orm_Discipline(skill_name='discipline1')
discipline2= orm_Discipline(skill_name='discipline2')
discipline3 = orm_Discipline(skill_name='discipline3')


# create relations
Test1.orm_Discipline.append(discipline1)
Test2.orm_Discipline.append(discipline2)
Test3.orm_Discipline.append(discipline3)


# insert into database
session.add_all([discipline1, discipline2, discipline3, Test1, Test2, Test3])

session.commit()