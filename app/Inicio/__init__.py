from flask_blueprint import Blueprint


from flask import Blueprint
Inicio = Blueprint('inicio', __name__, url_prefix='/inicio')

from . import views