import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()

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

    def newImprovement(self, a ,b):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.new_improvement", [a, b, status])

        return status.getvalue()

    def updateImprovement(self, a ,b ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.update_improvement", [a, b, status])

        return status.getvalue()

    def delImprovement(self, a ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.del_channel", [a, status])

        return status.getvalue()

    def newQeueu(self, a ,b,c ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.new_qeueu", [a, b, c, status])

        return status.getvalue()

    def delQeueu(self, a, b ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit_u.del_qeueu", [a, b, status])

        return status.getvalue()


    def search (self,a,b):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        result = cursor.var(cx_Oracle.OBJECT)

        return cursor.callfunc("search.search", cx_Oracle.OBJECT, [a, b])



if __name__ == "__main__":

    helper = UserHelper() 