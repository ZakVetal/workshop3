from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from wtforms import validators, ValidationError
import re

def myvalidate(form,field):
    if re.fullmatch(r'0[0-9]{12}',field.data):
        raise ValidationError('Field must be included number')

class userForm(Form):



    user_phone = StringField('user_phone: ',[validators.DataRequired('Please enter user_p.'),myvalidate,validators.Length(13,message="Wrong format for phone")])
    user_name = StringField('user_name: ', [validators.DataRequired('Please enter user_name.'),validators.Length(13,message="Wrong format for name")])
    user_surname = StringField('user_surname: ',[validators.DataRequired('Please enter user_surname.')])
    user_gender = StringField('user_gen: ', [validators.DataRequired('Please enter user_gen.')])



    submit = SubmitField('Submit')


class channelForm(Form):
     channel_url= StringField('channel_url: ', [validators.DataRequired('Please enter channel_url.'),validators.URL(message="Wrong format of URL")])
     channel_name = StringField('channel_url: ', [validators.DataRequired('Please enter channel_url.')])
     submit = SubmitField('Submit')


class subcsForm(Form):
    channel_url = StringField('channel_url: ', [validators.DataRequired('Please enter channel_url.'),validators.URL(message="Wrong format of URL")])
    user_phone = StringField('user_phone: ', [validators.DataRequired('Please enter user_p.'),myvalidate,validators.Length(13,message="Wrong format for phone")])
    subsc_date = StringField('subsc_date: ', [validators.DataRequired('Please enter subsc_date.')])


    submit = SubmitField('Submit')

class searchForm(Form):
    m1 = StringField('m1: ', [validators.DataRequired('Please enter channel_url.')])
    m2 = StringField('m2: ', [validators.DataRequired('Please enter user_p.')])
    submit = SubmitField('Submit')
