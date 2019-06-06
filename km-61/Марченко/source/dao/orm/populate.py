from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session


user1 = ormUser(
            user_name="alex",
            user_student_card_id="1",
            user_password='1234',
            user_complaint='texttext'
               )

user2 = ormUser(
            user_name="vova",
            user_student_card_id="2",
            user_password='1234qwerty',
            user_complaint='texttext'

)
user3 = ormUser(
            user_name="sasha",
            user_student_card_id="3",
            user_password='8888888',
            user_complaint = 'texttext'

)




complaint1 = orm_Discipline(complaint_text='complaint_txt')
complaint2= orm_Discipline(complaint_text='complaint_txt')
complaint3 = orm_Discipline(complaint_text='complaint_txt')


user1.orm_Complaint.append(complaint1)
user2.orm_Complaint.append(complaint2)
user3.orm_Complaint.append(complaint3)


# insert into database
session.add_all([complaint1, complaint2, complaint3, user1, user2, user3])

session.commit()