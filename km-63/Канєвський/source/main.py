import datetime

from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import func, text

from dao.db import OracleDb
from dao.orm.model import ormTeacher, ormGroup, ormSchedule
from sqlalchemy.sql import func
from forms.groups import GroupForm
from forms.teachers import TeacherForm
from forms.schedules import ScheduleForm
from forms.searchForm import SearchForm


app = Flask(__name__)
app.secret_key = 'development key'
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import json




@app.route('/', methods=['GET', 'POST'])
def root():

    return render_template('index.html')






@app.route('/search', methods=['GET', 'POST'])
def search():

    search_form = SearchForm()

    if request.method=='GET':
        return render_template('search.html', form = search_form, result=None)
    else:
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Group())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    db = OracleDb()


    # SELECT
    #     ormUser.user_name,
    #     count(ormUserSkill.skill_name) skill_count

    # FROM ormUser LEFT OUTER JOIN ormUserSkill
    #   ON  ormUser.user_id = ormUserSkill.user_id

    # GROUP BY ormUser.user_id,ormUser.user_name

    query1 = (
        db.sqlalchemy_session.query(
            ormSchedule.group_name,
            func.count(ormSchedule.group_name).label('skill_count')
        ). \
 \
            group_by(ormSchedule.group_name)
    ).all()
    print(query1)




    # SELECT
    #     ormSkill.skill_name,
    #     count(ormUserSkill.user_id) user_count

    # FROM ormSkill LEFT OUTER JOIN ormUserSkill
    #   ON  ormSkill.skill_name = ormUserSkill.skill_name

    # GROUP BY ormSkill.skill_name

    query2 = (
        db.sqlalchemy_session.query(
            ormSchedule.group_name,
            func.count(ormSchedule.group_name).label('skill_count')
        ). \
 \
            group_by(ormSchedule.group_name)
    ).all()
    print(query1)
    print(query2)


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


@app.route('/new_teacher', methods=['GET','POST'])
def new_teacher():

    form = TeacherForm()


    if request.method == 'POST':
        if form.validate() == False:
            return render_template('teacher.html', form=form, form_name="New teacher", action="new_teacher")
        else:
            new_teacher= ormTeacher(
                                teacher_id=form.teacher_id.data,
                                teacher_name=form.teacher_name.data,
                                teacher_surname=form.teacher_surname.data,
                                teacher_birthday=form.teacher_birthday.data.strftime("%d-%b-%y"),
                                teacher_patronymict=form.teacher_patronymict.data,

                            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_teacher)
            db.sqlalchemy_session.commit()


            return redirect(url_for('all_teacher'))

    return render_template('teacher_form.html', form=form, form_name="New teacher", action="new_teacher")



@app.route('/edit_teacher', methods=['GET','POST'])
def edit_teacher():

    form = TeacherForm()


    if request.method == 'GET':

        teacher_id =request.args.get('teacher_id')
        db = OracleDb()
        teacher = db.sqlalchemy_session.query(ormTeacher).filter(ormTeacher.teacher_id == teacher_id).one()

        # fill form and send to teacher
        form.teacher_id.data=teacher.teacher_id
        form.teacher_name.data=teacher.teacher_name
        form.teacher_surname.data=teacher.teacher_surname
        form.teacher_birthday.data=teacher.teacher_birthday
        form.teacher_patronymict.data=teacher.teacher_patronymict


        return render_template('teacher_form.html', form=form, form_name="Edit teacher", action="edit_teacher")


    else:

        if form.validate() == False:
            return render_template('teacher_form.html', form=form, form_name="Edit teacher", action="edit_teacher")
        else:
            db = OracleDb()
            # find teacher
            teacher = db.sqlalchemy_session.query(ormTeacher).filter(ormTeacher.teacher_id == form.teacher_id.data).one()

            # update fields from form data
            teacher.teacher_id = form.teacher_id.data
            teacher.teacher_name = form.teacher_name.data
            teacher.teacher_surname = form.teacher_surname.data
            teacher.teacher_birthday = form.teacher_birthday.data.strftime("%d-%b-%y")
            teacher.teacher_patronymict = form.teacher_patronymict.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('all_teacher'))





@app.route('/delete_teacher', methods=['POST'])
def delete_teacher():

    teacher_id = request.form['teacher_id']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormTeacher).filter(ormTeacher.teacher_id ==teacher_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()


    return teacher_id

@app.route('/new_group', methods=['GET','POST'])
def new_group():
    form = GroupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('group.html', form=form, form_name="New group", action="new_group")
        else:
            new_group = ormGroup(
                group_name=form.group_name.data,

            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_group)
            db.sqlalchemy_session.commit()

            return redirect(url_for('all_group'))

    return render_template('group.html', form=form, form_name="New group", action="new_group")


@app.route('/edit_group', methods=['GET', 'POST'])
def edit_group():
    form = GroupForm()

    if request.method == 'GET':

        group_name = request.args.get('group_name')
        db = OracleDb()
        group = db.sqlalchemy_session.query(ormGroup).filter(ormGroup.group_name == group_name).one()

        # fill form and send to group

        form.group_name.data = group.group_name


        return render_template('group.html', form=form, form_name="Edit group", action="edit_group")


    else:

        if form.validate() == False:
            return render_template('group.html', form=form, form_name="Edit group", action="edit_group")
        else:
            db = OracleDb()
            # find teacher
            group = db.sqlalchemy_session.query(ormGroup).filter(ormGroup.group_name == form.group_name.data).one()

            # update fields from form data

            group.group_name = form.group_name.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('all_group'))


@app.route('/delete_group', methods=['POST'])
def delete_group():
    group_name = request.form['group_name']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormGroup).filter(ormGroup.group_name == group_name).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return group_name

@app.route('/new_schedule', methods=['GET','POST'])
def new_schedule():
    form = ScheduleForm()
    now = datetime.datetime.now()
    form.schedule_data.data = now
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('schedule_form.html', form=form, form_name="New schedule", action="new_schedule")
        else:
            new_schedule = ormSchedule(
                schedule_data=form.schedule_data.data,
                group_name=form.group_name.data,
                teacher_id=form.teacher_id.data


            )
            db = OracleDb()
            db.sqlalchemy_session.add(new_schedule)
            db.sqlalchemy_session.commit()

            return redirect(url_for('all_schedule'))

    return render_template('schedule_form.html', form=form, form_name="New schedule", action="new_schedule")


@app.route('/edit_schedule', methods=['GET', 'POST'])
def edit_schedule():
    form = ScheduleForm()

    if request.method == 'GET':
        schedule_data = request.args.get('schedule_data')
        db = OracleDb()
        schedules = db.sqlalchemy_session.query(ormSchedule).filter(ormSchedule.schedule_data == schedule_data).one()

        # fill form and send to user

        form.schedule_data.data = schedules.schedule_data
        form.group_name.data = schedules.group_name
        form.teacher_id.data = schedules.teacher_id

        return render_template('schedule_form.html', form=form, form_name="Edit schedule", action="edit_schedule")

    else:

        if form.validate() == False:
            return render_template('schedule_form.html', form=form, form_name="Edit schedule", action="edit_schedule")
        else:
            db = OracleDb()
            # find user
            sched = db.sqlalchemy_session.query(ormSchedule).filter(ormSchedule.schedule_data == form.schedule_data.data).one()

            # update fields from form data

            sched.schedule_data = form.schedule_data.data
            sched.group_name = form.group_name.data
            sched.teacher_id = form.teacher_id.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('schedule'))


@app.route('/delete_schedule', methods=['POST'])
def delete_schedule():
    schedule_data = request.form['schedule_data']

    db = OracleDb()

    result = db.sqlalchemy_session.query(ormSchedule).filter(ormSchedule.schedule_data == schedule_data).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return schedule_data

@app.route('/searchTeacher', methods=['GET', 'POST'])

def searchSchedule():

     search_form = SearchForm()

     if request.method=='GET':
        search_form.schedule_data.label='schedule data:'
        return render_template('search.html', form = search_form, result=None , action ='searchSchedule',name = 'Schedule')
     else:
        search_form.schedule_data.label = 'schedule data:'
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Schedule()
                               , action ='searchSchedule',name = 'Schedule')
@app.route('/searchGroup', methods=['GET', 'POST'])
def searchGroup():

     search_form = SearchForm()

     if request.method=='GET':
        search_form.group_name.label='Group name:'
        return render_template('search.html', form = search_form, result=None , action ='searchGroup',name = 'Group')
     else:
        search_form.group_name.label = 'Group name:'
        return render_template('search.html', form = search_form, result=search_form.get_result_by_Group(), action ='searchGroup',name = 'Group')

@app.route('/all_teacher', methods=['GET'])
def all_teacher():
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormTeacher).all()


    print(result)
    return render_template('all_teacher.html', result=result)

@app.route('/all_group', methods=['GET'])
def all_group():
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormGroup).all()


    print(result)
    return render_template('all_group.html', result=result)

@app.route('/all_schedule', methods=['GET'])
def all_schedule():
    db = OracleDb()

    result = db.sqlalchemy_session.query(ormSchedule).all()


    print(result)
    return render_template('all_schedule.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)