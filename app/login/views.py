#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del 
# 
from ..modelos import Usuario
from flask_security.utils import login_user, logout_user, hash_password, encrypt_password

#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text,and_
from flask_security.decorators import roles_required


from ..forms import proveedoresForm
from ..login import Login


@Login.route('/login')
def login():
    return render_template('/login/login.html')

@Login.route('/login', methods=['POST'])
def login_post():
    print("login2")
    email = request.form.get('email')
    password = request.form.get('contrasena')

    #Consultamos si existe un usuario ya registrado con el email.
    user = Usuario.query.filter_by(usuario=email).first()

    #Verificamos si el usuario existe
    #Tomamos el password proporcionado por el usuario lo hasheamos, y lo comparamos con el password de la base de datos.
    if not user or not check_password_hash(user.contrasena, password):
    #if not user or not user.password==encrypt_password(password):
        #Si el usuario no existe o no coinciden los passwords
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('login.login')) #Si el usuario no existe o el password es incorrecto regresamos a login
    
    #Si llegamos a este punto sabemos que el usuario tiene datos correctos.
    #Creamos una sessión y logueamos al usuario
    login_user(user)
    return redirect(url_for('inicio.cargarInicio'))