from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from wtforms import validators, ValidationError


class UserForm(Form):


    email = StringField('Email: ',[validators.DataRequired('Please enter email.'),validators.Length(16, 16, "email only 16 symbols")])
    password = StringField('Password: ', [validators.DataRequired('Please enter your password.'),])
    submit = SubmitField('Submit')


class EventForm(Form):
    email = StringField('Email: ', [validators.DataRequired('Please enter email.'),validators.Length(16, 16, "email only 16 symbols")])
    name = StringField('Name event: ', [validators.DataRequired('Please enter name.')])
    data = DateField(' Data: ',[validators.DataRequired('Please enter date.')])
    time = StringField('Time: ', [validators.DataRequired('Please enter time.')])
    longitude = StringField('L: ', [validators.DataRequired('Please enter longitude.')])
    latitude = StringField('Name event: ', [validators.DataRequired('Please enter latitude.')])
    submit = SubmitField('Submit')

class CalendarForm(Form):
    date = StringField('Date_: ', [validators.DataRequired('Please enter date.')])
    email = StringField('Email: ', [validators.DataRequired('Please enter email.'),validators.Length(16, 16, "email only 16 symbols")])
    submit = SubmitField('Submit')

class searchForm(Form):
    min = StringField('min: ', [validators.DataRequired('Please enter min point.')])
    max = StringField('max: ', [validators.DataRequired('Please enter max point.')])
    submit = SubmitField('Submit')