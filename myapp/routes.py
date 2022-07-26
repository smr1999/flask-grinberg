from flask import render_template
from myapp import app
from myapp.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    myuser = {"username": "mohammad"}
    myposts = [
        {
            "author" : {"username" : "mohammd"},
            "body" : "This is the first post ."
        },
        {
            "author" : {"username" : "zahra"},
            "body" : "Avengers is the best movie i have ever seen !"
        }
    ]

    return render_template("index.html",user=myuser,title="Home",posts=myposts)

@app.route("/login")
def login():
    login_form = LoginForm()

    return render_template('login.html',form=login_form)