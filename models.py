from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class StudentModel(db.Model):
    _tablename_ = "students"

    id = db.Column(db.Integer, primary_key = True)
    f_name = db.Column(db.String())
    l_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String())
    hobbies = db.Column(db.String())
    country = db.Column(db.String(80))
    
    def _init_(self,f_name,l_name,email,password,gender,hobbies,country):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        self.gender = gender
        self.hobbies = hobbies
        self.country = country

    def _repr_(self):
        return f"{self.f_name}:{self.l_name}"