from flask import Flask, session, redirect, request, flash, url_for
from flask import render_template
from markupsafe import escape

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"


@app.route('/')
def index():
    number = session.get('number')
    if number:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route('/signin', methods=["POST"])
def signin():
    numbers = request.form["AccountNumber"]
    password = request.form["password"]
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
       return redirect('/')


@app.route('/error/')
def error():
    return render_template("error.html")

@app.route('/signout/')
def signout():
    session.pop("number", None)
    return redirect("/")


    


if __name__ == "__main__":
    app.run(port=3000)