from flask import Flask, render_template, request, redirect, url_for
from forms.search_form import SearchForm
from dao.orm.model import *
from dao.db import OracleDb
from forms.user_form import UserForm
from sqlalchemy.sql import func

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import json

app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')
@app.route('/user', methods=['GET'])
def user():
    db = OracleDb()
    result = db.sqlalchemy_session.query(ormUser).all()
    return render_template('user.html', users = result)
@app.route('/calendar', methods=['GET'])
def calendar():
    db = OracleDb()
    result = db.sqlalchemy_session.query(ormCalendar).all()
    return render_template('calendar.html', calendars = result)
@app.route('/event', methods=['GET'])
def event():
    db = OracleDb()
    result = db.sqlalchemy_session.query(ormEvent).join(ormCalendar).join(ormUser).all()
    return render_template('event.html', users = result)
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None)
    else:
        return render_template('search.html', form = search_form, result=search_form.get_result())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    db = OracleDb()
    query1  = (
                db.sqlalchemy_session.query(
                                            ormUser.user_name,
                                            func.count(ormEvent.name).label('events')
                                          ).\
                                    outerjoin(ormEvent).\
                                    group_by(ormUser.email,ormUser.password)
               ).all()
    query2 = (
        db.sqlalchemy_session.query(
            ormEvent.name,
            func.count(ormUser.email).label('count_email')
        ). \
            outerjoin(ormUser). \
            group_by(ormEvent.name)
    ).all()

    name, email = zip(*query1)

    bar = go.Bar(
        x=name,
        y=email
    )

    name, count_email = zip(*query2)
    pie = go.Pie(
        labels=name,
        values=count_email
    )



    data = {
                "bar":[bar],
                "pie":[pie]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)