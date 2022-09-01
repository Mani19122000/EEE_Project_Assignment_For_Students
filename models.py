# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Employee(db.Model):
    _tablename_ = "Employee"

    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String())

    def _init_(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def _repr_(self):
        return f"{self.name}:{self.employee_id}"