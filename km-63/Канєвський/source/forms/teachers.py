from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class TeacherForm(Form):

   teacher_id = HiddenField()

   teacher_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])


   teacher_surname = StringField("surname: ",[
                                 validators.DataRequired("Please enter your surname."),
                                 validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   teacher_patronymict = StringField("patronymict: ",[
                                    validators.DataRequired("Please enter your patronymict."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   teacher_birthday = DateField("Birthday: ", [ validators.DataRequired("Please enter your birthday.")])




   submit = SubmitField("Save")
