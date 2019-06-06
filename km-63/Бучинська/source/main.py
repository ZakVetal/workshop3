from flask import Flask, request, render_template
from  dao.db import OracleDb
from dao.helper import UserHelper
from forms.form import userForm,searchForm
import json
#from sqlalchemy.sql import func
import cx_Oracle
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def main1():
    return render_template('index.html')



@app.route('/search', methods=['GET', 'POST'])
def search_f():
    search = searchForm()
    helper = UserHelper()
    if request.method == 'POST':
        if search.validate() == False:
            print(search.m1.errors)
            print(search.m2.errors)
            return render_template('search.html', form=search)
        else:
            Tbl = helper.search(

                search.m1.data,
                search.m2.data,

            )

            return "Our search {}".format(Tbl)
    return render_template('search.html',form=search, action='')


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = userForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.user_phone.errors)
            print(form.user_name.errors)
            print(form.user_surname.errors)
            print(form.user_gender.errors)
            return render_template('form.html', form=form)
        else:
            user_phone, status = helper.newUser(

                                            form.user_phone.data,
                                            form.user_name.data,form.user_surname.data, form.user_gender.data

            )

            return "Status {} ID {}".format(status,user_phone)


    return render_template('form.html', form=form, action='')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    db = OracleDb()


    cursor.execute('select SUBSC.channel_url, count(SUBSC.user_phone) FROM SUBSC group by SUBSC.channel_url ')
    rss = cursor.fetchall()
    x,y =[],[]
    for i,j in (rss):
        x.append(i)
        y.append(j)

    pie = go.Pie(
        labels=x,
        values=y
    )

    data = {
                "pie":[pie]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dash.html', graphsJSON=graphsJSON)

if __name__ == '__main__':
    app.run(debug=True)

