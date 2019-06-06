from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class VariableForm(Form):



   variable = StringField("variable: ",[
                                    validators.DataRequired("Please enter your function.")

                                 ])


   variable_type = StringField("variable type: ",[
                                 validators.DataRequired("Please enter your function type.")

                                 ])

   function_name_fk = StringField("function name: ", [
       validators.DataRequired("Please enter your name.")

   ])

   submit = SubmitField("Save")