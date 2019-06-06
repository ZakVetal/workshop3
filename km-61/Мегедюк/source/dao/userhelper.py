from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getUserData(self, user_locale=None):

        if user_locale:
            user_locale="'{0}'".format(user_locale)
        else:
            user_locale='null'

        query = "select * from table(orm_user_locale.GetUserData({0}))".format(user_locale)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getUserData('Java'))
    print(helper.getUserData())
