from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError
from dao.db import OracleDb

class UserForm(Form):

    user_email = StringField("email: ", [
        validators.DataRequired("Please enter your  name."),
        validators.Length(6, 6, "Your name must be  include only 6 symbols")
    ])



    submit = SubmitField("Save")
