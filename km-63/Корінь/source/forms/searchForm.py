from flask_wtf import Form
from wtforms import StringField, SubmitField

from dao.orm.userhelper import UserHelper


class SearchForm(Form):
    variable_name = StringField('variable_ name: ')
    submit = SubmitField('Search')

    def get_result_by_Name(self):
        helper = UserHelper()
        return helper.getTestCount(self.variable_name.data)
