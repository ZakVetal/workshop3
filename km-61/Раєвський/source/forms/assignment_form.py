from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class AssignmentForm(Form):

    assignment_name = StringField("Name: ",[
                                    validators.DataRequired("Enter assignment name."),
                                    validators.Length(1, 30, "Name should be from 1 to 30 symbols")
                                 ])

    assignment_description = StringField("Description: ", [
       validators.DataRequired("Enter a description."),
       validators.Length(1, 2000, "Description should be from 1 to 2000 symbols")
    ])

    assignment_time = DateField("Deadline: ", [
       validators.DataRequired("Enter deadline.")
    ])

    submit = SubmitField("Save")