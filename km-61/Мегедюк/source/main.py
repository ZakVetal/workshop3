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







@app.route('/photoplace', methods=['GET'])
def photoplace():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).all()

    return render_template('photoplace.html', photoplaces = result)


@app.route('/localename', methods=['GET'])
def localename():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).join(ormLocaleplaces.join(ormUser).all()

    return render_template('localename.html', localenames = result)


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


    # SELECT
    #     ormUser.user_locale,
    #     count(ormPlaces.user_locale) user_count

    # FROM ormUser LEFT OUTER JOIN ormPlaces
    #   ON  ormUser.user_locale = ormPlaces.user_locale

    # GROUP BY ormUser.user_locale,ormUser.places_date


    query1  = (
                db.sqlalchemy_session.query(
                                            ormUser.places_date,
                                            func.count(ormPlaces.user_locale).label('user_count')
                                          ).\
                                    outerjoin(ormPlaces).\
                                    group_by(ormUser.user_locale,ormUser.places_date)
               ).all()




    # SELECT
    #     ormUser.user_locale,
    #     count(ormPlaces.places_date) user_count

    # FROM ormUser LEFT OUTER JOIN ormPlaces
    #   ON  ormUsersuser_locale = ormPlaces.user_locale

    # GROUP BY ormUser.user_locale

    query2 = (
        db.sqlalchemy_session.query(
           ormUser.user_locale,
            func.count(ormPlaces.places_date).label('user_count')
        ). \
            outerjoin(ormPlaces). \
            group_by( ormUser.user_locale)
    ).all()




    date, photo_counts = zip(*query1)
    bar = go.Bar(
        x=date,
        y=photo_counts
    )

    date, user_count = zip(*query2)
    pie = go.Pie(
        labels=date,
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

    form = UserForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            new_user= ormUser(
                                user_locale=form.user_locale.data,
                               
            db = OracleDb()
            db.sqlalchemy_session.add(new_user)
            db.sqlalchemy_session.commit()


            return redirect(url_for('user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")



@app.route('/edit_user', methods=['GET','POST'])
def edit_user():

    form = UserForm()


    if request.method == 'GET':

        user_id =request.args.get('places_date')
        db = OracleDb()
        user = db.sqlalchemy_session.query(ormUser).filter(ormUser.places_date == places_date).one()

        # fill form and send to user
        form.places_date.data = user.places_date
        form.user_locale.data = user.user_locale
        

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(ormUser).filter(ormUser.places_date == form.places_date.data).one()

            # update fields from form data
            user.user_locale = form.user_locale.data
          

            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))





@app.route('/delete_user', methods=['POST'])
def delete_user():

   places_date = request.form['user_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).filter(ormUser.places_date ==places_date).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return places_date

if __name__ == '__main__':
    app.run(debug=True)
