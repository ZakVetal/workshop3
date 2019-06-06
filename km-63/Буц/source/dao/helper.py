import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()


    def createStudent(self, daybook,name,birth,contr):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_student", [daybook,name,birth,contr,status])

        return  status.getvalue()

    def dropStudent(self,daybook):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("my_pack.drop_student", [daybook , status])

        return status.getvalue()

    def updateStudent(self, daybook,name,birth,contr):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_student", [daybook,name,birth,contr,status])

        return status.getvalue()



    def createModule(self, modname,teacher):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.new_Module", [modname,teacher, status])

        return status.getvalue()

    def updateModule(self, modname,teacher ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.update_Module", [modname,teacher, status])

        return status.getvalue()

    def dropModule(self, modname ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_Module", [modname, status])

        return status.getvalue()


    def createlearning(self, daybook, mod_name,daterep,point):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.create_learning", [ daybook, mod_name,daterep,point, status])

        return status.getvalue()

    def droplearning(self, daybook, mod_name ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("my_pack.drop_learning", [ daybook, mod_name , status])

        return status.getvalue()


    def Finding(self,number,date,min,max):

        result = self.db.cursor.var(cx_Oracle.Tbl)

        return self.db.cursor.callfunc("my_pack.GetMod", cx_Oracle.OBJECT, [number,date,min,max])


if __name__ == "__main__":

    helper = UserHelper()