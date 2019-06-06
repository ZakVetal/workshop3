from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getUserData(self, user_phone=None):

        if user_phone:
            user_phone="'{0}'".format(user_phone)
        else:
            user_phone='null'

        query = "select * from table(orm_user_phone.GetUserData({0}))".format(user_phone)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getUserData('Java'))
    print(helper.getUserData())
