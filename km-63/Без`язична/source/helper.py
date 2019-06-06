import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()


    def createUser(self, email,password,contr):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_user", [email,password,contr,status])

        return  status.getvalue()

    def dropUser(self,email):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("my_pack.drop_user", [email , status])

        return status.getvalue()

    def updateUser(self, email,password,contr):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_user", [email,password,contr,status])

        return status.getvalue()



    def createEvent(self, email,date,name,time,longitude,latitude):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.new_Event", [email,date,name,time,longitude,latitude, status])

        return status.getvalue()

    def updateEvent( self, email,date,name,time,longitude,latitude):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_Event", [self, email,date,name,time,longitude,latitude, status])

        return status.getvalue()

    def dropEvent(self, name ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_Event", [name, status])

        return status.getvalue()


    def createCalendar(self, email,date):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_Calendar", [ email,date, status])

        return status.getvalue()

    def dropCalendar(self, date ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_Calendar", [ date , status])

        return status.getvalue()


    def Finding(self,number,date,min,max):

        result = self.db.cursor.var(cx_Oracle.Tbl)

        return self.db.cursor.callfunc("my_pack.GetMod", cx_Oracle.OBJECT, [number,date,min,max])


if __name__ == "__main__":

    helper = UserHelper()