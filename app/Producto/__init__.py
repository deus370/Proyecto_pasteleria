from flask_blueprint import Blueprint


from flask import Blueprint
Producto = Blueprint('producto', __name__, url_prefix='/producto')

from . import views
