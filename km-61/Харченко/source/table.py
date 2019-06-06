import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username="harchen",
        password="cgvxtx1223",
        hostname="localhost",
        port="1521",
        database="xe",
    )
)

Session = sessionmaker(bind=engine)
session = Session()

News1 = ormNews(
                    news_name = "new movie about football",
                    text = "this year there will be a new movie about football that will tell about the career of Mesi",
                    sourse = "footballman",
               )

News2 = ormNews( 
                    news_name = "exhibition E3 2019",
                    text = "June 8, 2019 will be held the annual exhibition E3 where Sony will present 14 new games",
                    sourse = "newstwo",
               )

News3 = ormNews( 
                    news_name = "new scandal on the field",
                    text = "aggressive athletes beat judge",
                    sourse = "notface",
               )

view1 = ormNews( nick = "Bob",
                new_id = "2"
                date_read = '11-OCT-2018',
               )
view2 = ormNews(nick = "Bob",
                new_id = "3"
                date_read = '11-OCT-2018',
               )

view3 = ormNews( nick = "Bobi",
                new_id = "1"
                date_read = '14-OCT-2018',
               )
               
view4 = ormNews( nick = "Bobi",
                new_id = "2"
                date_read = '15-OCT-2018',
               )

Sports = ormclass(class_name='Sports')
Games = ormclass(class_name='Games')
Films = ormclass(class_name='Films')

# create relations
News_id1.orm_class.append(Sports)
News_id1.orm_class.append(Films)

News_id2.orm_class.append(Games)

News_id3.orm_class.append(Sports)

# insert into database
session.add_all([Sports,Films,Games,News1,News2,News3,view1,view2,view3,view4])

session.commit()