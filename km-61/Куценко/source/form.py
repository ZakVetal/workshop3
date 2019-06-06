from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class UF(Form):

   user_id = HiddenField()

   user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   user_phone = StringField("PhoneNumber: ", [
       validators.DataRequired("Please enter your phone number."),
       validators.Length(9, 12, "Phone should be from 9 to 12 symbols")
   ])

   user_birthday = DateField("Birthday: ", [ validators.DataRequired("Please enter your birthday.")])

   submit = SubmitField("Save")