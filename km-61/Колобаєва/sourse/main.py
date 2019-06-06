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

    return render_template('index.html', users = result)


@app.route('/skill', methods=['GET'])
def message():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormMessage).all()

    return render_template('message.html', message = result)


@app.route('/board', methods=['GET'])
def board():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).join(ormBoard).join(ormMessage).all()

    return render_template('board.html', board = result)


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
                                            ormUser.user_phone,
                                            func.count(ormBoard.add_time).label('message_count')
                                          ).\
                                    outerjoin(ormBoard).\
                                    group_by(ormUser.user_phone,ormMessage.time_send)
               ).all()


    query2 = (
        db.sqlalchemy_session.query(
            ormMessage.time_send,
            func.count(ormBoard.add_time).label('message_count')
        ). \
            outerjoin(ormBoar). \
            group_by(ormMessage.time_send)
    ).all()



    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)

#     =================================================================================================

@app.route('/edit_user', methods=['GET','POST'])
def edit_user():

    form = UserForm()


    if request.method == 'GET':

        user_id =request.args.get('user_id')
        db = OracleDb()
        user = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_id == user_id).one()

        form.user_phone.data =  user.user_phone
        form.user_name.data = user.user_name
        form.user_email.data = user.user_email
        

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_id == form.user_id.data).one()

            # update fields from form data
            user_phone.data =  user.user_phone
            user_name.data = user.user_name
            user_email.data = user.user_email

            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))





@app.route('/delete_user', methods=['POST'])
def delete_user():

    user_phone = request.form['user_phone']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_phone ==user_phone).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return user_phone

if __name__ == '__main__':
    app.run(debug=True)
