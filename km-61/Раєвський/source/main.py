from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from dao.orm.model import *
from dao.credentials import *
from dao.db import OracleDb
from forms.worker_form import *
from forms.assignment_form import *
from forms.search_form import *


Base = declarative_base()


oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username=username,
        password=password,
        hostname=host,
        port=port,
        database=service,
    )
)

Session = sessionmaker(bind=engine)
session = Session()


#eugen_worker = OrmWorker('Eugen', 'R', 'V', '12-11-1920', 'Cleaner')


#session.add_all([eugen_worker])
#session.commit()


app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def root():

    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():

    search_form = SearchForm()

    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None)
    else:
        return render_template('search.html', form = search_form, result=search_form.get_result())


@app.route('/worker', methods=['GET'])
def worker():

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmWorker).all()
    return render_template('worker.html', workers = result)


@app.route('/assignment', methods=['GET'])
def assignment():

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmAssignment).all()

    return render_template('assignment.html', assignments = result)


@app.route('/worker_assignment', methods=['GET'])
def worker_assignment():

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmWorker).join(OrmWorkerAssignment).join(OrmAssignment).all()

    return render_template('worker_assignment.html', users = result)


@app.route('/new_worker', methods=['GET','POST'])
def new_worker():

    form = WorkerForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('worker_form.html', form=form, form_name="New worker", action="new_worker")
        else:
            new_worker = OrmWorker(
                worker_name=form.worker_name.data,
                worker_surname=form.worker_surname.data,
                worker_patronymic=form.worker_patronymic.data,
                worker_birth_date=form.worker_birth_date.data.strftime("%d-%m-%y"),
                worker_job_title=form.worker_job_title.data
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_worker)
            db.sqlalchemy_session.commit()


            return redirect('/worker')

    return render_template('worker_form.html', form=form, form_name="New worker", action="Worker")



@app.route('/edit_worker', methods=['GET','POST'])
def edit_worker():

    form = WorkerForm()


    if request.method == 'GET':

        worker_id =request.args.get('worker_id')
        db = OracleDb()
        worker = db.sqlalchemy_session.query(OrmWorker).filter(OrmWorker.worker_id == worker_id).one()

        # fill form and send to user
        form.worker_name.data = worker.worker_name
        form.worker_surname.data = worker.worker_surname
        form.worker_patronymic.data = worker.worker_patronymic
        form.worker_birth_date.data = worker.worker_birth_date
        form.worker_job_title.data = worker.worker_job_title

        return render_template('worker_form.html', form=form, form_name="Edit worker", action="edit_worker?worker_id=" + request.args.get('worker_id'))


    else:
        if form.validate() == False:
            return render_template('worker_form.html', form=form, form_name="Edit worker", action="edit_worker?worker_id=" + request.args.get('worker_id'))
        else:
            db = OracleDb()
            # find user
            worker = db.sqlalchemy_session.query(OrmWorker).filter(OrmWorker.worker_id == request.args.get('worker_id')).one()

            # update fields from form data
            worker.worker_name = form.worker_name.data
            worker.worker_surname = form.worker_surname.data
            worker.worker_patronymic = form.worker_patronymic.data
            worker.worker_birth_date = form.worker_birth_date.data.strftime("%d-%m-%y")
            worker.worker_job_title = form.worker_job_title.data

            db.sqlalchemy_session.commit()

            return redirect('/worker')


@app.route('/delete_worker', methods=['POST'])
def delete_worker():

    worker_id = request.form['worker_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmWorker).filter(OrmWorker.worker_id==worker_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return worker_id


@app.route('/new_assignment', methods=['GET','POST'])
def new_assignment():

    form = AssignmentForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('assignment_form.html', form=form, form_name="New assignment", action="new_assignment")
        else:
            new_assignment = OrmAssignment(
                assignment_name=form.assignment_name.data,
                assignment_description=form.assignment_description.data,
                assignment_time=form.assignment_time.data.strftime("%d-%m-%y")
                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_assignment)
            db.sqlalchemy_session.commit()


            return redirect('/assignment')

    return render_template('assignment_form.html', form=form, form_name="New assignment", action="new_assignment")



@app.route('/edit_assignment', methods=['GET','POST'])
def edit_assignment():

    form = AssignmentForm()


    if request.method == 'GET':

        assignment_id =request.args.get('assignment_id')
        db = OracleDb()
        assignment = db.sqlalchemy_session.query(OrmAssignment).filter(OrmAssignment.assignment_id == assignment_id).one()

        # fill form and send to user
        form.assignment_name.data = assignment.assignment_name
        form.assignment_description.data = assignment.assignment_description
        form.assignment_time.data = assignment.assignment_time

        return render_template('assignment_form.html', form=form, form_name="Edit assignment", action="edit_assignment?assignment_id=" + request.args.get('assignment_id'))


    else:
        if form.validate() == False:
            return render_template('assignment_form.html', form=form, form_name="Edit assignment", action="edit_assignment?assignment_id=" + request.args.get('assignment_id'))
        else:
            db = OracleDb()
            # find user
            assignment = db.sqlalchemy_session.query(OrmAssignment).filter(OrmAssignment.assignment_id == request.args.get('assignment_id')).one()

            # update fields from form data
            assignment.assignment_name = form.assignment_name.data
            assignment.assignment_description = form.assignment_description.data
            assignment.assignment_time = form.assignment_time.data.strftime("%d-%m-%y")

            db.sqlalchemy_session.commit()

            return redirect('/assignment')


@app.route('/delete_assignment', methods=['POST'])
def delete_assignment():
    print(request.form['assignment_id'])
    assignment_id = request.form['assignment_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmAssignment).filter(OrmAssignment.assignment_id==assignment_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return assignment_id


if __name__ == '__main__':
    app.run(debug=True)