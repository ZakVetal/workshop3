from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField
from wtforms import validators


class NewsForm(Form):
    new_id = HiddenField()

    news_name = StringField("Your news name: ", [
        validators.Length(1, 15)
    ])

    text = StringField("Your news item: ", [
        validators.Length(1, 10000)
    ])
    
    sourse = StringField("The name under which the news is published: ", [
        validators.Length(1, 30)
    ])

    submit = SubmitField("Save")