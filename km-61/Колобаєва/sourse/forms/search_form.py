from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    user_phone = StringField('User phone: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getMessageData(self.text_mes.data)
