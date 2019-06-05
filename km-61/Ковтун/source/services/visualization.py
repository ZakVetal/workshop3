import plotly
import plotly.graph_objs as go
import json
from Workshop.application.models.db import *


def students_by_groups_bar_graph():
    data = db.session.query(Groups.Id, Groups.Title, db.func.count(Students.Id).label("Students quantity")).join(
        StudentGroup, Groups.Id == StudentGroup.GroupId).join(Students, StudentGroup.StudentId == Students.Id).group_by(
        Groups.Id, Groups.Title).all()

    groups = []
    student_quantity_by_groups = []

    for value in data:
        groups.append(value[1])
        student_quantity_by_groups.append(value[2])

    data = [
        go.Bar(
            x=groups,
            y=student_quantity_by_groups
        )
    ]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


def students_by_names_pie_graph():
    data = db.session.query(Students.Firstname, db.func.count(Students.Id).label("Quantity")).group_by(
        Students.Firstname).all()

    student_name = []
    names_quantity = []

    for value in data:
        student_name.append(value[0])
        names_quantity.append(value[1])

    data = [
        go.Pie(
            labels=student_name,
            values=names_quantity
        )
    ]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
