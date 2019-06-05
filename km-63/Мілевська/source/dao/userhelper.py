from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getUserData(self, **kwargs):
        first_name = kwargs.get('first_name', 'null')
        last_name = kwargs.get('last_name', 'null')

        query = "select * from table(orm_user_package.GetUserData())" #.format(first_name, last_name)
        print(query)

        result = self.db.execute(query)
        print(result)
        return result


if __name__ == "__main__":

    helper = UserHelper()