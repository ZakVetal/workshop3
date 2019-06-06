from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField
from datetime import date
from wtforms import validators


class FileForm(Form):
    file_id = HiddenField()

    file_name = StringField("File name: ", [
        validators.DataRequired("Please enter file name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    file_type = StringField("Type: ", [
        validators.DataRequired("Please enter file type."),
        validators.Length(3, 6, "Type should be from 3 to 6 symbols")
    ])

    file_context = StringField("Context: ", [
        validators.Length(0, 40, "Context should be from 0 to 40 symbols")])

    file_owner = IntegerField("Owner: ", [validators.optional()])

    file_date = DateField("Create date: ", [validators.DataRequired("Please enter your file create date.")],
                          format='%d-%b-%y', default=date.today())

    submit = SubmitField("Save")
