from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from wtforms import validators, ValidationError


class StudentForm(Form):


    student_daybook = StringField('student_daybook: ',[validators.DataRequired('Please enter student_daybook.'),validators.Length(16, 16, "Daybook only 16 symbols")])
    student_name = StringField('student_name: ', [validators.DataRequired('Please enter student_name.'),])
    student_birth = DateField('student_birth: ',[validators.DataRequired('Please enter student_birth.')])
    student_contract = StringField('student_contract: ', [validators.DataRequired('Please enter student_contract.')])



    submit = SubmitField('Submit')


class ModulesForm(Form):
     module_name= StringField('module_name: ', [validators.DataRequired('Please enter module_name.')])
     teacher = StringField('teacher: ', [validators.DataRequired('Please enter teacher.')])
     submit = SubmitField('Submit')


class LearningForm(Form):
    module_name_ = StringField('module_name_: ', [validators.DataRequired('Please enter module_name.')])
    student_daybook_ = StringField('student_daybook_: ',[validators.DataRequired('Please enter student_daybook.'),validators.Length(16, 16, "Daybook only 16 symbols")])
    reporting = DateField(' reporting: ',[validators.DataRequired('Please enter  reporting date.')])
    point = IntegerField(' reporting: ',[validators.DataRequired('Please enter  reporting date.'),validators.Length(0, 100, "Point only 0-100")])
    submit = SubmitField('Submit')

class searchForm(Form):
    min = StringField('min: ', [validators.DataRequired('Please enter min point.')])
    max = StringField('max: ', [validators.DataRequired('Please enter max point.')])
    daybook = StringField('daybook: ', [validators.DataRequired('Please enter your student'),validators.Length(16, 16, "Daybook only 16 symbols")])
    daterep = DateField('daterep: ', [validators.DataRequired('Please enter reporting date')])
    submit = SubmitField('Submit')
