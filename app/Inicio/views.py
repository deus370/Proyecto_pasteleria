from flask import render_template

from ..Inicio import Inicio

@Inicio.route("/cargarInicio")
def cargarInicio():
    return render_template("/inicio/inicio.html")

@Inicio.route("/cargarAcerca")
def cargarAcerca():
    return render_template("/inicio/acerca.html")