from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import func, text

from dao.db import OracleDb
from dao.orm.model import ormUser, ormFunction, ormFunctionVariable
from dao.orm.userhelper import UserHelper
from forms.formUser import FormUser
from forms.functionForm import FormFunction
from forms.searchForm import SearchForm

from forms.variableForm import VariableForm

app = Flask(__name__)
app.secret_key = 'development key'
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import json




@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()
    query1 = (
        db.sqlalchemy_session.query(
            func.count(ormUser.user_name),
            ormUser.role.label('role')
        ). \
            group_by(ormUser.role)
    ).all()

    stmt = text('''select count(names) as namess,counts as countss
                            from
                            (select orm_function.function_name as names,count(orm_variable.variable_name) as counts
                            from  orm_function 
                            inner join orm_variable 
                            on orm_function.function_name = orm_variable.function_name_fk
                            group by orm_function.function_name)
                            group by counts''')

    query = (db.sqlalchemy_session.query("namess", "countss"). \
             from_statement(stmt)
             ).all()

    variable, counts = zip(*query)
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

@app.route('/all_user', methods=['GET'])
def all_user():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).all()
    print(result)
    return render_template('all_user.html', result = result)

@app.route('/new_user', methods=['GET','POST'])
def new_user():

    form = FormUser()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            new_user= ormUser(

                                user_name=form.user_name.data,
                                role=form.role.data
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_user)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    form = FormUser()
    if request.method == 'GET':

        user_name =request.args.get('user_name')
        db = OracleDb()
        user = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_name == user_name).one()

        # fill form and send to user

        form.user_name.data = user.user_name
        form.role.data = user.role

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")


    else:

        if form.validate() == False:
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_name == form.user_name.data).one()

            # update fields from form data

            user.role = form.role.data
            user.user_name = form.user_name.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('all_user'))


@app.route('/delete_user', methods=['GET'])
def delete_user():
    user_name = request.args.get('user_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormUser).filter(ormUser.user_name ==user_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_user'))

@app.route('/searchByUser', methods=['GET', 'POST'])
def searchByUser():

    search_form = SearchForm()

    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None, action ='searchByUser',name = 'User' )
    else:
        print(search_form.get_result_by_Name())
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Name()
                               , action ='searchByUser',name = 'User')

@app.route('/searchByFunction', methods=['GET', 'POST'])
def searchByFunction():

    search_form = SearchForm()

    if request.method=='GET':
        search_form.user_name.label='Function name:'
        return render_template('search.html', form = search_form, result=None , action ='searchByFunction',name = 'Function')
    else:
        search_form.user_name.label = 'Function name:'
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Function()
                               , action ='searchByFunction',name = 'Function')

@app.route('/new_function', methods=['GET','POST'])
def new_function():

    form = FormFunction()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('function_form.html', form=form, form_name="New function", action="new_function")
        else:
            new_functions= ormFunction(

                                function_name=form.functions.data,
                                function_type=form.function_type.data,
                                user_name_fk = form.user_name_fk.data
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_functions)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_function'))

    return render_template('function_form.html', form=form, form_name="New function", action="new_function")

@app.route('/all_function', methods=['GET'])
def all_function():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormFunction).all()
    print(result)
    return render_template('all_function.html', result = result)

@app.route('/delete_function', methods=['GET'])
def delete_function():
    function_name = request.args.get('function_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormFunction).filter(ormFunction.function_name ==function_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_function'))

@app.route('/edit_function', methods=['GET', 'POST'])
def edit_function():
    form = FormFunction()
    if request.method == 'GET':

        function_name =request.args.get('function_name')
        db = OracleDb()
        functions = db.sqlalchemy_session.query(ormFunction).filter(ormFunction.function_name == function_name).one()

        # fill form and send to user

        form.functions.data = functions.function_name
        form.function_type.data = functions.function_type
        form.user_name_fk.data = functions.user_name_fk


        return render_template('function_form.html', form=form, form_name="Edit function", action="edit_function")


    else:

        if form.validate() == False:
            return render_template('function_form.html', form=form, form_name="Edit function", action="edit_function")
        else:
            db = OracleDb()
            # find user
            func = db.sqlalchemy_session.query(ormFunction).filter(ormFunction.function_name == form.functions.data).one()

            # update fields from form data

            func.function_name = form.functions.data
            func.function_type = form.function_type.data
            func.user_name_fk = form.user_name_fk.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('all_function'))

@app.route('/all_variable', methods=['GET'])
def all_variable():

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormFunctionVariable).all()
    print(result)
    return render_template('all_variable.html', result = result)


@app.route('/new_variable', methods=['GET','POST'])
def new_variable():

    form = VariableForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('variable.html', form=form, form_name="New variable", action="new_variable")
        else:
            new_var= ormFunctionVariable(

                                variable_name=form.variable.data,
                                type_variable=form.variable_type.data,
                                function_name_fk = form.function_name_fk.data
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_var)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_variable'))

    return render_template('variable.html', form=form, form_name="New variable", action="new_variable")

@app.route('/delete_variable', methods=['GET'])
def delete_variable():
    variable_name = request.args.get('variable_name')
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormFunctionVariable).filter(ormFunctionVariable.variable_name ==variable_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return redirect(url_for('all_variable'))


@app.route('/edit_variable', methods=['GET', 'POST'])
def edit_variable():
    form = VariableForm()
    if request.method == 'GET':

        variable_name =request.args.get('variable_name')
        db = OracleDb()
        variables = db.sqlalchemy_session.query(ormFunctionVariable).filter(ormFunctionVariable.variable_name == variable_name).one()

        # fill form and send to user

        form.variable.data = variables.variable_name
        form.variable_type.data = variables.type_variable
        form.function_name_fk.data = variables.function_name_fk


        return render_template('variable.html', form=form, form_name="Edit variable", action="edit_variable")


    else:

        if form.validate() == False:
            return render_template('variable.html', form=form, form_name="Edit variable", action="edit_variable")
        else:
            db = OracleDb()
            # find user
            var = db.sqlalchemy_session.query(ormFunctionVariable).filter(ormFunctionVariable.variable_name == form.variable.data).one()

            # update fields from form data

            var.variable_name = form.variable.data
            var.type_variable = form.variable_type.data
            var.function_name_fk = form.function_name_fk.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('all_variable'))
if __name__ == '__main__':
    app.run(debug=True, port = 5050)
