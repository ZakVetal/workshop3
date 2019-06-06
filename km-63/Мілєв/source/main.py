if __name__ == "__main__":
    #TODO 
from flask import Flask, request, render_template
from  dao.db import OracleDb
from dao.helper import UserHelper
from forms.form import userForm,searchForm
import json
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
            print(search.user_name.errors)
            print(search.improvement_name.errors)
            return render_template('search.html', form=search)
        else:
            Tbl = helper.search(

                search.user_name.data,
                search.improvement_name.data,

            )

            return "Our search {}".format(Tbl)
    return render_template('search.html',form=search, action='')


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = userForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.user_name.errors)
            print(form.user_id.errors)
            return render_template('form.html', form=form)
        else:
            user_id, status = helper.newUser(

                                            form.user_id.data,
                                            form.user_name.data

            )

            return "Status {} ID {}".format(status,user_id)


    return render_template('form.html', form=form, action='')


@app.route('/dashboard', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)