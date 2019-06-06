import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username="SYSTEM",
        password="87opuzit",
        hostname="localhost",
        port="1521",
        database="Test",
    )
)

Session = sessionmaker(bind=engine)
session = Session()

