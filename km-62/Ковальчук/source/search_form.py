from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    patch_file = StringField('path fail: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getDocumentData(self.patch_file.data)