from flask_blueprint import Blueprint


from flask import Blueprint
Empleado = Blueprint('empleado', __name__, url_prefix='/empleado')

from . import views

