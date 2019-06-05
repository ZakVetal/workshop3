from flask import Flask, render_template, request, redirect, url_for
from WorkShop3.forms.search_form import Search_User_Network_Form
from WorkShop3.forms.user_form import User_Form
from WorkShop3.dao.orm.model import *
from WorkShop3.dao.db import OracleDb
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

    result = db.sqlalchemy_session.query(orm_User_Name).all()

    return render_template('user.html', users=result)


@app.route('/network', methods=['GET'])
def network():
    db = OracleDb()

    result = db.sqlalchemy_session.query(orm_network).all()

    return render_template('network.html', networks=result)


@app.route('/user_network', methods=['GET'])
def user_use_network():
    db = OracleDb()

    result = db.sqlalchemy_session.query(orm_User_Name).join(orm_user_use_network).join(orm_network).all()

    return render_template('user_network.html', users=result)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = Search_User_Network_Form()

    if request.method == 'GET':
        return render_template('search.html', form=search_form, result=None)
    else:
        return render_template('search.html', form=search_form, result=search_form.searched_result())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()
#
#     SELECT
#     orm_User_Name.user_name,
#     count(orm_user_use_network.network_name)
#     skill_count
#
#
# FROM
# orm_User_Name
# LEFT
# OUTER
# JOIN
# orm_user_use_network
# ON
# orm_User_Name.user_id = orm_user_use_network.user_id
#
# GROUP
# BY
# orm_User_Name.user_id, orm_User_Name.user_name
#
# query1 = (
#     db.sqlalchemy_session.query(
#         orm_User_Name.user_name,
#         func.count(orm_user_use_network.network_name).label('network_count')
#     ). \
#         outerjoin(orm_user_use_network). \
#         group_by(orm_User_Name.user_id, orm_User_Name.user_name)
# ).all()
#
# SELECT
# orm_network.network_name,
# count(orm_user_use_network.user_id)
# user_count
#
# FROM
# orm_network
# LEFT
# OUTER
# JOIN
# orm_user_use_network
# ON
# orm_network.network_name = orm_user_use_network.network_name
#
# GROUP
# BY
# orm_network.network_name
#
# query2 = (
#     db.sqlalchemy_session.query(
#         orm_network.network_name,
#         func.count(orm_user_use_network.user_id).label('user_count')
#     ). \
#         outerjoin(orm_user_use_network). \
#         group_by(orm_network.network_name)
# ).all()
#
# names, skill_counts = zip(*query1)
# bar = go.Bar(
#     x=names,
#     y=skill_counts
# )
#
# skills, user_count = zip(*query2)
# pie = go.Pie(
#     labels=skills,
#     values=user_count
# )
#
# data = {
#     "bar": [bar],
#     "pie": [pie]
# }
# graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
#
# return render_template('dashboard.html', graphsJSON=graphsJSON)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = User_Form()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            new_user = orm_User_Name(
                user_name=form.user_name.data,
                user_email=form.user_email.data,
                user_birthday=form.user_birthday.data.strftime("%d-%b-%y"),
                credit_card=form.credit_card.data
            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_user)
            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")


@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    form = User_Form()

    if request.method == 'GET':

        user_id = request.args.get('user_id')
        db = OracleDb()
        user = db.sqlalchemy_session.query(orm_User_Name).filter(orm_User_Name.user_id == user_id).one()

        # fill form and send to user
        form.user_id.data = user.user_id
        form.user_name.data = user.user_name
        form.user_email.data = user.user_email
        form.user_birthday.data = user.user_birthday
        form.credit_card.data = user.credit_card

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(orm_User_Name).filter(orm_User_Name.user_id == form.user_id.data).one()

            # update fields from form data
            user.user_name = form.user_name.data
            user.user_email = form.user_email.data
            user.user_birthday = form.user_birthday.data.strftime("%d-%b-%y")
            user.credit_card = form.credit_card.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))


@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form['user_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(orm_User_Name).filter(orm_User_Name.user_id == user_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return user_id


if __name__ == '__main__':
    app.run(debug=True)
