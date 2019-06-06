from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class FormUser(Form):



   user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name.")

                                 ])


   role = StringField("Role: ",[
                                 validators.DataRequired("Please enter your name.")

                                 ])



   submit = SubmitField("Save")