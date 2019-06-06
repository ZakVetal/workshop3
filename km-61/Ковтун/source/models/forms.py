from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms import validators
import Workshop.application.models.db as db_models
from Workshop.application.services.helper import DBHelper
import datetime


class StudentForm(Form):
    Firstname = StringField("Firstname", [validators.DataRequired("Firstname is required")])
    Lastname = StringField("Lastname", [validators.DataRequired("Lastname is required")])
    Middlename = StringField("Middlename")
    SSN = IntegerField("SSN", [validators.DataRequired("SSN is required")])
    Birthdate = DateField("Birthdate", [validators.Optional()])

    Submit = SubmitField("Submit")

    def get_db_student(self):
        return db_models.Students(
            Firstname=self.Firstname.data,
            Lastname=self.Lastname.data,
            Middlename=self.Middlename.data,
            SSN=self.SSN.data,
            Birthdate=self.Birthdate.data
        )

    def update_db_student(self, student):
        student.Firstname = self.Firstname.data
        student.Lastname = self.Lastname.data
        student.Middlename = self.Middlename.data
        student.SSN = self.SSN.data
        student.Birthdate = self.Birthdate.data


class GroupForm(Form):
    Title = StringField("Title", [validators.DataRequired("Group title is required")])
    CreationDate = DateField("Creation Date", [validators.DataRequired("Creation date is required")])
    ExpirationDate = DateField("Expiration Date", [validators.Optional()])

    Submit = SubmitField("Submit")

    def get_db_group(self):
        return db_models.Groups(
            Title=self.Title.data,
            CreationDate=self.CreationDate.data,
            ExpirationDate=self.ExpirationDate.data
        )

    def update_db_group(self, group):
        group.Title = self.Title.data
        group.CreationDate = self.CreationDate.data
        group.ExpirationDate = self.ExpirationDate.data


class StudentGroupForm(Form):
    Student = SelectField("Student", [validators.DataRequired("Student value is required")])
    Group = SelectField("Group", [validators.DataRequired("Group value is required")])
    StartDate = DateField("Start Date", [validators.DataRequired("Start date is required")])
    EndDate = DateField("End Date", [validators.Optional()])

    Submit = SubmitField("Submit")

    def get_db_student_group(self):
        return db_models.StudentGroup(
            StudentId=self.Student.data,
            GroupId=self.Group.data,
            StartDate=self.StartDate.data,
            EndDate=self.EndDate.data
        )

    def update_db_student_group(self, student_group):
        student_group.StudentId = self.Student.data
        student_group.GroupId = self.Group.data
        student_group.StartDate = self.StartDate.data
        student_group.EndDate = self.EndDate.data


class StudentsAdvancedSearchForm(Form):
    Firstname = StringField("Firstname", [validators.Optional()], default="",
                            render_kw={"placeholder": "Firstname"})
    Lastname = StringField("Lastname", [validators.Optional()], default="",
                           render_kw={"placeholder": "Lastname"})
    Group = SelectField("Group", choices=[('any', "Any group")], )

    Submit = SubmitField("Search")

    def get_requested_students(self):
        helper = DBHelper()
        return helper.find_student(self.Firstname.data if self.Firstname.data != "" else None,
                                   self.Lastname.data if self.Lastname.data != "" else None,
                                   self.Group.data if self.Group.data != 'any' else None)
