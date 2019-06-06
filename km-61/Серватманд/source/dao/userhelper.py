from workshop3.dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def User_data(self, user_id=None):
        if user_id:
            user_id = "'{0}'".format(user_id)
        else:
            user_id = 'null'

        query = "select user_id from ORM_USER_USE_NETWORK({0}))".format(user_id)

        result = self.db.execute(query)
        return result

    def Discipline_Name(self, discipline_id=None):

        if discipline_id:
            discipline_id = "'{0}'".format(network_id)
        else:
            network_id = 'null'

        query = "select network_id from ORM_USER_USE_NETWORK({0}))".format(network_id)

        result = self.db.execute(query)
return result