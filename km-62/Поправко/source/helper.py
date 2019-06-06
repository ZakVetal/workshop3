import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()


    def createUser(self, user_name,user_email,birth,contr):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_User", [user_name,user_email,birth,contr,status])

        return  status.getvalue()

    def dropUser(self,user_name):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("my_pack.drop_User", [user_name ])

        return status.getvalue()

    def updateUser(self, user_name,useremail,user_id):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_User", [user_name,user_email,user_id])

        return status.getvalue()



    def createModule(self, time_of_review,like):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.new_Module", [time_of_review,like])

        return status.getvalue()

    def updateModule(self, time_of_review,like ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_Module", [time_of_review,like])

        return status.getvalue()

    def dropModule(self, time_of_review ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_Module", [time_of_review])

        return status.getvalue()


    def createlearning(self, user_name, mod_name,daterep,point):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_learning", [ user_name, mod_name,daterep,point])

        return status.getvalue()

    def droplearning(self, user_name, mod_name ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_learning", [ user_name, mod_name ])

        return status.getvalue()


    def Finding(self,number,date,min,max):

        result = self.db.cursor.var(cx_Oracle.Tbl)

        return self.db.cursor.callfunc("my_pack.GetMod", cx_Oracle.OBJECT, [number,date,min,max])


if __name__ == "__main__":

    helper = UserHelper()