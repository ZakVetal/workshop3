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


@app.route('/Document', methods=['GET'])
def Document():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormDocument).all()

    return render_template('Document.html', Documents = result)


@app.route('/userDocument', methods=['GET'])
def userDocument():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).join(ormUserDocument).join(ormDocument).all()

    return render_template('userDocument.html', users = result)


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
    #     ormUser.full_name,
    #     count(ormUserDocument.patch_file) Document_count

    # FROM ormUser LEFT OUTER JOIN ormUserDocument
    #   ON  ormUser.email = ormUserDocument.email

    # GROUP BY ormUser.email,ormUser.full_name


    query1  = (
                db.sqlalchemy_session.query(
                                            ormUser.full_name,
                                            func.count(ormUserDocument.patch_file).label('Document_count')
                                          ).\
                                    outerjoin(ormUserDocument).\
                                    group_by(ormUser.email,ormUser.full_name)
               ).all()




    # SELECT
    #     ormDocument.patch_file,
    #     count(ormUserDocument.email) user_count

    # FROM ormDocument LEFT OUTER JOIN ormUserDocument
    #   ON  ormDocument.patch_file = ormUserDocument.patch_file

    # GROUP BY ormDocument.patch_file

    query2 = (
        db.sqlalchemy_session.query(
            ormDocument.patch_file,
            func.count(ormUserDocument.email).label('user_count')
        ). \
            outerjoin(ormUserDocument). \
            group_by(ormDocument.patch_file)
    ).all()




    names, Document_counts = zip(*query1)
    bar = go.Bar(
        x=names,
        y=Document_counts
    )

    Documents, user_count = zip(*query2)
    pie = go.Pie(
        labels=Documents,
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
        if form.valemailate() == False:
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            new_user= ormUser(
                                id=form.id.data,
                                full_name=form.full_name.data,
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_user)
            db.sqlalchemy_session.commit()


            return redirect(url_for('user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")



@app.route('/edit_user', methods=['GET','POST'])
def edit_user():

    form = UserForm()


    if request.method == 'GET':

        email =request.args.get('email')
        db = OracleDb()
        user = db.sqlalchemy_session.query(ormUser).filter(ormUser.email == email).one()

        # fill form and send to user
        form.email.data = user.email
        form.full_name.data = user.full_name
        form.id.data = user.id

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.valemailate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(ormUser).filter(ormUser.email == form.email.data).one()

            # update fields from form data
            user.id = form.id.data
            user.full_name = form.full_name.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('user'))





@app.route('/delete_user', methods=['POST'])
def delete_user():

    email = request.form['email']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).filter(ormUser.email ==email).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return email

if __name__ == '__main__':
    app.run(debug=True)
