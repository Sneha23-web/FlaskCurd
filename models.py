from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class StudentModel(db.Model):   
    _tablename_ = "students"

    id = db.Column(db.Integer, primary_key = True)
    f_name = db.Column(db.String())
    l_name = db.Column(db.String())
    email = db.Column(db.String())
    dob = db.Column(db.String())
    gender = db.Column(db.String())
    acc_type = db.Column(db.String())
    pan = db.Column(db.String(80))
    aadhaar = db.Column(db.String(80))
    country = db.Column(db.String(80))
    state = db.Column(db.String(80))
    pre_branch = db.Column(db.String(80))
    addr = db.Column(db.String(80))

    
    def _init_(self,f_name,l_name,email,dob,gender,acc_type,pan,aadhaar,country,state,pre_branch,addr):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.acc_type = acc_type
        self.pan = pan
        self.aadhaar = aadhaar
        self.country = country
        self.state = state
        pre_branch = pre_branch
        addr = addr


    def _repr_(self):
        return f"{self.f_name}:{self.l_name}"