from db import OracleDb


class MyHelper:

    def init(self):
        self.db = OracleDb()

    def getUserData(self, group_name = None):

        if group_name:
            group_name="'{0}'".format(group_name)
        else:
            group_name='null'

        query = "select * from table(orm_user.getUserData({0}))".format(group_name)

        result = self.db.execute(query)
        return result.fetchall()

    def getTodoData(self, todo_name = None):

        if todo_name:
            todo_name="'{0}'".format(todo_name)
        else:
            todo_name='null'

        query = "select * from table(orm_todo.getTodoData({0}))".format(todo_name)

        result = self.db.execute(query)
        return result.fetchall()

    def newUser(self, user_email, user_name, user_phone):

        cursor = self.db.cursor

        user_id = cursor.var(cx_Oracle.NATIVE_INT)
        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("USER_AUTH.NEW_USER", [user_id, status, user_email, user_name, user_phone])

        return user_id.getvalue(), status.getvalue()

    def deleteTodo(self, todo_name):
        cursor = self.db.cursor

        status = cursor.var(cx_Oracle.STRING)
        cursor.callproc("std.drop_todo", [status, todo_name])

        return status.getvalue()


if name == "main":

    helper = MyHelper()