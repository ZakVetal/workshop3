from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class WorkerForm(Form):

   worker_name = StringField("Name: ",[
                                    validators.DataRequired("Enter a name."),
                                    validators.Length(1, 30, "Name should be from 1 to 30 symbols")
                                 ])

   worker_surname = StringField("Surname: ", [
       validators.DataRequired("Enter a surname."),
       validators.Length(1, 30, "Surname should be from 1 to 30 symbols")
   ])

   worker_patronymic = StringField("Patronymic: ", [
       validators.Length(0, 30, "Patronymic should be from 1 to 30 symbols")
   ])

   worker_birth_date = DateField("Birth date: ",[
       validators.DataRequired("Enter birth date.")
    ])

   worker_job_title = StringField("Job title: ", [
       validators.DataRequired("Enter job title."),
       validators.Length(1, 30, "Job title should be from 1 to 30 symbols")
   ])


   submit = SubmitField("Save")