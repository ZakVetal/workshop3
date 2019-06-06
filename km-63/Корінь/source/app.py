import datetime
import json

from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import func
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from dao.db import OracleDb
from dao.orm.model import ormVariable, ormData, ormTest
from forms.dataForm import DataForm
from forms.searchForm import SearchForm
from forms.testForm import TestForm
from forms.varForm import VarForm
from itertools import groupby
from operator import itemgetter
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/all_variable', methods=['GET'])
def all_variable():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormVariable).all()
    print(result)
    return render_template('VariableAll.html', result = result)


@app.route('/variable', methods=['GET','POST'])
def variable():

    form = VarForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('variable.html', form=form, form_name="New variable", action="variable")
        else:
            new_var= ormVariable(

                                variable_name=form.variable.data,
                                variable_type=form.variable_type.data,

                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_var)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_variable'))

    return render_template('variable.html', form=form, form_name="New variable", action="variable")

@app.route('/delete_variable', methods=['GET'])
def delete_variable():
    variable_name = request.args.get('variable_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormVariable).filter(ormVariable.variable_name ==variable_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_variable'))


@app.route('/edit_variable', methods=['GET', 'POST'])
def edit_variable():
    form = VarForm()
    if request.method == 'GET':

        variable_name =request.args.get('variable_name')
        db = OracleDb()
        variables = db.sqlalchemy_session.query(ormVariable).filter(ormVariable.variable_name == variable_name).one()

        # fill form and send to user

        form.variable.data = variables.variable_name
        form.variable_type.data = variables.variable_type


        return render_template('variable.html', form=form, form_name="Edit variable", action="edit_variable")


    else:

        if form.validate() == False:
            return render_template('variable.html', form=form, form_name="Edit variable", action="edit_variable")
        else:
            db = OracleDb()
            # find user
            var = db.sqlalchemy_session.query(ormVariable).filter(ormVariable.variable_name == form.variable.data).one()
            print(var)

            # update fields from form data

            var.variable_name = form.variable.data
            var.variable_type = form.variable_type.data



            db.sqlalchemy_session.commit()

            return redirect(url_for('all_variable'))


@app.route('/all_data', methods=['GET'])
def all_data():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormData).all()
    print(result)
    return render_template('DataAll.html', result = result)


@app.route('/new_data', methods=['GET','POST'])
def new_data():

    form = DataForm()
    now = datetime.datetime.now()
    form.date.data = now
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('data.html', form=form, form_name="New Data", action="new_data")
        else:
            new_var= ormData(

                                data=now,
                                value=form.value.data,
                                variable_name_fk=form.variable_name_fk.data,
                                test_fk = form.test_name_fk.data

                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_var)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_data'))

    return render_template('data.html', form=form, form_name="New Data", action="new_data")

@app.route('/delete_data', methods=['GET'])
def delete_data():
    data_name = request.args.get('data_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormData).filter(ormData.data ==data_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_data'))


@app.route('/edit_data', methods=['GET', 'POST'])
def edit_data():
    form = DataForm()
    if request.method == 'GET':

        data_name =request.args.get('data_name')
        db = OracleDb()
        var = db.sqlalchemy_session.query(ormData).filter(ormData.data == data_name).one()

        # fill form and send to user

        form.date.data = var.data
        form.value.data = var.value
        form.variable_name_fk.data = var.variable_name_fk
        form.test_name_fk.data = var.test_fk


        return render_template('data.html', form=form, form_name="Edit data", action="edit_data")


    else:

        if form.validate() == False:
            return render_template('data.html', form=form, form_name="Edit data", action="edit_data")
        else:
            db = OracleDb()
            # find user
            var = db.sqlalchemy_session.query(ormVariable).filter(ormVariable.variable_name == form.variable.data).one()
            print(var)

            # update fields from form data

            var.data = form.date.data
            var.value = form.value.data
            var.variable_name_fk = form.variable_name_fk.data
            var.test_fk = form.test_name_fk.data



            db.sqlalchemy_session.commit()

            return redirect(url_for('all_data'))

@app.route('/all_test', methods=['GET'])
def all_test():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormTest).all()
    print(result)
    return render_template('TestAll.html', results = result)


@app.route('/new_test', methods=['GET','POST'])
def new_test():

    form = TestForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('test.html', form=form, form_name="New test", action="new_test")
        else:
            new_var= ormTest(

                                test_name=form.test.data,
                                result=form.result.data,

                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_var)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_test'))

    return render_template('test.html', form=form, form_name="New test", action="new_test")

@app.route('/delete_test', methods=['GET'])
def delete_test():
    test_name = request.args.get('test_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormTest).filter(ormTest.test_name ==test_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_test'))


@app.route('/edit_test', methods=['GET', 'POST'])
def edit_test():
    form = TestForm()
    if request.method == 'GET':

        test_name =request.args.get('test_name')
        db = OracleDb()
        test = db.sqlalchemy_session.query(ormTest).filter(ormTest.test_name == test_name).one()

        # fill form and send to user

        form.test.data = test.test_name
        form.result.data = test.result


        return render_template('test.html', form=form, form_name="Edit test", action="edit_test")


    else:

        if form.validate() == False:
            return render_template('test.html', form=form, form_name="Edit test", action="edit_test")
        else:
            db = OracleDb()
            # find user
            tests = db.sqlalchemy_session.query(ormTest).filter(ormTest.test_name == form.test.data).one()


            # update fields from form data

            tests.test_name = form.test.data
            tests.result = form.result.data



            db.sqlalchemy_session.commit()

            return redirect(url_for('all_test'))


@app.route('/search', methods=['GET', 'POST'])
def search():

    search_form = SearchForm()

    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None, action ='search',name = 'Variable' )
    else:
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Name()
                               , action ='search',name = 'Variable')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()
    query1 = (
        db.sqlalchemy_session.query(
            func.count(ormVariable.variable_name),
            ormVariable.variable_type.label('type')
        ).group_by(ormVariable.variable_type)
    ).all()
    print(query1)

    # query2 = (
    #     db.sqlalchemy_session.query(
    #         func.count(ormData.data),
    #         ormTest.test_name.label('name')
    #     ).join(ormTest).group_by(ormTest.test_name)
    # ).all()

    query2 = (db.sqlalchemy_session.query(ormData.data, func.count(ormTest.test_name)).join(ormTest).group_by(
        ormData.data)).all()
    query2 = [(y[0].strftime('%Y-%m-%d'), y[1]) for y in query2]
    query2 = [(x, sum(map(itemgetter(1), y))) for x, y in groupby(query2, itemgetter(0))]
    variable, counts = zip(*query2)
    bar = go.Bar(
        x=counts,
        y=variable
    )

    skills, user_count = zip(*query1)
    pie = go.Pie(
        labels=user_count,
        values=skills
    )
    print(variable, counts)
    print(skills, user_count)


    data = {
                "bar":[bar],
                "pie":[pie]
           }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)



if __name__ == '__main__':
    app.run(debug=True, port = 5050)