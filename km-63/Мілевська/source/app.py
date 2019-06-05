from flask import Flask, render_template, request, jsonify
from sqlalchemy.sql import func

from dao.db import OracleDb
from dao.orm.model import ormUser, ormEvent, ormUserAttendedEvent
from forms.event_form import EventForm
from forms.search_form import SearchForm
from forms.user_form import UserForm
from flask_wtf.csrf import CSRFProtect
import json
import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'z^_fs6oh+rbel1qu_ne^7^6-_dtj(8916t*)#%hbgufx&ads4)'
csrf = CSRFProtect(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/users')
def users():
    db = OracleDb()
    queryset = db.sqlalchemy_session.query(ormUser).all()
    return render_template('users.html', users=queryset)


if __name__ == '__main__':

    app.run()


@app.route('/user_edit', methods=['POST', ])
def user_edit():
    form = UserForm(request.form)
    data = form.data
    token = data.pop('csrf_token', None)
    if request.method == 'POST' and form.validate():
        db = OracleDb()
        user_id = data.pop('user_id', None)
        if user_id:
            db.sqlalchemy_session.query(ormUser).filter_by(user_id=user_id).update(data)
            print(ormUser())
        else:
            new_user = ormUser(**data)
            db.sqlalchemy_session.add(new_user)
        db.sqlalchemy_session.commit()
        return jsonify({'successed': True})
    else:
        form_errors = {}
        errors = {}
        for key, value in form.errors.items():
            errors[key] = ' '.join(value)
        form_errors['errors'] = errors
        return jsonify(form_errors)


@app.route('/del_user', methods=['POST', ])
def del_user():
    data = dict(request.form)
    if request.method == 'POST':
        db = OracleDb()
        db.sqlalchemy_session.query(ormUser).filter_by(user_id=data.get('user_id', None)).delete()
        db.sqlalchemy_session.commit()
    return jsonify({'success': True})


# EVENTS
@app.route('/events')
def events():
    db = OracleDb()
    queryset = db.sqlalchemy_session.query(ormEvent).all()
    return render_template('events.html', events=queryset)


@app.route('/event_edit', methods=['POST', ])
def event_edit():
    form = EventForm(request.form)
    data = form.data
    token = data.pop('csrf_token', None)
    if request.method == 'POST' and form.validate():
        db = OracleDb()
        event_id = data.pop('event_id', None)
        if event_id:
            db.sqlalchemy_session.query(ormEvent).filter_by(event_id=event_id).update(data)
        else:
            new_user = ormEvent(**data)
            db.sqlalchemy_session.add(new_user)
        db.sqlalchemy_session.commit()
        return jsonify({'successed': True})
    else:
        form_errors = {}
        errors = {}
        for key, value in form.errors.items():
            errors[key] = ' '.join(value)
        form_errors['errors'] = errors
        return jsonify(form_errors)


@app.route('/del_event', methods=['POST', ])
def del_event():
    data = dict(request.form)
    if request.method == 'POST':
        db = OracleDb()
        db.sqlalchemy_session.query(ormEvent).filter_by(event_id=data.get('event_id', None)).delete()
        db.sqlalchemy_session.commit()
    return jsonify({'success': True})


@app.route('/attendance', methods=['GET', ])
def attendance():
    db = OracleDb()
    queryset = db.sqlalchemy_session.\
        query(ormEvent).\
        join(ormUserAttendedEvent).\
        join(ormUser).\
        all()
    user_list = db.sqlalchemy_session.query(ormUser).all()
    event_list = db.sqlalchemy_session.query(ormEvent).all()
    return render_template(
        'attendance.html',
        attendances=queryset,
        users=user_list,
        events=event_list
    )


@app.route('/add_user_to_event', methods=['POST', ])
def add_user_to_event():
    data = dict(request.form)
    if request.method == 'POST':
        db = OracleDb()
        try:
            event = db.sqlalchemy_session.query(ormEvent).get(data.get('event_id'))
            user = db.sqlalchemy_session.query(ormUser).get(data.get('user_id'))
            event.orm_users.append(user)
            db.sqlalchemy_session.commit()
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'error': e.args[0]})
    else:
        return jsonify({'error': 'Error. Bad request'})


@app.route('/del_user_from_event', methods=['POST', ])
def del_user_from_event():
    data = dict(request.form)
    if request.method == 'POST':
        db = OracleDb()
        db.sqlalchemy_session.query(ormUserAttendedEvent).\
            filter_by(user_id=data.get('user_id', None), event_id=data.get('event_id', None)).\
            delete()
        db.sqlalchemy_session.commit()
    return jsonify({'success': True})


@app.route('/search', methods=['GET', 'POST'])
def search():

    search_form = SearchForm()

    if request.method == 'GET':
        return render_template('search.html', form=search_form, result=None)
    else:
        return render_template('search.html', form=search_form, result=search_form.get_result())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()

    # First
    first_query = (
        db.sqlalchemy_session.query(
            ormEvent.event_name,
            func.count(ormUserAttendedEvent.user_id).label('user_count')
        ).join(ormUser).group_by(ormEvent.event_name, ormEvent.event_id)
    ).all()

    events, user_count = zip(*first_query)
    pie = go.Pie(
        labels=events,
        values=user_count,
    )

    # Second
    second_query = (
        db.sqlalchemy_session.query(
            ormEvent.event_date,
            func.count(ormEvent.event_id).label('events_count')
        ).group_by(ormEvent.event_date)
    ).all()

    dates, events_count = zip(*second_query)
    bar = go.Bar(
        x=dates,
        y=events_count
    )

    data = {
        'bar': [bar],
        'pie': [pie]
    }

    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphsJSON=graphsJSON)
