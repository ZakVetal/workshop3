from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormSchedule).delete()
session.query(ormGroup).delete()
session.query(ormTeacher).delete()


# populate database with new rows

Best = ormTeacher(
    teacher_id =0,
    teacher_name = "Best",
    teacher_surname = "Perfect",
    teacher_birthday = '04-FEB-2007',
    teacher_patronymict = "Forever",
               )

Good = ormTeacher(
    teacher_id =1,
    teacher_name = "Good",
    teacher_surname = "Yeah",
    teacher_birthday = '05-FEB-2007',
    teacher_patronymict = "Always",
               )
Bad = ormTeacher(
    teacher_id =2,
    teacher_name = "Bad",
    teacher_surname = "Oh",
    teacher_birthday = '06-FEB-2007',
    teacher_patronymict = "****",
               )

KM63 = ormGroup(
    group_name ="KM-63"
               )
KM62 = ormGroup(
    group_name ="KM-62"
               )
KM61 = ormGroup(
    group_name ="KM-61"
               )


Monday = ormSchedule(
    schedule_data = '06-JUN-2007',
    teacher_id=0,
    group_name='KM-63'


               )

Tuesday = ormSchedule(
    schedule_data = '07-JUN-2007',
    teacher_id=0,
    group_name='KM-63'

               )

Wednesday = ormSchedule(
    schedule_data = '08-JUN-2007',
    teacher_id=0,
    group_name='KM-63'

               )

# create relations

# insert into database
session.add_all([Best,Good,Bad,KM63,KM62,KM61,Wednesday,Tuesday,Monday])



session.commit()