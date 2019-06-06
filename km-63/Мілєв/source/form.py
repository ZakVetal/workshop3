from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from wtforms import validators, ValidationError
import re


class userForm(Form):



    user_id = StringField('user_id: ',[validators.DataRequired('Please enter user_id.'),validators.Length(11,message="Wrong format for id")])
    user_name = StringField('user_name: ', [validators.DataRequired('Please enter user_name.'),validators.Length(13,message="Wrong format for name")])
    user_birthday = StringField('user_birthday: ',[validators.DataRequired('Please enter user_birthday.')])



    submit = SubmitField('Submit')


class improvementForm(Form):
     improvement_name = StringField('improvement_name: ', [validators.DataRequired('Please enter improvement_name.'),validators.Length(20,message="Wrong format for name")])
     improvement_id = StringField('improvement_id: ', [validators.DataRequired('Please enter improvement_id.')])
     submit = SubmitField('Submit')


class subcsForm(Form):
    improvement_name = StringField('improvement_name: ', [validators.DataRequired('Please enter improvement_name.'),validators.Length(20,message="Wrong format for name")])
    improvement_id = StringField('improvement_id: ', [validators.DataRequired('Please enter improvement_id.')])
    improvement_priority = StringField('improvement_priority: ', [validators.DataRequired('Please enter improvement_priority.')])


    submit = SubmitField('Submit')

class searchForm(Form):
    user_name = StringField('user_name: ', [validators.DataRequired('Please enter user_name.')])
    improvement_name = StringField('improvement_name: ', [validators.DataRequired('Please enter improvement_name.')])
    submit = SubmitField('Submit')