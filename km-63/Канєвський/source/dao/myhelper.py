from sqlalchemy import func

from dao.db import OracleDb
from dao.orm.model import ormSchedule


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getVariable(self, group_name=None):

        if group_name:
            group_name = "'{0}'".format(group_name)
        else:
            group_name = 'null'

        query = "select * from table(ORM_COUNT.GetCountData({0}))".format(group_name)
        print(query)
        result = self.db.execute(query)
        return result.fetchall()



    def test(self):
        db = OracleDb()
        query1 = (
                db.sqlalchemy_session.query(
                    ormSchedule.group_name,
                    func.count(ormSchedule.group_name).label('skill_count')
                ). \

                    group_by(ormSchedule.group_name)
            ).all()
        print(query1)




if __name__ == "__main__":

     helper = UserHelper()
     print(helper.getVariable('KM-63'))
     print(helper.test())