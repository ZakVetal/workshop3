from flask_wtf import Form
from wtforms import StringField,   SubmitField
from wtforms import validators


class UserForm(Form):

   

   user_locale = StringField("Locale: ",[
                                    validators.DataRequired("Please enter your locale."),
                                    validators.Length(5, 20, "Locale should be from 5 to 20 symbols")
                                 ])


 


   submit = SubmitField("Save")
