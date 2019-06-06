from flask import Flask, request, render_template
from  dao.db import OracleDb
from dao.helper import UserHelper
from forms.all_forms import StudentForm,searchForm,ModulesForm,LearningForm
import json
import cx_Oracle
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def main_index():
    return render_template('index.html')




@app.route('/search', methods=['GET', 'POST'])
def search_f():
    search = searchForm()
    helper = UserHelper()
    if request.method == 'POST':
        if search.validate() == False:
            print(search.min.errors)
            print(search.max.errors)
            print(search.daybook.errors)
            print(search.daterep.errors)

            return render_template('search.html', form=search)
        else:
            Tbl = helper.Finding(

                search.min.data,
                search.max.data,
                search.daybook.data,
                search.daterep.data,

            )

            return "Our search {}".format(Tbl)
    return render_template('search.html',form=search, action='')


@app.route('/student', methods=['GET', 'POST'])
def student():
    form = StudentForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.student_daybook.errors)
            print(form.student_name.errors)
            print(form.student_birth.errors)
            print(form.student_contract.errors)
            return render_template('student.html', form=form)
        else:
            status = helper.createStudent(

                                            form.student_daybook.data,
                                            form.student_name.data,form.student_birth.data, form.student_contract.data

            )

            return "Status {} ID {}".format(status)

            status = helper.updateStudent(

                                            form.student_daybook.data,
                                            form.student_name.data,form.student_birth.data, form.student_contract.data

            )

            return "Status {} ID {}".format(status)

            status = helper.dropStudent(

                                            form.student_daybook.data,


            )

            return "Status {} ID {}".format(status)


    return render_template('student.html', form=form, action='')


@app.route('/dashboard/<z>', methods=['GET', 'POST'])
def dashboard(z):

    db = OracleDb()

    connection = cx_Oracle.connect('system', 'buts', 'localhost:1521/xe')
    cursor = connection.cursor()

    cursor.execute('select learning.date_reporting, learning.number FROM learning where  learning.number_of_daybook = ' + str(z) )
    rss = cursor.fetchall()
    x,y =[],[]
    for i,j in (rss):
        x.append(i)
        y.append(j)

    pie = go.Plot(
        labels=x,
        values=y
    )
    cursor.execute('select learning.module_name, avg(learning.point) group by learning.module_name  ')
    query2 = cursor.fetchall()
    x, y = [], []
    for i,j in (rss):
        x.append(i)
        y.append(j)
        bar = go.Bar(
            labels=x,
            values=y
        )
    data = {
                "bar":[bar],
        "plot":[plot]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dash.html', graphsJSON=graphsJSON)

@app.route('/module', methods=['GET', 'POST'])
def Module():
    form = ModulesForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.module_name.errors)
            print(form.teacher.errors)
            return render_template('module.html', form=form)
        else:
            status = helper.createModule(

                                            form.module_name.data,
                                            form.user_name.teacher,
            )

            return "Status {} ID {}".format(status,module_name)

            status = helper.dropModule(

                form.module_name.data
            )

            return "Status {} ID {}".format(status)
        status = helper.updateModule(

            form.module_name.data,
            form.user_name.teacher,
        )

        return "Status {} ID {}".format(status)

    return render_template('module.html', form=form, action='')

@app.route('/learning', methods=['GET', 'POST'])
def learning():
    form = LearningForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.module_name_.errors)
            print(form.student_daybook_.errors)
            print(form.reporting.errors)
            print(form.point.errors)
            return render_template('learning.html', form=form)
        else:
            status = helper.createlearning(

                                            form.module_name_.data,
                                            form.student_daybook_.data,form.reporting.data, form.point.data

            )

            return "Status {} ID {} {}".format(status)




    return render_template('learning.html', form=form, action='')


if __name__ == '__main__':
    app.run(debug=True)

