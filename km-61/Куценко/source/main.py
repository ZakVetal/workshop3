from flask import Flask, render_template, request, redirect, url_for
from forms.search import SearchForm
from dao.model import *
from dao.db import OracleDb
from forms.form import UF
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

    result = db.sqlalchemy_session.query(User).all()

    return render_template('user.html', users = result)


@app.route('/date', methods=['GET'])
def date():

    db = OracleDb()

    result = db.sqlalchemy_session.query(date).all()

    return render_template('date.html', date = result)


@app.route('/userskill', methods=['GET'])
def place():

    db = OracleDb()

    result = db.sqlalchemy_session.query(User).join(date).join(place).all()

    return render_template('userskill.html', users = result)


@app.route('/search', methods=['GET', 'POST'])
def search():

    search_form = SearchForm()

    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None)
    else:
        return render_template('search.html', form = search_form, result=search_form.data_result())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    db = OracleDb()

    #
    #     SELECT
    #     User.user_name,
    #     count(place.place_name)
    #
    #
    #
    # FROM
    # date
    # LEFT
    # OUTER
    # JOIN
    # place
    # ON
    # date.user_id = place.user_id
    #
    # GROUP
    # BY
    # place.user_id, place.user_name
    #

    query1  = (
                db.sqlalchemy_session.query(
                                            User.user_name,
                                            func.count(place.place_name).label('place_name')
                                          ).\
                                    outerjoin(place).\
                                    group_by(User.user_id,User.user_name)
               ).all()

    # SELECT
    # user.user_name,
    # count(user.user_id)
    # user_count
    #
    # FROM
    # place
    # LEFT
    # OUTER
    # JOIN
    # user
    # ON
    # user.user_name = place.user_name
    #
    # GROUP
    # BY
    # user.user_name

    query2 = (
        db.sqlalchemy_session.query(
            user.user_name,
            func.count(place.palce_id).label('place_count')
        ). \
            outerjoin(place). \
            group_by(date.skill_name)
    ).all()




    names, skill_counts = zip(*query1)
    bar = go.Bar(
        x=names,
        y=skill_counts
    )

    skills, user_count = zip(*query2)
    pie = go.Pie(
        labels=skills,
        values=user_count
    )



    data = {
                "bar":[bar],
                "pie":[pie]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)

#     =================================================================================================


@app.route('/new_user', methods=['GET','POST'])
def new_user():

    form = UF()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            new_user= User(

                                user_birthday=form.user_birthday.data.strftime("%d-%b-%y"),
                                user_phone=form.user_phone.data,
                                user_name=form.user_name.data,

                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_user)
            db.sqlalchemy_session.commit()


            return redirect(url_for('user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")



@app.route('/edit_user', methods=['GET','POST'])
def edit_user():

    form = UF()


    if request.method == 'GET':

        user_id =request.args.get('user_id')
        db = OracleDb()
        user = db.sqlalchemy_session.query(User).filter(User.user_id == user_id).one()


        form.user_id.data = user.user_id
        form.user_name.data = user.user_name
        form.user_studybook.data =  user.user_studybook
        form.user_birthday.data = user.user_birthday
        form.user_email.data = user.user_email
        form.user_year.data = user.user_year

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()

            user = db.sqlalchemy_session.query(User).filter(User.user_id == form.user_id.data).one()

            # update fields from form data
            user.user_studybook = form.user_studybook.data
            user.user_birthday = form.user_birthday.data.strftime("%d-%b-%y")
            user.user_email = form.user_email.data
            user.user_name = form.user_name.data
            user.user_year = form.user_year.data.strftime("%d-%b-%y")

            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))





@app.route('/delete_user', methods=['POST'])
def delete_user():

    user_id = request.form['user_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(User).filter(User.user_id ==user_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return user_id

if __name__ == '__main__':
    app.run(debug=True)