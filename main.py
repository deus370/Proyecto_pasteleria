#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, redirect, render_template, request, url_for
from flask import Flask,render_template, url_for
from flask_wtf.csrf import CSRFProtect
from flask import request
from flask import make_response
from flask import flash

from app import create_app

import app.forms as forms
app=create_app()

#activar proteccion CSRF
csrf=CSRFProtect()

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/acerca')
def acerca():
    return render_template("acerca.html")

if __name__=="__main__":
    ##Levantar el servidor y que permita trabajar en el puerto 3000
    csrf.init_app(app)
    app.run(port=3000)
