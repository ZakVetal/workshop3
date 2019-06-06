from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper


class SearchForm(Form):

    first_name = StringField('First name: ')
    last_name = StringField('Last name: ')
    submit = SubmitField('Search')

    def get_result(self):
        helper = UserHelper()
        data = {
            'first_name': self.first_name.data,
            'last_name': self.last_name.data
        }
        return helper.getUserData(**data)
