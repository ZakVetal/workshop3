import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()

#for user
    def newUser(self, a,b,c,d):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.new_user", [a, b, c, d,status])

        return  status.getvalue()

    def delUser(self,a):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("edit_u.del_user", [a , status])

        return status.getvalue()

    def updateUser(self, a,b,c,d):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.update_user", [a, b, c, d,status])

        return status.getvalue()

#for channel
    def newChannel(self, a,b):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.new_channel", [a, b, status])

        return status.getvalue()

    def updateChannel(self, a ,b ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.update_channel", [a, b, status])

        return status.getvalue()

    def delChannel(self, a ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.del_channel", [a, status])

        return status.getvalue()
#for subscription
    def newSub(self, a ,b,c ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.new_subscription", [a, b, c, status])

        return status.getvalue()

    def delSub(self, a, b ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.del_subscription", [a, b, status])

        return status.getvalue()


    def search (self,a,b):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        result = cursor.var(cx_Oracle.OBJECT)

        return cursor.callfunc("search.search", cx_Oracle.OBJECT, [a, b])











if __name__ == "__main__":

    helper = UserHelper()