from dao.db import OracleDb


class WorkerHelper:

    def __init__(self):
        self.db = OracleDb()

    def GetJobData(self, worker_surname=None, assignment_name=None):
        if worker_surname:
            worker_surname = "'{0}'".format(worker_surname)
        else:
            worker_surname = 'null'

        if assignment_name:
            assignment_name = "'{0}'".format(assignment_name)
        else:
            assignment_name = 'null'

        query = "select * from table(orm_worker_assignment.GetJob({0}, {1}))".format(worker_surname, assignment_name)

        result = self.db.execute(query)
        return result.fetchall()