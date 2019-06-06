from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class TestForm(Form):



   test = StringField("Test name: ",[
                                    validators.DataRequired("Please enter your name.")

                                 ])


   result = StringField("Result: ",[
                                 validators.DataRequired("Please enter your result.")

                                 ])


   submit = SubmitField("Save")