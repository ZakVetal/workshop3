from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.worker_helper import WorkerHelper


class SearchForm(Form):
    worker_surname = StringField('Surname: ')
    assignment_name = StringField('Assignment: ')
    submit = SubmitField('Search')

    def get_result(self):
        helper = WorkerHelper()
        a= helper.GetJobData(self.worker_surname.data, self.assignment_name.data)
        print(a)
        return a


