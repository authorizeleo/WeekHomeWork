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
        registerusername = request.form['username']
        registerPassword = request.form['registerPassword']
        Check = User.query.filter_by(username= registerusername).first()
        if name != "" and  registerPassword != "" and registerusername != "":   
            if  Check is not None and registerusername == Check.username  :
                return redirect('/loser')
            else:
                create(name, registerusername, registerPassword)
                flash("註冊成功!")
                return redirect('/')
        else:
            flash("欄位不得為空!")
            return redirect('/')
            
    name = session.get('name')
    if name:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route('/signin', methods=["POST","GET"])
def signin():
    req = request.form
    numbers = req.get("AccountNumber")
    password = req.get("password")
    if request.method == "POST":
        signinCheck = User.query.filter_by(username= numbers).first()
        if signinCheck is not None and numbers == signinCheck.username and password == signinCheck.password:
            session["name"] = signinCheck.name
            session['id'] = signinCheck.id
            return  redirect("/member/") 
        else:
            return redirect(url_for("error", message="帳號或密碼輸入錯誤"))
    name = session.get('name')
    if name:
        return redirect('/member/')
    else:
        return '<h1 style="color:lightpink">錯誤操作<h1> <br> <a href="/">返回首頁</a>'

@app.route('/member/' , methods=['GET','POST'])
def member():
    name = session.get('name')
    id = session.get('id')
    if name: 
        if request.method == 'POST':
            EditPassword = request.form['EditPassword']
            again = request.form['again']
            EditMember = User.query.filter_by(id=id).first()
            if EditPassword == again and EditPassword != "":
                EditMember.password = EditPassword
                db.session.commit()
                flash('密碼修改完成')
                return redirect('/member/')
            elif (EditPassword == "" or again == ""):
                flash('密碼不得為空')
                return redirect('/member/')
            else :
                flash('密碼兩者不一致')
                return redirect('/member/')
        else:
            return render_template("member.html" , data=name)
    else :
        flash("拜託你，可以好好登入嗎?")
        return redirect('/')




@app.route('/error/')
def error():
    name = session.get('name')
    if name:
        flash("千萬不要這樣子玩!")
        return redirect("/member/")
    else:
        message = request.args.get("message","帳號或密碼輸入錯誤")
        return render_template("error.html", message=message)

@app.route('/signout/')
def signout():
    session.pop("name", None)
    session.pop("id", None)
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