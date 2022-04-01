from flask_blueprint import Blueprint


from flask import Blueprint
Compra = Blueprint('compra', __name__, url_prefix='/compras')

from . import views
