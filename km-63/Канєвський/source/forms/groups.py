from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField
from wtforms import validators


class GroupForm(Form):

    group_name = StringField("Name: ", [
        validators.DataRequired("Please enter your  group name."),
        validators.Length(5,7, "Group name must be  include only 6 symbols")
    ])



    submit = SubmitField("Save")