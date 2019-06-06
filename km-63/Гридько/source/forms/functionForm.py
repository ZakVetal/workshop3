from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class FormFunction(Form):



   functions = StringField("function: ",[
                                    validators.DataRequired("Please enter your function.")

                                 ])


   function_type = StringField("function type: ",[
                                 validators.DataRequired("Please enter your function type.")

                                 ])

   user_name_fk = StringField("user name: ", [
       validators.DataRequired("Please enter your name.")

   ])

   submit = SubmitField("Save")