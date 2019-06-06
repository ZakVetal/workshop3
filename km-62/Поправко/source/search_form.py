from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError
from dao.db import OracleDb
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    news_name = StringField('News name: ')
    submit = SubmitField("Search")
    def get_result(self):
        helper = UserHelper()
        return helper.getSkillData(self.news_name.data)