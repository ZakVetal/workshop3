import datetime


from sqlalchemy import func, text
from sqlalchemy.exc import IntegrityError, DatabaseError, InvalidRequestError

from dao.db import OracleDb
from dao.orm.model import Base, ormTest, ormData, ormVariable
import requests
import random


class UserHelper:

    def __init__(self):
        self.db = OracleDb()


    def getTestCount(self, variable_name=None):

        if variable_name:
            variable_name = "'{0}'".format(variable_name)
        else:
            variable_name = 'null'

        query = "select * from table(orm_test_count.GetTestCount({0}))".format(variable_name)

        result = self.db.execute(query)
        return result.fetchall()







if __name__ == "__main__":
    db = OracleDb()
    helper = UserHelper()
    print(helper.test())
    print(helper.getTestCount('a'))




