from flask_wtf import Form
from wtforms import StringField, ValidationError, IntegerField
from wtforms import validators


class UserForm(Form):
    user_id = IntegerField()
    user_email = StringField(
        "Email: ", [
            validators.DataRequired("Please enter your email."),
            validators.Email("Wrong email format")
        ]
    )
    user_name = StringField(
        "Username: ", [
            validators.DataRequired("Please enter your username."),
            validators.Length(3, 20, "Name should be from 3 to 20 symbols")
        ]
    )
    user_first_name = StringField(
        "First name: ", [
            validators.DataRequired("Please enter your first name."),
            validators.Length(3, 20, "Name should be from 3 to 20 symbols")
        ]
    )
    user_last_name = StringField(
        "First name: ", [
            validators.DataRequired("Please enter your last name."),
            validators.Length(3, 20, "Name should be from 3 to 20 symbols")
        ]
    )

    # submit = SubmitField("Save")


