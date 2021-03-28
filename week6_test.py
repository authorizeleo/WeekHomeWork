from flask import Flask, session, redirect, request, flash , url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.secret_key = "123456"
app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True , autoincrement=True)  
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False , unique=True )
    password = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        registerusername = str(request.form['username'])
        registerPassword = request.form['registerPassword']
        Check = User.query.filter_by(username= registerusername).first()
        if  Check is not None and registerusername == Check.username  :
            return redirect('/loser')
        else:
            create(name, registerusername, registerPassword)
            flash("註冊成功!")
            return redirect('/')
            
    number = session.get('number')
    if number:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route('/signin', methods=["POST","GET"])
def signin():
    req = request.form
    numbers = str(req.get("AccountNumber"))
    password = req.get("password")
    if request.method == "POST":
        signinCheck = User.query.filter_by(username= numbers).first()
        if signinCheck is not None and numbers == signinCheck.username and password == signinCheck.password:
            session["number"] = "Hello world"
            return render_template("member.html",data=signinCheck.name)  
        else:
            message = request.args.get("message","帳號或密碼輸入錯誤")
            return redirect(url_for("error", message=message))
    number = session.get('number')
    if number:
        return redirect('/member/')
    else:
        return '<h1 style="color:lightpink">錯誤操作<h1> <br> <a href="/">返回首頁</a>'

@app.route('/member/')
def member():
    number = session.get('number')
    if number: 
        return render_template("member.html")
    else :
        flash("拜託你，可以好好登入嗎?")
        return redirect('/')


@app.route('/error/')
def error():
    number = session.get('number')
    if number:
        flash("千萬不要這樣子玩!")
        return redirect("/member/")
    else:
        message = request.args.get("message","帳號或密碼輸入錯誤")
        return render_template("error.html", message=message)

@app.route('/signout/')
def signout():
    session.pop("number", None)
    return redirect("/")

@app.route('/loser')
def loser():
    return '<h1 style="color:lightpink">帳號已經被註冊<h1> <br> <a href="/">返回首頁</a>' 


def create(name, username, password ): 
    oldUser = User.query.order_by(desc('id')).first()
    if oldUser == None:
        user = User(id = 1, name=name, username=username, password=password )
        add(user)
    else :
        user = User(id=oldUser.id +1 , name=name, username=username, password=password )
        add(user)

def add(user):
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    app.run(port=3000)