#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import ProveedoresDB, IngredientesDB
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text
from flask_security.decorators import roles_required
from ..forms import insumoForm
from ..Insumos import Insumo

@Insumo.route('/Formulario',methods=['GET','POST'])
def Formulario():
    #Cargar los provedores y colocarlos en el select
    proveedores  = ProveedoresDB.query.filter(ProveedoresDB.estatus==1).all()
    user_form = insumoForm()
    
    #Llenamos el select
    user_form.proveedor.choices=[(i.id_proveedor,i.nombre) for i in proveedores]

    context={
        'user_form':user_form
    }
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        c=float(user_form.Cantidad.data)
        u=str(user_form.unidad.data)
        p=str(user_form.proveedor.data)
        
        
        print(c)
        insumo= IngredientesDB(nombre=n,cantidad=c,unidad=u,proveedor=p)
        
        db.session.add(insumo)   
        db.session.commit()
        
        flash("Se guardaron correctamente los datos")
        return redirect(url_for('insumo.cargarTabla'))

    return render_template('/insumos/insumosFormulario.html',**context)


@Insumo.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = IngredientesDB.query.filter(IngredientesDB.estatus!=0,).all()
    user_form = insumoForm()
    proveedores=[]
    
    for i in result:
            result1 = ProveedoresDB.query \
            .with_entities(ProveedoresDB.nombre) \
            .filter(ProveedoresDB.estatus==1,ProveedoresDB.id_proveedor.like(i.proveedor)).all()
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
        .filter(IngredientesDB.estatus!=0,IngredientesDB.nombre.like(busqueda)).all()
        
        
        for i in result:
            result1 = ProveedoresDB.query \
            .with_entities(ProveedoresDB.nombre) \
            .filter(ProveedoresDB.estatus==1,ProveedoresDB.id_proveedor.like(i.proveedor)).all()
            proveedores.append(result1[0].nombre)

        aux=len(proveedores)

        context={
        'user_form':user_form,
        'res':result,
        'proveedores':proveedores,
        'aux':aux
        }
        
        return render_template('/insumos/tablaInsumo.html',**context)

    return render_template('/insumos/tablaInsumo.html',**context)

@Insumo.route("/eliminar",methods=['GET','POST'])
def eliminar():
    id = request.form.get('id')
    print(id)
    
    insumo = IngredientesDB.query.filter_by(id_ingrediente=id).first()
    insumo.estatus=0
    db.session.commit()
    
    flash("Se eliminaron los datos correctamente")
    return redirect(url_for('insumo.cargarTabla'))


@Insumo.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    proveedores  = ProveedoresDB.query.filter(ProveedoresDB.estatus==1).all()
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
    return render_template('/insumos/insumosActualizar.html',**context)


@Insumo.route("/actualizar",methods=['GET','POST'])
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
    flash("Se actualizaron correctamente los datos")
    return redirect(url_for('insumo.cargarTabla'))


