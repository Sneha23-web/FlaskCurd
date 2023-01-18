from flask import Flask, render_template,request,redirect
from models import db, StudentModel

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# @app.route('/')
# def main():
#         return 'Hello Snehaaaaaaa!!!!!!!'


@app.route('/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
         return render_template('create.html')

    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str,hobby))
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']

        students = StudentModel(
            f_name = f_name,
            l_name = l_name,
            email = email,
            password = password,
            gender = gender,
            hobbies = hobbies,
            country = country

        )
        db.session.add(students)
        db.session.commit()
        return redirect('/')

@app.route('/', methods = ['GET'])
def RetrieveList():
    std = StudentModel.query.all()
    return render_template('index.html',students = std)


@app.route('/<int:id>/edit', methods = ['GET','POST'])
def update(id):
    std = StudentModel.query.filter_by(id = id).first()
    
    if request.method == 'POST':
        db.session.delete(std)
        db.session.commit()
        if std:
            hobby = request.form.getlist('hobbies')
            hobbies = ",".join(map(str,hobby))
            f_name = request.form['f_name']
            l_name = request.form['l_name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            hobbies = hobbies
            country = request.form['country']
            
            studentdata = StudentModel(
                f_name = f_name,
                l_name = l_name,
                email = email,
                password = password,
                gender = gender,
                hobbies = hobbies,
                country = country
            )
            db.session.add(studentdata)
            db.session.commit()
            return redirect('/')
        return f"student with id = {id} does not exist"
    return render_template('update.html',std = std)



@app.route('/<int:id>/delete', methods = ['GET','POST'])
def delete(id):
    student = StudentModel.query.filter_by(id = id).first()
    if request.method == 'POST':
        if student:
             db.session.delete(student)
             db.session.commit()
             return redirect('/')
        abort(404)
    return render_template('delete.html')



app.run(host="localhost", port="5000")
