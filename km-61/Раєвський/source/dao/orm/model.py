from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class OrmWorker(Base):
    __tablename__ = 'worker'

    worker_id = Column(Integer, primary_key=True)
    worker_name = Column(String(30), nullable=False)
    worker_surname = Column(String(30), nullable=False)
    worker_patronymic = Column(String(30), nullable=True)
    worker_birth_date = Column(Date, nullable=False)
    worker_job_title = Column(String(30), nullable=False)

    orm_workers = relationship('OrmWorkerAssignment')

    def __init__(self, worker_name, worker_surname, worker_patronymic, worker_birth_date, worker_job_title):
        self.worker_name = worker_name
        self.worker_surname = worker_surname
        self.worker_patronymic = worker_patronymic
        self.worker_birth_date = worker_birth_date
        self.worker_job_title = worker_job_title


class OrmAssignment(Base):
    __tablename__ = 'assignment'

    assignment_id = Column(Integer, primary_key=True)
    assignment_name = Column(String(30), nullable=False)
    assignment_description = Column(String(2000), nullable=False)
    assignment_time = Column(Date, nullable=False)

    orm_users = relationship('OrmWorkerAssignment')

    def __init__(self, assignment_name, assignment_description, assignment_time):
        self.assignment_name = assignment_name
        self.assignment_description = assignment_description
        self.assignment_time = assignment_time


class OrmWorkerAssignment(Base):
    __tablename__ = 'worker_assignment'

    wa_worker_id_fk = Column(Integer, ForeignKey('worker.worker_id'), primary_key = True)
    wa_assignment_id_fk = Column(Integer, ForeignKey('assignment.assignment_id'), primary_key=True)
    wa_assignment_date = Column(Date, nullable=False)
    wa_complete_time = Column(Date, nullable=True)