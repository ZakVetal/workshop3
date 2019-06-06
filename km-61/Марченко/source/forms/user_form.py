from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class UserForm(Form):

   user_id = HiddenField()

   user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])


   user_password = StringField("password: ",[
                                   validators.DataRequired("Please enter your password."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

    complaint_txt =  StringField("Complaint: ",[
                                   validators.DataRequired("Please enter the text of your complaint."),
                                   validators.Length(3, 300, "")
                                 ])

submit = SubmitField("Save")