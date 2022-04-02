from flask import render_template
from flask_security import login_required, current_user

from ..Inicio import Inicio

@Inicio.route("/cargarInicio")
@login_required
def cargarInicio():
    return render_template("/inicio/inicio.html", name=current_user.name)