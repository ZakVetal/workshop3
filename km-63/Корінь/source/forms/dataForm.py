from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class DataForm(Form):



   date = StringField("Date: " )


   value = StringField("Value: ",[
                                 validators.DataRequired("Please enter your function type.")

                                 ])
   variable_name_fk = StringField("variable name: ", [
       validators.DataRequired("Please enter your function type.")

   ])
   test_name_fk = StringField("test name: ", [
       validators.DataRequired("Please enter your function type.")

   ])

   submit = SubmitField("Save")