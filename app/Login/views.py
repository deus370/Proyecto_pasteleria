from flask import render_template

from ..Login import Login

@Login.route("/login")
def login():
    return render_template("/login/login.html")

@Login.route("/register")
def register():
    return render_template("/login/register.html")