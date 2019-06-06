from Workshop.application.dao.connection import OracleConnection


class DBHelper:

    def find_student(self, firstname=None, lastname=None, group=None):
        def null_check(value):
            return f"'{value}'" if value != None else 'null'

        with OracleConnection() as db:
            return db.execute(
                f"SELECT * FROM STUDENT_SEARCH.FIND({null_check(firstname)},{null_check(lastname)},{null_check(group)})")


