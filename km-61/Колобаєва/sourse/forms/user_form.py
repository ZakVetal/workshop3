from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class UserForm(Form):


 user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   user_email = StringField("Email: ",[validators.DataRequired("Please enter your Email."),
                                 validators.Email("Wrong email format")
                                 ])

   user_phone = DateField("Phone: ", [ validators.DataRequired("Please enter your phone.")
                                   validators.Length(10, "Phone should be 10 symbols")
                                 ])


   submit = SubmitField("Save")
