#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import ComprasDB,ProveedoresDB, IngredientesDB
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text
from flask_security.decorators import roles_required
from ..forms import ComprasForm
from ..Compra import Compra

@Compra.route('/Formulario',methods=['GET','POST'])
def Formulario():
    #Cargar los provedores y colocarlos en el select
    ingredientes  = IngredientesDB.query.all()
    user_form =ComprasForm()
    
    #Llenamos el select
    user_form.ingrediente.choices=[(i.id_ingrediente,i.nombre) for i in ingredientes]

    context={
        'user_form':user_form
    }
    
    if user_form.is_submitted():
        c=float(user_form.costo.data)
        i=int(user_form.ingrediente.data)
        can=str(user_form.cantidad.data)
        
        
        compra= ComprasDB(costo=c,ingrediente=i,cantidad=can)
        
        db.session.add(compra)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('compra.cargarTabla'))

    return render_template('comprasFormulario.html',**context)


@Compra.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = IngredientesDB.query.all()
    user_form = IngredientesForm()
    proveedores=[]
    
    for i in result:
            result1 = ProveedoresDB.query \
            .with_entities(ProveedoresDB.nombre) \
            .filter(ProveedoresDB.id_proveedor.like(i.proveedor)).all()
            proveedores.append(result1[0].nombre)
        
    aux=len(proveedores)
    
    context={
        'user_form':user_form,
        'res':result,
        'proveedores':proveedores,
        'aux':aux
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        proveedores=[]
        
        print(busqueda)
        
        result = IngredientesDB.query \
        .with_entities(IngredientesDB.id_ingrediente,IngredientesDB.nombre,IngredientesDB.cantidad,IngredientesDB.unidad,IngredientesDB.proveedor) \
        .filter(IngredientesDB.nombre.like(busqueda)).all()
        
        
        for i in result:
            result1 = ProveedoresDB.query \
            .with_entities(ProveedoresDB.nombre) \
            .filter(ProveedoresDB.id_proveedor.like(i.proveedor)).all()
            proveedores.append(result1[0].nombre)

        aux=len(proveedores)

        context={
        'user_form':user_form,
        'res':result,
        'proveedores':proveedores,
        'aux':aux
        }
        
        return render_template('tablaInsumo.html',**context)

    return render_template('tablaInsumo.html',**context)


@Compra.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    proveedores  = ProveedoresDB.query.all()
    ingredientes  = InsumoDB.query.all()
    user_form = insumoForm()
    
    #Llenamos el select
    user_form.proveedor.choices=[(i.id_proveedor,i.nombre) for i in proveedores]
    
    id = request.form.get('id')
    
    
    result = IngredientesDB.query \
        .with_entities(IngredientesDB.id_ingrediente,IngredientesDB.nombre,IngredientesDB.cantidad,IngredientesDB.unidad,IngredientesDB.proveedor) \
        .filter(IngredientesDB.id_ingrediente.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
        
    return render_template('insumosActualizar.html',**context)


@Compra.route("/actualizar",methods=['GET','POST'])
def actualizar():
    
    user_form = insumoForm()
    
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


