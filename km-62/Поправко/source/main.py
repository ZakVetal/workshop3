import flask import Flask, render_template
from dao.orm.model import *
from dao.db import OracleDb
from forms.user_form import UserForm
from sqlalchemy.sql import func

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import json

app = flask.Flask(__name__)

app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return flask.render_template('index.html')

@app.route('/user')
def user_page():
    db = OracleDb()
    result = db.sqlalchemy_session.query(User).all()
    return render_template('user.html', users=result)

@app.route('/history_of_views')
def view_page():
    db = OracleDb()
    result = db.sqlalchemy_session.query(User).join(News).join(History_of_views).all()
    return flask.render_template('history_of_views.html', history_of_views = result)

@app.route('/news')
def news_page():
    db = OracleDb()
    result = db.sqlalchemy_session.query(News).all()
    return flask.render_template('news.html', news = result)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    search_form = SearchForm()
    if request.method == 'GET':
        return render_template('search.html', form=search_form, result=None)
    else:
    return render_template('search.html', form=search_form, result=search_form.get_result())

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()

query1  = (
                db.sqlalchemy_session.query(
                                            User.user_name,
                                            func.count(userSkill.news_name).label('news_count')
                                          ).\
                                    outerjoin(userSkill).\
                                    group_by(User.user_id,User.user_name)
               ).all()

query2 = (
        db.sqlalchemy_session.query(
            ormSkill.news_name,
            func.count(userSkill.user_id).label('user_count')
        ). \
            outerjoin(userSkill). \
            group_by(ormSkill.news_name)
    ).all()

    names, news_counts = zip(*query1)
    bar = go.Bar(
        x=names,
        y=news_counts
    )

    news, user_count = zip(*query2)
    pie = go.Pie(
        labels=news,
        values=user_count
    )

    data = {
                "bar":[bar],
                "pie":[pie]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphsJSON=graphsJSON)

if __name__ == '__main__':
    app.run()
