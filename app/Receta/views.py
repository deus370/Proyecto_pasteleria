#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import RecetasDB, IngredientesDB
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text
from flask_security.decorators import roles_required
from ..forms import RecetaForm
from ..Receta import Receta




@Receta.route('/Formulario',methods=['GET','POST'])
def Formulario():
    #Cargar los provedores y colocarlos en el select
    ingredientes  = IngredientesDB.query.all()
    user_form = RecetaForm()
    
    #Llenamos el select
    user_form.ingrediente.choices=[(i.id_ingrediente,i.nombre) for i in ingredientes]

    context={
        'user_form':user_form
    }
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        c=float(user_form.cantidad.data)
        i=str(user_form.ingrediente.data)
        
        
        receta= RecetasDB(nombre=n,cantidad=c,ingrediente=i)
        
        db.session.add(receta)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('receta.cargarTabla'))

    return render_template('recetasFormulario.html',**context)


@Receta.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = RecetasDB.query.all()
    user_form = RecetaForm()
    
    for i in result:
        print(i.proveedor)
    
    
    context={
        'user_form':user_form,
        'res':result
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        
        result = IngredientesDB.query \
        .with_entities(IngredientesDB.id_ingrediente,IngredientesDB.nombre,IngredientesDB.cantidad,IngredientesDB.unidad,IngredientesDB.proveedor) \
        .filter(IngredientesDB.nombre.like(busqueda)).all()




        context={
        'user_form':user_form,
        'res':result
        }
        
        return render_template('tablaInsumo.html',**context)

    return render_template('tablaInsumo.html',**context)

@Receta.route("/eliminar",methods=['GET','POST'])
def eliminar():
    id = request.form.get('id')
    print(id)
    
    insumo = RecetasDB.query.filter_by(id_Receta=id).first()
    db.session.delete(insumo)
    db.session.commit()
    
    flash("datos Eliminados")
    return redirect(url_for('insumo.cargarTabla'))


@Receta.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    ingredientes  = IngredientesDB.query.all()
    user_form = RecetaForm()
    
    #Llenamos el select
    user_form.proveedor.choices=[(i.id_ingrediente,i.nombre) for i in ingredientes]
    
    id = request.form.get('id')
    
    
    result = IngredientesDB.query \
        .with_entities(IngredientesDB.id_ingrediente,IngredientesDB.nombre,IngredientesDB.cantidad,IngredientesDB.unidad,IngredientesDB.proveedor) \
        .filter(IngredientesDB.id_ingrediente.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
        
    return render_template('insumosActualizar.html',**context)


@Receta.route("/actualizar",methods=['GET','POST'])
def actualizar():
    
    user_form = RecetaForm()
    
    id = request.form.get('id')
    nombre=request.form.get('nombre')
    cantidad=request.form.get('cantidad')
    unidad=request.form.get('unidad')
    proveedor=request.form.get('proveedor')
    
    #aCTUALIZAR
    insumo = IngredientesDB.query.filter_by(id_ingrediente=id).first()
    insumo.nombre = nombre
    insumo.unidad = unidad
    insumo.cantidad = cantidad
    insumo.proveedor = proveedor
    
    db.session.commit()
    flash("datos actualizados")
    return redirect(url_for('insumo.cargarTabla'))


