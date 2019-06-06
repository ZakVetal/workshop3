from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class orm_User_Name(Base):
    __tablename__ = 'ORM_USER_NAME'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_email = Column(String(40))
    user_birthday = Column(Date, nullable=False)
    credit_card = Column(String(16), nullable=False)

    orm_network = relationship('orm_network', secondary='ORM_USER_USE_NETWORK')


class orm_network(Base):
    __tablename__ = 'ORM_NETWORK_NAME'
    network_id = Column(Integer, primary_key=True, )
    network_name = Column(String(20))

    orm_user = relationship('orm_User_Name', secondary='ORM_USER_USE_NETWORK')


class orm_user_use_network(Base):
    __tablename__ = 'ORM_USER_USE_NETWORK'

    user_id = Column(Integer, ForeignKey('ORM_USER_NAME.user_id'), primary_key=True)
    network_id = Column(Integer, ForeignKey('ORM_NETWORK_NAME.network_id'), primary_key=True)
