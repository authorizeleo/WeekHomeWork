from flask import Flask, session, redirect, request, flash , url_for
from flask import render_template, jsonify
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy import desc


app = Flask(__name__)
app.secret_key = "123456"
app.config.from_object('config')
db = SQLAlchemy(app)
app.config["JSON_AS_ASCII"] = False


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True , autoincrement=True)  
    name = db.Column(db.String(5), nullable=False)
    username = db.Column(db.String(255), nullable=False , unique=True )
    password = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)





@app.route('/',methods=['POST','GET'])
def index():
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
            updateName = request.form['updateName']
            if updateName.strip() == "" : 
                flash('名字不得為空')
                return redirect('/member/')
            SearchupdateName = User.query.filter_by(id=id).first()
            SearchupdateName.name = updateName
            session["name"] = SearchupdateName.name
            db.session.commit()
            flash('更新成功')
            return render_template("member.html" , data=updateName)
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

@app.route('/api/users')
def api():
    databases = User.query.all()
    words = []
    for data in databases:
        word = {
            "data":{
                "id":data.id,
                "name":data.name,
                "username":data.username},
        }
        words.append(word)
        
    nulluser = {
        "data": None
    }
    if 'username' in request.args:
        username = request.args['username']
    else:
        return jsonify(nulluser)
    for w in words:
        if w['data']["username"] == username:
            return jsonify(w)
    return jsonify(nulluser)


   



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
    