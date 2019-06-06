from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    user_name = StringField('Name: ')
    user_surname = StringField('Username: ')
    discipline_name = StringField('Discipline: ')
    submit = SubmitField('Search')

    def get_result(self):
        helper = UserHelper()
        return helper.getMessageData(self.text_mes.data)
        return helper.discipline_name(self.discipline_name.data)
        return helper.user_name(self.user_name.data)
        return helper.user_surname(self.user_name.data)