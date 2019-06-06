from WorkShop3.dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def User_Name(self, user_id=None):
        if user_id:
            user_id = "'{0}'".format(user_id)
        else:
            user_id = 'null'

        query = "select user_id from ORM_USER_USE_NETWORK({0}))".format(user_id)

        result = self.db.execute(query)
        return result

    def Network_Name(self, network_id=None):

        if network_id:
            network_id = "'{0}'".format(network_id)
        else:
            network_id = 'null'

        query = "select network_id from ORM_USER_USE_NETWORK({0}))".format(network_id)

        result = self.db.execute(query)
        return result
