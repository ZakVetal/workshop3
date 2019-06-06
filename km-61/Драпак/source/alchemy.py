from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, DATE, create_engine, Integer
from sqlalchemy.orm import relationship, sessionmaker
import cx_Oracle

Base = declarative_base()


class User(Base):

    __tablename__ = 'User'

    full_name = Column(String(100), primary_key=True)
    location = Column(String(100), nullable=False)


class TODOList(Base):

    __tablename__ = 'TODOList'

    full_name = Column(String(100), ForeignKey('User.full_name'), primary_key=True)
    date = Column(DATE, primary_key=True)
    name = Column(String(50), primary_key=True)


class Action(Base):

    __tablename__ = 'Action'

    full_name = Column(String(100), ForeignKey('User.full_name'), primary_key=True)
    date = Column(DATE, ForeignKey('TODOList.date'), primary_key=True)
    name = Column(String(50), ForeignKey('TODOList.name'), primary_key=True)

    time_open = Column(DATE, primary_key=True)
    time_close = Column(DATE)
    description = Column(String(255), primary_key=True)
    execution_time = Column(Integer)
    location = Column(String(255))


oracle_connection_str = "oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}"

engine = create_engine(
    oracle_connection_str.format(
        username="BlindProrok",
        password="prorok2000",
        hostname="localhost",
        port="1521",
        database="XE",
    )
)

Session = sessionmaker(bind=engine)
session = Session()

VasiliyZaytsev = User(full_name='Vasiliy Zaytsev', location='KPI')
TonyStark = User(full_name='Tony Stark', location='Cinema')
LexaSubotin = User(full_name='Lexa Subotin', location='The Wall')
AriaStark = User(full_name='Aria Stark', location='HDRezka')

SaveTheWorldT1 = TODOList(full_name='Tony Stark', date='26-APR-2019', name='Save the world')
SaveTheWorldT2 = TODOList(full_name='Tony Stark', date='26-APR-2019', name='Click with fingers')
SaveTheWorldA1 = TODOList(full_name='Aria Stark', date='28-APR-2019', name='Save the world')
SaveTheWorldA2 = TODOList(full_name='Aria Stark', date='28-APR-2019', name='Save the world')

ActionT1 = Action(full_name='Tony Stark', date='26-APR-2019', name='Save the world',
                  time_open='26-APR-2019', time_close='26-APR-2019',
                  description='get the gauntlet', execution_time=30*60, location='Cinema')
ActionT2 = Action(full_name='Tony Stark', date='26-APR-2019', name='Click with fingers',
                  time_open='26-APR-2019', time_close='26-APR-2019',
                  description='click your fingers', execution_time=60, location='Cinema')
ActionA1 = Action(full_name='Aria Stark', date='28-APR-2019', name='Save the world',
                  time_open='28-APR-2019', time_close='28-APR-2019',
                  description='jump on the night king', execution_time=60, location='Cinema')
ActionA2 = Action(full_name='Aria Stark', date='28-APR-2019', name='Save the world',
                  time_open='28-APR-2019', time_close='28-APR-2019',
                  description='make the bloody surprise to everyone', execution_time=60, location='Cinema')

session.add_all([VasiliyZaytsev, TonyStark, LexaSubotin, AriaStark,
                 SaveTheWorldT1, SaveTheWorldT2, SaveTheWorldA1, SaveTheWorldA2,
                 ActionT1, ActionT2, ActionA1, ActionA2])

session.commit()