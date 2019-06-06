from flask_wtf import Form
from wtforms import StringField, SubmitField

from dao.orm.userhelper import UserHelper


class SearchForm(Form):
    user_name = StringField('User name: ')
    submit = SubmitField('Search')

    def get_result_by_Name(self):
        helper = UserHelper()
        return helper.getVariable(self.user_name.data)
    def get_result_by_Function(self):
        helper = UserHelper()
        return helper.getVariables(self.user_name.data)