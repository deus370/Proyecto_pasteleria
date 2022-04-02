#Importamos los módulos a usar de flask
from math import prod
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
import base64
#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import ProductosDB, RecetasDB
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db
from sqlalchemy import insert,Column,Text
from flask_security.decorators import roles_required
from ..forms import ProductosForm
from ..Producto import Producto




@Producto.route('/Formulario',methods=['GET','POST'])
def Formulario():
    #Cargar los provedores y colocarlos en el select
    recetas  = RecetasDB.query.filter(RecetasDB.estatus==1).all()
    user_form = ProductosForm()
    
    #Llenamos el select
    user_form.receta.choices=[(i.id_receta,i.nombre) for i in recetas]

    context={
        'user_form':user_form
    }
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        c=float(user_form.cantidad.data)
        d=str(user_form.descripcion.data)
        p=float(user_form.precio.data)
        r=user_form.receta.data
        
        img = request.files['img']
    
        if not img:
            flash('Imagen no agregada')
            return redirect(url_for('main.registerProduct'))

        imagen = base64.b64encode(img.read())
        
        producto= ProductosDB(nombre=n,cantidad=c,descripccion=d,precio=p,receta=r,imagen=imagen,estatus=1)
        
        db.session.add(producto)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('producto.cargarTabla'))

    return render_template('productosFormulario.html',**context)


@Producto.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = ProductosDB.query.filter(ProductosDB.estatus==1).all()
    user_form = ProductosForm()
    recetas=[]
    
    for i in result:
            result1 = RecetasDB.query \
            .with_entities(RecetasDB.nombre) \
            .filter(RecetasDB.estatus==1,RecetasDB.id_receta.like(i.receta)).all()
            recetas.append(result1[0].nombre)
        
    aux=len(recetas)
    
    context={
        'user_form':user_form,
        'res':result,
        'recetas':recetas,
        'aux':aux
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        recetas=[]
        
        result = ProductosDB.query \
        .with_entities(ProductosDB.id_producto,ProductosDB.nombre,ProductosDB.cantidad,ProductosDB.precio,ProductosDB.descripccion,ProductosDB.receta,ProductosDB.imagen) \
        .filter(ProductosDB.estatus==1,ProductosDB.nombre.like(busqueda)).all()
        
        for i in result:
            result1 = RecetasDB.query \
            .with_entities(RecetasDB.nombre) \
            .filter(RecetasDB.estatus==1,RecetasDB.id_receta.like(i.receta)).all()
            recetas.append(result1[0].nombre)
        
        aux=len(recetas)
    
        context={
            'user_form':user_form,
            'res':result,
            'recetas':recetas,
            'aux':aux
        }
        
        return render_template('tablaProductos.html',**context)

    return render_template('tablaProductos.html',**context)

@Producto.route("/eliminar",methods=['GET','POST'])
def eliminar():
    id = request.form.get('id')
    print(id)
    
    producto = ProductosDB.query.filter_by(id_producto=id).first()
    producto.estatus=0
    db.session.commit()
    
    flash("datos Eliminados")
    return redirect(url_for('producto.cargarTabla'))


@Producto.route("/cargarActualizar",methods=['GET','POST'])
def cargarActualizar():
    recetas  = RecetasDB.query.filter(RecetasDB.estatus==1).all()
    user_form = ProductosForm()
    
    #Llenamos el select
    user_form.receta.choices=[(i.id_receta,i.nombre) for i in recetas]
    
    id = request.form.get('id')
    
    
    result = ProductosDB.query \
        .with_entities(ProductosDB.id_producto,ProductosDB.nombre,ProductosDB.cantidad,ProductosDB.precio,ProductosDB.descripccion,ProductosDB.receta,ProductosDB.imagen) \
        .filter(ProductosDB.id_producto.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
        
    return render_template('productosActualizar.html',**context)


@Producto.route("/actualizar",methods=['GET','POST'])
def actualizar():
    
    user_form = ProductosForm()
    
    id = request.form.get('id')
    n = request.form.get('nombre')
    p = request.form.get('precio')
    d = request.form.get('descripcion')
    c = request.form.get('cantidad')
    img = request.files['img']
    r=user_form.receta.data
    
    
    id = request.form.get('id')
    
    
    if not img:
        flash('Imagen no agregada')
        #aCTUALIZAR
        producto = ProductosDB.query.filter_by(id_producto=id).first()
        producto.nombre = n
        producto.precio = p
        producto.descripccion = d
        producto.cantidad = c
        producto.receta = r
        db.session.commit()
    else:
        imagen = base64.b64encode(img.read())
        producto = ProductosDB.query.filter_by(id_producto=id).first()
        producto.nombre = n
        producto.precio = p
        producto.descripccion = d
        producto.cantidad = c
        producto.receta = r
        producto.imagen=imagen
        db.session.commit()
    
    flash("datos actualizados")
    return redirect(url_for('producto.cargarTabla'))


@Producto.route("/preparar",methods=["GET","POST"])
def preparar():
    user_form = ProductosForm()
    
    id = request.form.get('id')
    
    
    result = ProductosDB.query \
        .with_entities(ProductosDB.id_producto,ProductosDB.nombre,ProductosDB.imagen,ProductosDB.cantidad) \
        .filter(ProductosDB.id_producto.like(id)).all()
        
    context={
        'user_form':user_form,
        'res':result
    }
    
    return render_template("productosPreparar.html",**context)

@Producto.route("/hornear",methods=['GET','POST'])
def hornear():
    
    user_form = ProductosForm()
    
    id = request.form.get('id')
    c = float(request.form.get('hornear'))
    
    producto = ProductosDB.query.filter_by(id_producto=id).first()
    producto.cantidad =(producto.cantidad+c)
    db.session.commit()
    
    
    flash("Panquecitos Horneados")
    return redirect(url_for('producto.cargarTabla'))