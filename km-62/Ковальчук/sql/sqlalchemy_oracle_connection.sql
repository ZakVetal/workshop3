import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username="username",
        password="password",
        hostname="host",
        port="port",
        database="service",
    )
)

Session = sessionmaker(bind=engine)
session = Session()
