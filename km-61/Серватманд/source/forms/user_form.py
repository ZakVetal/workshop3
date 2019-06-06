from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class UserForm(Form):

   user_id = HiddenField()

   user_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])


   user_surname = StringField("surname: ",[
                                   validators.DataRequired("Please enter your surname."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

    Discipline_name =  StringField("Discipline: ",[
                                   validators.DataRequired("Please enter the name of Discipline."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

submit = SubmitField("Save")