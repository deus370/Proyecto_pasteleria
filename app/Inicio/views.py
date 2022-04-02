from flask import render_template

from ..Inicio import Inicio

@Inicio.route("/cargarInicio")
def cargarInicio():
    return render_template("/inicio/inicio.html")