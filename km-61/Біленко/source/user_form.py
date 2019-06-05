from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField
from wtforms import validators


class User_Form(Form):
    user_id = HiddenField()

    user_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")
    ])

    user_email = StringField("Email: ", [
        validators.DataRequired("Please enter your Email."),
        validators.Email("Wrong email format -- test@test.com")
    ])

    user_birthday = DateField("Birthday: ", [validators.DataRequired("Please enter your birthday.")])

    credit_card = StringField("Credit Card: ", [
        validators.DataRequired("Please enter your credit card."),
        validators.Length(16, 16, "Credit card consists 16 numbers")
    ])

    network_name = StringField("Social network: ", [
        validators.DataRequired("Please enter your social network, which used."),
        validators.Length(2, 20, "Write shorter name of network")
    ])

    submit = SubmitField("Save")
