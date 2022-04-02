from flask_blueprint import Blueprint


from flask import Blueprint
Insumo = Blueprint('insumo', __name__, url_prefix='/insumo')

from . import views