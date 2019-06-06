from workshop3.dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def User_data(self, user_id=None):
        if user_id:
            user_id = "'{0}'".format(user_id)
        else:
            user_id = 'null'

        query = "select user_id from ORM_USER_USE_COMPLAINT({0}))".format(user_id)

        result = self.db.execute(query)
        return result

    def Complaint_Name(self, complaint_id=None):

        if complaint_id:
            complaint_id = "'{0}'".format(complaint_id)
        else:
            complaint_id = 'null'

        query = "select complaint_id from ORM_USER_USE_COMPLAINT({0}))".format(complaint_id)

        result = self.db.execute(query)
return result