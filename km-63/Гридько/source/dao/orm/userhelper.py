

from dao.db import OracleDb



class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getVariable(self, user_name=None):

        if user_name:
            user_name = "'{0}'".format(user_name)
        else:
            user_name = 'null'

        query = "select * from table(ORM_USER_FUNCTION.GetVariable({0}))".format(user_name)

        result = self.db.execute(query)
        return result.fetchall()

    def getVariables(self, function_name=None):

        if function_name:
            function_name = "'{0}'".format(function_name)
        else:
            function_name = 'null'

        query = "select * from table(orm_user_Function_search.GetVariable({0}))".format(function_name)

        result = self.db.execute(query)
        return result.fetchall()





if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getVariable('Roma'))

    #print(helper.newTeatcher('Oleksandr','teacther','public static int summ ( int p1 , int p2 , int p3   ){return p1+p2+p3;}'))
    #print(helper.newUser('Oleksandr','Roma','student','public static int summm ( int pp1 , int pp2 , int pp3   ){return pp1+pp2+pp3;}'))


