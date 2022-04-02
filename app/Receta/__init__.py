from flask_blueprint import Blueprint


from flask import Blueprint
Receta = Blueprint('receta', __name__, url_prefix='/receta')

from . import views