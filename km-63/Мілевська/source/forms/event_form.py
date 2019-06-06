from flask_wtf import Form
from wtforms import StringField, IntegerField, DateField
from wtforms import validators


class EventForm(Form):
    event_id = IntegerField()
    event_name = StringField(
        "Event name: ", [
            validators.DataRequired("Please enter event name."),
            validators.Length(3, 20, "Name should be from 3 to 20 symbols")
        ]
    )
    event_date = DateField(
        "Event date", [
            validators.DataRequired("Please enter event date."),
        ]
    )
