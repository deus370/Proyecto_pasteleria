from flask_blueprint import Blueprint


from flask import Blueprint
Compra = Blueprint('compra', __name__, url_prefix='/compra')

from . import views
