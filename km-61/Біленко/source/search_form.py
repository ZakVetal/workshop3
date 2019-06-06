from flask_wtf import Form
from wtforms import StringField, SubmitField
from WorkShop3.dao.userhelper import UserHelper


class Search_User_Network_Form(Form):
    user_name = StringField('User"s name: ')
    network_name = StringField('Network"s name: ')
    submit = SubmitField('Search')

    def searched_result(self):
        helper = UserHelper()
        return helper.User_Name(self.user_name.data)
        return helper.Network_Name(self.network_name.data)
