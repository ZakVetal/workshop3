from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    group_name = StringField('Group name')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getUsername(self.group_name.data)
