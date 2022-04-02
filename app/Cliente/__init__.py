from flask_blueprint import Blueprint


from flask import Blueprint
Cliente = Blueprint('cliente', __name__, url_prefix='/cliente')

from . import views

