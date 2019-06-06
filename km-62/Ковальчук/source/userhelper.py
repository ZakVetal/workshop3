from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getDocumentData(self, patch_file=None):

        if patch_file:
            patch_file="'{0}'".format(patch_file)
        else:
            patch_file='null'

        query = "select * from table(orm_user_DocumentS.GetDocumentData({0}))".format(patch_file)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getDocumentData('Java'))
    print(helper.getDocumentData())
