#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import ProveedoresDB
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text,and_
from flask_security.decorators import roles_required
from ..forms import proveedoresForm
from ..Proveedor import Proveedor




@Proveedor.route('/Formulario',methods=['GET','POST'])
def Formulario():
    
    user_form = proveedoresForm()
    
    context={
        'user_form':user_form
    }
    
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        c=str(user_form.calle.data)
        nu=int(user_form.numero.data)
        cp=int(user_form.cp.data)
        colonia=str(user_form.colonia.data)
        
        
        proveedor = ProveedoresDB(nombre=n,calle=c,numero=nu,cp=cp,colonia=colonia,estatus=1)
        print(proveedor)
        db.session.add(proveedor)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('proveedor.cargarTabla'))

    return render_template('proveedoresFormulario.html',**context)


@Proveedor.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = ProveedoresDB.query.filter(ProveedoresDB.estatus==1).all()
    user_form = proveedoresForm()
    
    context={
        'user_form':user_form,
        'res':result
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        print(busqueda)
        
        
        result = ProveedoresDB.query \
        .with_entities(ProveedoresDB.id_proveedor,ProveedoresDB.nombre,ProveedoresDB.calle,ProveedoresDB.numero,
            ProveedoresDB.cp,ProveedoresDB.colonia) \
        .filter(ProveedoresDB.estatus==1,ProveedoresDB.nombre.like(busqueda)).all()
        
        context={
        'user_form':user_form,
        'res':result
        }
        
        return render_template('tablaProveedor.html',**context)

    return render_template('tablaProveedor.html',**context)

@Proveedor.route("/eliminar",methods=['GET','POST'])
def eliminar():
    id = request.form.get('id')
    
    
    proveedor = ProveedoresDB.query.filter_by(id_proveedor=id).first()
    
    proveedor.estatus=0
    
    db.session.commit()
    
    flash("datos Eliminados")
    return redirect(url_for('proveedor.cargarTabla'))

@Proveedor.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    user_form = proveedoresForm()
    
    id = request.form.get('id')
    
    result = ProveedoresDB.query \
        .with_entities(ProveedoresDB.id_proveedor,ProveedoresDB.nombre,ProveedoresDB.calle,ProveedoresDB.numero,
            ProveedoresDB.cp,ProveedoresDB.colonia) \
        .filter(ProveedoresDB.id_proveedor.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
        
    return render_template('proveedoresActualizar.html',**context)


@Proveedor.route("/actualizar",methods=['GET','POST'])
def actualizar():
    
    id = request.form.get('id')
    nombre=request.form.get('nombre')
    calle=request.form.get('calle')
    numero=request.form.get('numero')
    cp=request.form.get('cp')
    colonia=request.form.get('colonia')
    
    #aCTUALIZAR
    proveedor = ProveedoresDB.query.filter_by(id_proveedor=id).first()
    proveedor.nombre = nombre
    proveedor.calle = calle
    proveedor.numero = numero
    proveedor.cp = cp
    proveedor.colonia = colonia
    
    db.session.commit()
    flash("datos actualizados")
    return redirect(url_for('proveedor.cargarTabla'))


