from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UH

class SearchForm(Form):

    name = StringField('name: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UH()
        return helper.getData(self.name.data)