from WorkShop3.dao.orm.model import *
from WorkShop3.dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session


User1 = orm_User_Name(user_name="User1",
                    user_email='user1@gmail.com',
                    user_birthday='11-OCT-2001',
                    credit_card='1111222233334444'
                    )

User2 = orm_User_Name(user_name="User2",
                    user_email='user2@gmail.com',
                    user_birthday='12-OCT-2002',
                    credit_card='2222333344445555'
                    )

User3 = orm_User_Name(user_name="User3",
                    user_email='user3@gmail.com',
                    user_birthday='13-OCT-2003',
                    credit_card='3333444455556666'
                    )


Facebook = orm_network(network_name='Facebook')
VKontakte = orm_network(network_name='VKontakte')
Instagram = orm_network(network_name='Instagram')

# create relations
User1.orm_network.append(Facebook)
User1.orm_network.append(VKontakte)
User1.orm_network.append(Instagram)

User2.orm_network.append(Instagram)

User3.orm_network.append(VKontakte)

# insert into database
session.add_all([Facebook, VKontakte, Instagram, User1, User2, User3])

session.commit()
