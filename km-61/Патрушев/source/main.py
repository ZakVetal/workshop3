from flask import Flask, flash, render_template, request, redirect, url_for
import sqlalchemy.sql as sql
from forms.search_form import SearchForm
from dao.orm.entities import *
from dao.db import OracleDb
from forms.file_form import FileForm
from forms.user_form import UserForm
import json
import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    db = OracleDb()

    query1 = (
        db.sqlalchemy_session.query(
            OrmFile.file_date,
            sql.func.count(OrmFile.file_id).label('file_count')
        ).group_by(OrmFile.file_date).order_by(OrmFile.file_date)
    ).all()

    query2 = (
        db.sqlalchemy_session.query(
            OrmUser.user_id,
            OrmUser.user_name,
            sql.func.count(OrmFile.file_id).label('owns_count_files')
        ).outerjoin(OrmFile).group_by(OrmUser.user_id, OrmUser.user_name)
    ).all()

    date, file_count = zip(*query1)
    bar = go.Scatter(
        x=date,
        y=file_count
    )

    user_id, name, own_files_count = zip(*query2)
    pie = go.Pie(
        labels=[f'id={id}, name={name}' for id, name in zip(user_id, name)],
        values=own_files_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }

    json_data = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', json=json_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    db = OracleDb()
    search_form = SearchForm()
    user_names = db.sqlalchemy_session.query(OrmUser.user_name).all()
    file_names = db.sqlalchemy_session.query(OrmFile.file_name).all()

    if request.method == 'GET':
        return render_template('search.html', form=search_form, result=None, users=user_names, files=file_names)
    else:
        search_form.user_name.data = request.form.get('user_name')
        search_form.file_name.data = request.form.get('file_name')
        return render_template('search.html', form=search_form, result=search_form.search(), users=user_names,
                               files=file_names)


# FILE ORIENTED QUERIES -----------------------------------------------------------------------------------------------


@app.route('/file', methods=['GET'])
def index_file():
    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmFile).all()
    for element in result:
        if element.file_owner_id:
            user = db.sqlalchemy_session.query(OrmUser).filter(OrmUser.user_id == element.file_owner_id).one()
            element.file_owner_name = user.user_name

    return render_template('file.html', files=result)


@app.route('/new_file', methods=['GET', 'POST'])
def new_file():
    form = FileForm()
    db = OracleDb()
    users = db.sqlalchemy_session.query(OrmUser).all()
    if request.method == 'POST':
        if not form.validate():
            return render_template('file_form.html', form=form, form_name="New file", action="new_file")
        else:
            if request.form.get('owner_select') != 'None':
                owner_id = [user.user_id for user in users if user.user_name == request.form.get('owner_select')][0]
            else:
                owner_id = sql.null()

            file_obj = OrmFile(
                file_name=form.file_name.data,
                file_type=form.file_type.data,
                file_context=form.file_context.data,
                file_owner_id=owner_id,
                file_date=form.file_date.data.strftime("%d-%b-%y")
            )

            db = OracleDb()
            db.sqlalchemy_session.add(file_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('index_file'))

    return render_template('file_form.html', form=form, form_name="New file", action="new_file", users=users)


@app.route('/edit_file', methods=['GET', 'POST'])
def edit_file():
    form = FileForm()

    if request.method == 'GET':

        file_id = request.args.get('file_id')
        db = OracleDb()
        file = db.sqlalchemy_session.query(OrmFile).filter(OrmFile.file_id == file_id).one()

        # fill form and send to user
        form.file_id.data = file.file_id
        form.file_name.data = file.file_name
        form.file_type.data = file.file_type
        form.file_context.data = file.file_context
        form.file_owner.data = file.file_owner_id
        form.file_date.data = file.file_date

        return render_template('file_form.html', form=form, form_name="Edit file", action="edit_file")

    else:

        if not form.validate():
            return render_template('file_form.html', form=form, form_name="Edit file", action="edit_file")
        else:
            db = OracleDb()
            # find user
            file = db.sqlalchemy_session.query(OrmFile).filter(OrmFile.file_id == form.file_id.data).one()

            # update fields from form data

            file.file_id = form.file_id.data
            file.file_name = form.file_name.data
            file.file_type = form.file_type.data
            file.file_context = form.file_context.data
            file.file_owner_id = form.file_owner.data
            file.file_date = form.file_date.data.strftime("%d-%b-%y")

            db.sqlalchemy_session.commit()

            return redirect(url_for('index_file'))


@app.route('/delete_file')
def delete_file():
    file_id = request.args.get('file_id')

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmFile).filter(OrmFile.file_id == file_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('index_file'))


# END FILE ORIENTED QUERIES -------------------------------------------------------------------------------------------

# USER ORIENTED QUERIES -----------------------------------------------------------------------------------------------


@app.route('/user', methods=['GET'])
def index_user():
    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmUser).all()

    return render_template('user.html', users=result)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = UserForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('user_form.html', form=form, form_name="New user", action="new_user")
        else:
            user_obj = OrmUser(
                user_name=form.user_name.data,
                user_login=form.user_login.data
            )
            db = OracleDb()
            db.sqlalchemy_session.add(user_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('index_user'))

    return render_template('user_form.html', form=form, form_name="New user", action="new_user")


@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    form = UserForm()

    if request.method == 'GET':

        user_id = request.args.get('user_id')
        db = OracleDb()
        user = db.sqlalchemy_session.query(OrmUser).filter(OrmUser.user_id == user_id).one()

        # fill form and send to user
        form.user_name.data = user.user_name
        form.user_login.data = user.user_login

        return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")

    else:

        if not form.validate():
            return render_template('user_form.html', form=form, form_name="Edit user", action="edit_user")
        else:
            db = OracleDb()
            # find user
            user = db.sqlalchemy_session.query(OrmUser).filter(OrmUser.user_id == form.user_id.data).one()

            # update fields from form data

            user.user_id = form.user_id.data
            user.user_name = form.user_name.data
            user.user_login = form.user_login.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('index_user'))


@app.route('/delete_user')
def delete_user():
    user_id = request.args.get('user_id')

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmUser).filter(OrmUser.user_id == user_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('index_user'))


# END USER ORIENTED QUERIES -------------------------------------------------------------------------------------------

# EDITOR FILES ORIENTED QUERIES ---------------------------------------------------------------------------------------

@app.route('/file_editors', methods=['GET'])
def index_edit_files():
    db = OracleDb()

    users = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).all()

    return render_template('editor_files.html', users=users)


@app.route('/new_editor_file', methods=['GET', 'POST'])
def new_editor_file():
    db = OracleDb()

    if request.method == 'POST':

        user_id = int(request.form.get('user_id'))
        file_id = int(request.form.get('file_id'))

        join_users = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).all()
        exist = []

        for user in join_users:
            for file in user.orm_editor:
                exist.append((user.user_id, file.file_id))

        if (user_id, file_id) not in exist:
            editor_obj = OrmFileEditor(
                user_id=user_id,
                file_id=file_id
            )
            db = OracleDb()
            db.sqlalchemy_session.add(editor_obj)
            db.sqlalchemy_session.commit()
        else:
            flash("already have this row", 'error')

        return redirect(url_for('index_edit_files'))

    users = db.sqlalchemy_session.query(OrmUser).all()
    files = db.sqlalchemy_session.query(OrmFile).all()

    return render_template('editor_file_form.html', users=users, files=files, form_name="New editor",
                           action="new_editor_file")


@app.route('/edit_editor_file', methods=['GET', 'POST'])
def edit_editor_file():
    db = OracleDb()
    if request.method == 'GET':

        user_id = request.args.get('user_id')
        file_id = request.args.get('file_id')
        join_users = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).filter(
            OrmFile.file_id == file_id, OrmUser.user_id == user_id).one()

        # fill form and send to user
        users = db.sqlalchemy_session.query(OrmUser).all()
        files = db.sqlalchemy_session.query(OrmFile).all()

        return render_template('editor_file_form.html', form_name="Edit editor", action="edit_editor_file", users=users,
                               files=files,
                               data=join_users)

    else:

        user_id = int(request.form.get('user_id'))
        file_id = int(request.form.get('file_id'))

        old_user_id = int(request.args.get('user_id'))
        old_file_id = int(request.args.get('file_id'))

        join_users = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).all()
        exist = []

        for user in join_users:
            for file in user.orm_editor:
                exist.append((user.user_id, file.file_id))

        if (user_id, file_id) not in exist:
            join_users = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).filter(
                OrmFile.file_id == old_file_id, OrmUser.user_id == old_user_id).one()

            join_users.user_id = user_id
            join_users.file_id = file_id

            db.sqlalchemy_session.commit()
        else:
            flash("already have this row (db dont change)", 'error')

        return redirect(url_for('index_edit_files'))


@app.route('/delete_editor_file')
def delete_editor():
    user_id = request.args.get('user_id')
    file_id = request.args.get('file_id')

    db = OracleDb()

    result = db.sqlalchemy_session.query(OrmUser).join(OrmFileEditor).join(OrmFile).filter(
        OrmFile.file_id == file_id, OrmUser.user_id == user_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('index_edit_files'))


# END EDITOR FILES ORIENTED QUERIES -----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
