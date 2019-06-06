from flask_wtf import Form
from wtforms import StringField, SubmitField
from dao.db import OracleDb

class SearchForm(Form):
    nick = StringField()
    news_name = StringField()
    date_read =  StringField('form:DD-MMM-YYYY :')
    submit = SubmitField('Search')

 def search(self):
        db = OracleDb()

        nick = f"'{self.news_name.data}'" if selfnews_name.data != 'None' else 'null'
        name = f"'{self.nick.data}'" if self.nick.data != 'None' else 'null'

        query = f"select * from table(search.find({nick}, {name}))"

        result = db.execute(query)
        result = result.fetchall()
        if result:
            return result
        else:
            return 'search table'