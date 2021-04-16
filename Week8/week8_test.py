from flask import Flask, session, redirect, request, flash , url_for
from flask import render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
import datetime
from sqlalchemy import desc



app = Flask(__name__)
app.secret_key = "123456"
app.config.from_object('config')
db = SQLAlchemy(app)
app.config["JSON_AS_ASCII"] = False


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True , autoincrement=True)  
    name = db.Column(db.String(255), nullable=False, index=True)
    username = db.Column(db.String(255), nullable=False , unique=True )
    password = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)





@app.route('/')
def index():
    status = request.cookies.get('status')
    if status :
        return render_template('member.html')
    return render_template("index.html")


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        registername = request.form['name']
        registerusername = request.form['username']
        registerPassword = request.form['registerPassword']
        Check = User.query.filter_by(username= registerusername).first()
        if registername.strip() != '' and  registerPassword.strip() != '' and registerusername.strip() != '':   
            if  Check is not None and registerusername == Check.username  :
                return redirect('/loser')
            else:
                create(registername, registerusername, registerPassword)
                flash("註冊成功!")
                return redirect('/')
        else:
            flash("欄位不得為空!")
            return redirect('/')


@app.route('/signin', methods=["POST","GET"])
def signin():
    req = request.form
    numbers = req.get("AccountNumber")
    password = req.get("password")
    if request.method == "POST":
        signinCheck = User.query.filter_by(username= numbers).first()
        if signinCheck is not None and numbers == signinCheck.username and password == signinCheck.password:
            session['id'] = signinCheck.id
            resp = make_response(redirect('/member/'))
            resp.set_cookie('status', 'login' )
            resp.set_cookie('username', signinCheck.username)
            return resp
        else:
            return redirect(url_for("error", message="帳號或密碼輸入錯誤"))
    status = request.cookies.get('status')
    if status:
        return redirect('/member/')
    else:
        return '<h1 style="color:lightpink">錯誤操作<h1> <br> <a href="/">返回首頁</a>'

@app.route('/member/' , methods=["POST","GET"])
def member():
    status = request.cookies.get('status')
    username = request.cookies.get('username')
    databases = User.query.filter_by(username=username).first()
    if status: 
        return render_template("member.html" , data=databases.name )
    else :
        flash("拜託你，可以好好登入嗎?")
        return redirect('/')




@app.route('/error/')
def error():
    status = request.cookies.get('status')
    if status:
        flash("千萬不要這樣子玩!")
        return redirect("/member/")
    else:
        message = request.args.get("message","帳號或密碼輸入錯誤")
        return render_template("error.html", message=message)

@app.route('/signout/')
def signout():
    resp = make_response(redirect("/"))
    resp.delete_cookie('status')
    resp.delete_cookie('username')
    return resp

@app.route('/loser')
def loser():
    return '<h1 style="color:lightpink">帳號已經被註冊<h1> <br> <a href="/">返回首頁</a>' 

@app.route('/api/users')
def api():           
    nulluser = {
        "data": None
    }
    if 'username' in request.args:
        username = request.args['username']
    else:
        return jsonify(nulluser)
    databases = User.query.filter_by(username=username).first()
    if databases is None:
        return jsonify(nulluser)
    else:
        users ={
            "data":{
                "id":databases.id,
                "name":databases.name,
                "username":databases.username
            }
        }
        return jsonify(users)  


@app.route('/api/user', methods=['POST',"GET"])
def updatename():
    test_ok = {
        "ok":True
    }
    test_error = {
        "error":True
    }
    status = request.cookies.get('status')
    username = request.cookies.get('username')
    databases = User.query.filter_by(username=username).first()
    if status:
        if request.method == 'POST':
            update = request.json["name"]
            databases.name = update
            db.session.commit()
            return jsonify(test_ok)
        else:
            return jsonify(test_error)
    else:
        return redirect("/")


   



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
    db.create_all()
    app.run(port=3000,debug=True)