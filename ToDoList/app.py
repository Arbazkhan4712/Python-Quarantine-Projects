from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_craeted = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


# @app.route('/<name>')
# def hello(name):
#     return 'hello {}\'s profile'.format(escape(name))
@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        title = request.form['title']
        desc= request.form['desc']
        todo = ToDo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo =ToDo.query.all()
    return render_template('index.html',alltodo=alltodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = ToDo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")




@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST': 
        title = request.form['title']
        desc= request.form['desc']
        todo = ToDo(title=title, desc=desc)
        todo = ToDo.query.filter_by(sno=sno).first()
        todo.titl = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = ToDo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)


if __name__ == "__main__":
    app.run(debug=True)