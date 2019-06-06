from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators


class ScheduleForm(Form):
    schedule_data = DateField()

    group_name = StringField("Name: ", [
        validators.DataRequired("Please enter your  group name."),
        validators.Length(0, 7, "Group name must be  include only 6 symbols")
    ])

    teacher_id = IntegerField("teacher id: ", [
        validators.DataRequired("Please enter your teacher id."),

    ])



    submit = SubmitField("Save")