from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField
from datetime import date
from wtforms import validators


class DateForm(Form):

    nick = StringField("username that read the news: ", [
        validators.Length(3, 15)
    ])

    new_id = IntegerField("id read news: ", [validators.optional()])

    date_read = DateField("read news date: ",
                          format='%d-%b-%y', default=date.today())

    submit = SubmitField("Save")