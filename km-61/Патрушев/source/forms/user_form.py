from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField
from wtforms import validators


class UserForm(Form):
    user_id = HiddenField()

    user_name = StringField("User name: ", [
        validators.Length(3, 40, "Name should be from 3 to 40 symbols")
    ])

    user_login = StringField("Login: ", [
        validators.DataRequired("Please enter file type."),
        validators.Length(3, 20, "Type should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")
