from dao.db import OracleDb


class UH:

    def __init__(self):
        self.db = OracleDb()

    def getData(self, name=None):

        if name:
            name="'{0}'".format(name)
        else:
            name='null'

        query = "select * from table(m_name.getData({0}))".format(name)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UH()
