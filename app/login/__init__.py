from flask_blueprint import Blueprint


from flask import Blueprint
Login = Blueprint('login', __name__, url_prefix='/login')

from . import views

