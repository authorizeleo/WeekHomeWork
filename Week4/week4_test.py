from flask import Flask, session, redirect, request, flash, url_for
from flask import render_template
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "123456"


@app.route('/')
def index():
    number = session.get('number')
    if number:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route('/signin', methods=["POST","GET"])
def signin():
    req = request.form
    numbers = req.get("AccountNumber")
    password = req.get("password")
    if request.method == "POST":
        if numbers == "test" and password == "test":
            session["number"] = "Hello world"
            return redirect("/member/")  
        else:
            return redirect("/error/")

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
        return render_template("error.html")

@app.route('/signout/')
def signout():
    session.pop("number", None)
    return redirect("/")


    


if __name__ == "__main__":
    app.run(port=3000)