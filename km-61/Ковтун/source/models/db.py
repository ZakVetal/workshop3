from flask_sqlalchemy import SQLAlchemy
from Workshop.application.models.forms import *

db = SQLAlchemy()


class Groups(db.Model):
    __tablename__ = "groups"

    Id = db.Column("group_identifier", db.String, primary_key=True, default="")
    Title = db.Column("title", db.String)
    CreationDate = db.Column("creation_date", db.DateTime)
    ExpirationDate = db.Column("expiration_date", db.DateTime)

    def get_wtf_form(self):
        return GroupForm(
            Title=self.Title,
            CreationDate=self.CreationDate,
            ExpirationDate=self.ExpirationDate
        )


class Students(db.Model):
    __tablename__ = "students"

    Id = db.Column("student_number", db.String, primary_key=True, default="")
    SSN = db.Column("ssn", db.Integer)
    Firstname = db.Column("firstname", db.String)
    Middlename = db.Column("middlename", db.String)
    Lastname = db.Column("lastname", db.String)
    Birthdate = db.Column("birthdate", db.DateTime)

    def get_wtf_form(self):
        return StudentForm(
            Firstname=self.Firstname,
            Middlename=self.Middlename,
            Lastname=self.Lastname,
            Birthdate=self.Birthdate,
            SSN=self.SSN,
        )


class StudentGroup(db.Model):
    __tablename__ = "studentgroup"

    Id = db.Column("id", db.String, primary_key=True, default="")

    StudentId = db.Column("student_number", db.String, db.ForeignKey('students.student_number'))
    Students = db.relationship('Students')

    GroupId = db.Column("group_identifier", db.String, db.ForeignKey('groups.group_identifier'))
    Groups = db.relationship("Groups")

    StartDate = db.Column("start_date", db.DateTime)
    EndDate = db.Column("end_date", db.DateTime)

    def get_wtf_form(self):
        return StudentGroupForm(
            Student=self.StudentId,
            Group=self.GroupId,
            StartDate=self.StartDate,
            EndDate=self.EndDate
        )
