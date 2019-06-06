from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    user_locale = StringField('User дщсфду: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getUserData(self.user_locale.data)
