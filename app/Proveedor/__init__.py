from flask_blueprint import Blueprint


from flask import Blueprint
Proveedor = Blueprint('proveedor', __name__, url_prefix='/proveedor')

from . import views

