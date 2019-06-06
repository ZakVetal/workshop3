from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    user_name = StringField('Username: ')
    user_password = StringField('Password: ')
    complaint_txt = StringField('Write your complaint: ')
    submit = SubmitField('Search')

    def get_result(self):
        helper = UserHelper()
        return helper.getMessageData(self.text_mes.data)
        return helper.complaint_txt(self.complaint_txt.data)
        return helper.user_name(self.user_name.data)
        return helper.user_password(self.user_password.data)