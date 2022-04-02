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
    ingredientes  = IngredientesDB.query.filter(IngredientesDB.estatus==1).all()
    user_form = RecetaForm()
    
    #Llenamos el select
    user_form.ingrediente.choices=[(i.id_ingrediente,i.nombre) for i in ingredientes]
    

    context={
        'user_form':user_form
    }
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        c=float(user_form.cantidad.data)
        i=user_form.ingrediente.data
        
        receta= RecetasDB(nombre=n,cantidad=c,ingrediente=i,estatus=1)
        
        db.session.add(receta)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('receta.cargarTabla'))

    return render_template('/recetas/recetasFormulario.html',**context)


@Receta.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = RecetasDB.query.filter(RecetasDB.estatus==1).all()
    user_form = RecetaForm()
    Ingredientes=[]
    
    
    
    for i in result:
            result1 = IngredientesDB.query \
            .with_entities(IngredientesDB.nombre) \
            .filter(IngredientesDB.id_ingrediente.like(i.ingrediente)).all()
            Ingredientes.append(result1[0].nombre)
    
            
    aux=len(Ingredientes)
    
    context={
        'user_form':user_form,
        'res':result,
        'aux':aux,
        'ingrediente':Ingredientes
    
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        
        result = RecetasDB.query \
        .with_entities(RecetasDB.id_receta,RecetasDB.nombre,RecetasDB.cantidad,RecetasDB.ingrediente,RecetasDB.cubierta) \
        .filter(RecetasDB.nombre.like(busqueda)).all()
        
        
        Ingredientes=[]
        
        for i in result:
                result1 = IngredientesDB.query \
                .with_entities(IngredientesDB.nombre) \
                .filter(IngredientesDB.id_ingrediente.like(i.ingrediente)).all()
                Ingredientes.append(result1[0].nombre)
        
                
        aux=len(Ingredientes)
        
        context={
            'user_form':user_form,
            'res':result,
            'aux':aux,
            'ingrediente':Ingredientes
        }
        
        return render_template('/recetas/tablaReceta.html',**context)

    return render_template('/recetas/tablaReceta.html',**context)

@Receta.route("/eliminar",methods=['GET','POST'])
def eliminar():
    id = request.form.get('id')
    print(id)
    
    insumo = RecetasDB.query.filter_by(id_Receta=id).first()
    insumo.estatus=0
    db.session.commit()
    
    flash("datos Eliminados")
    return redirect(url_for('receta.cargarTabla'))


@Receta.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    ingredientes  = IngredientesDB.query.filter(IngredientesDB.estatus!=0).all()
    user_form = RecetaForm()
    
    #Llenamos el select
    user_form.ingrediente.choices=[(i.id_ingrediente,i.nombre) for i in ingredientes]
    
    id = request.form.get('id')
    
    
    result = RecetasDB.query \
        .with_entities(RecetasDB.id_receta,RecetasDB.nombre,RecetasDB.cantidad,RecetasDB.ingrediente) \
        .filter(RecetasDB.id_receta.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
    return render_template('/recetas/recetasActualizar.html',**context)


@Receta.route("/actualizar",methods=['GET','POST'])
def actualizar():
    
    user_form = RecetaForm()
    
    id = request.form.get('id')
    nombre=request.form.get('nombre')
    cantidad=request.form.get('cantidad')
    ingrediente=request.form.get('ingrediente')
    
    #aCTUALIZAR
    insumo = RecetasDB.query.filter_by(id_receta=id).first()
    insumo.nombre = nombre
    insumo.cantidad = cantidad
    insumo.ingrediente = ingrediente
    
    db.session.commit()
    flash("datos actualizados")
    return redirect(url_for('receta.cargarTabla'))


