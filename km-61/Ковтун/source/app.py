from flask import Flask, render_template, request, redirect, url_for
from Workshop.application.models.db import *
from Workshop.application.dao.credentials import *
from Workshop.application.services.helper import DBHelper
from Workshop.application.services.visualization import students_by_groups_bar_graph, students_by_names_pie_graph
import datetime
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = "application_key"

app.config["SQLALCHEMY_DATABASE_URI"] = f"oracle://{username}:{password}@{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/students")
def students():
    _students = Students().query.all()
    return render_template("students.html", students=_students)


@app.route("/student/<uuid>", methods=["GET", "POST"])
def student(uuid):
    current_student = Students.query.filter(Students.Id == uuid).first()
    form = current_student.get_wtf_form()

    if request.method == "POST":
        if not form.validate():
            return render_template('student.html', form=form)
        else:
            form.update_db_student(current_student)
            db.session.commit()
            return redirect(url_for("students"))

    return render_template('student.html', form=form)


@app.route("/student/new", methods=["GET", "POST"])
def new_student():
    form = StudentForm()

    if request.method == "POST":
        if not form.validate():
            return render_template('student.html', form=form)
        else:
            student = form.get_db_student()
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("students"))

    return render_template('student.html', form=form)


@app.route("/delete_student/<uuid>", methods=["POST"])
def delete_student(uuid):
    if request.method == "POST":
        current_student = Students.query.filter(Students.Id == uuid).first()
        db.session.delete(current_student)
        db.session.commit()
    return redirect(url_for("students"))


@app.route("/groups")
def groups():
    _groups = Groups().query.all()
    return render_template("groups.html", groups=_groups)


@app.route("/group/<uuid>", methods=["GET", "POST"])
def group(uuid):
    current_group = Groups.query.filter(Groups.Id == uuid).first()
    form = current_group.get_wtf_form()

    if request.method == "POST":
        if not form.validate():
            return render_template('group.html', form=form)
        else:
            form.update_db_group(current_group)
            db.session.commit()
            return redirect(url_for("groups"))

    return render_template('group.html', form=form)


@app.route("/group/new", methods=["GET", "POST"])
def new_group():
    form = GroupForm()

    if request.method == "POST":
        if not form.validate():
            return render_template('group.html', form=form)
        else:
            group = form.get_db_group()
            db.session.add(group)
            db.session.commit()
            return redirect(url_for("groups"))

    return render_template('group.html', form=form)


@app.route("/delete_group/<uuid>", methods=["POST"])
def delete_group(uuid):
    if request.method == "POST":
        current_group = Groups.query.filter(Groups.Id == uuid).first()
        db.session.delete(current_group)
        db.session.commit()
    return redirect(url_for("groups"))


@app.route("/studentsgroups")
def students_groups():
    _studentgroups = StudentGroup.query.join(Students).join(Groups).all()
    return render_template("studentsgroups.html", studentgroups=_studentgroups)


@app.route("/studentsgroups/<uuid>", methods=["GET", "POST"])
def student_group(uuid):
    studentgroup = StudentGroup.query.join(Students).join(Groups).filter(StudentGroup.Id == uuid).first()
    form = studentgroup.get_wtf_form()
    form.Student.choices = [(student.Id, f"{student.Firstname} {student.Lastname}") for student in Students.query.all()]
    form.Group.choices = [(group.Id, group.Title) for group in Groups.query.all()]

    if request.method == "POST":
        if not form.validate():
            render_template("studentgroup.html", form=form)
        else:
            form.update_db_student_group(studentgroup)
            db.session.commit()
            return redirect(url_for("students_groups"))
    return render_template("studentgroup.html", form=form)


@app.route("/studentgroup/new", methods=["GET", "POST"])
def new_student_group():
    form = StudentGroupForm()

    form.Student.choices = [(student.Id, f"{student.Firstname} {student.Lastname}") for student in Students.query.all()]
    form.Group.choices = [(group.Id, group.Title) for group in Groups.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template('studentgroup.html', form=form)
        else:
            student_group = form.get_db_student_group()
            db.session.add(student_group)
            db.session.commit()
            return redirect(url_for("students_groups"))

    return render_template('studentgroup.html', form=form)


@app.route("/delete_student_group/<uuid>", methods=["POST"])
def delete_student_group(uuid):
    if request.method == "POST":
        studentgroup = StudentGroup.query.join(Students).join(Groups).filter(StudentGroup.Id == uuid).first()
        db.session.delete(studentgroup)
        db.session.commit()
    return redirect(url_for("students_groups"))


@app.route("/students/search/advanced", methods=["GET", "POST"])
def students_advanced_search():
    form = StudentsAdvancedSearchForm()
    form.Group.choices += [(group.Title, group.Title) for group in Groups.query.all()]

    if request.method == "POST":
        if not form.validate():
            return render_template("students_advanced_search.html", form=form, students=[])
        else:
            students = form.get_requested_students()
            return render_template("students_advanced_search.html", form=form, students=students)

    return render_template("students_advanced_search.html", form=form, students=[])


@app.route("/dashboard", methods=["GET"])
def dashboard():
    group_division_data = students_by_groups_bar_graph()
    names_division_data = students_by_names_pie_graph()
    return render_template("dashboard.html", group_division_data=group_division_data,
                           names_division_data=names_division_data)
