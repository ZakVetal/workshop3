from flask_wtf import Form
from wtforms import StringField, SubmitField
from dao.db import OracleDb


class SearchForm(Form):
    user_name = StringField('User name: ')

    file_name = StringField('File name:  ')

    submit = SubmitField('Search')

    def search(self):
        db = OracleDb()

        user = f"'{self.user_name.data}'" if self.user_name.data != 'None' else 'null'
        file = f"'{self.file_name.data}'" if self.file_name.data != 'None' else 'null'

        query = f"select * from table(editors_search.find({file}, {user}))"

        result = db.execute(query)
        result = result.fetchall()
        if result:
            return result
        else:
            return 'Empty search table'
