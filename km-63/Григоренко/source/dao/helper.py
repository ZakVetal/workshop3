import cx_Oracle
from dao.db import OracleDb

class UserHelper():

    def __init__(self):
        self.db = OracleDb()


    def createStudent(self,name,group,student_id,email):

        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.create_student", [name,group,student_id,email,status])

        return  status.getvalue()

    def deleteStudent(self,student_id):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("edit.delete_student", [student_id,status])

        return status.getvalue()

    def updateStudent(self,name,group,student_id,email):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.update_student", [name,group,student_id,email,status])

        return status.getvalue()



    def createMark(self,date,mark):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.create_Mark", [ date,mark,status])

        return status.getvalue()
    
    def deleteMark(self,date ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.delete_Mark", [date,status])

        return status.getvalue()

    def updateMark(self,date,mark ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.update_Mark", [date,mark,status])

        return status.getvalue()



    def createFile(self,title,form):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.create_File", [title,form,status])

        return status.getvalue()

    def deleteFile(self,title ):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.delete_File", [title,status])

        return status.getvalue()


    def updateFile(self,title,form):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("edit.update_File", [title,form,status])

        return status.getvalue()


if __name__ == "__main__":

    helper = UserHelper()
