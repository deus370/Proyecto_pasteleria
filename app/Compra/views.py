#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy

from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required

from app import Proveedor
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
        
        p=IngredientesDB.query \
            .with_entities(IngredientesDB.proveedor) \
            .filter(IngredientesDB.id_ingrediente.like(i)).all()
        
        compra= ComprasDB(costo=c,ingrediente=i,cantidad=can,estatus=1,proveedor=p[0].proveedor)
        
        db.session.add(compra)   
        db.session.commit()
        
        flash("Datos guardados")
        return redirect(url_for('compra.cargarTabla'))

    return render_template('comprasFormulario.html',**context)


@Compra.route('/cargarTabla',methods=['GET','POST'])
def cargarTabla():    
    result = ComprasDB.query.filter(ComprasDB.estatus==1).all()
    user_form = ComprasForm()
    ingredientes=[]
    proveedores=[]
    
    #Cargar nombre del proveedor
    for i in result:
            result1 = ProveedoresDB.query \
            .with_entities(ProveedoresDB.nombre) \
            .filter(ProveedoresDB.id_proveedor.like(i.proveedor)).all()
            proveedores.append(result1[0].nombre)
    
    #Cargar nombre del Ingrediente
    for i in result:
            result1 = IngredientesDB.query \
            .with_entities(IngredientesDB.nombre) \
            .filter(IngredientesDB.id_ingrediente.like(i.ingrediente)).all()
            ingredientes.append(result1[0].nombre)
        
    aux=len(proveedores)
    
    context={
        'user_form':user_form,
        'res':result,
        'proveedores':proveedores,
        'ingredientes':ingredientes,
        'aux':aux
    }
    
    if request.method=="POST":
        busqueda=str(request.form.get('busqueda')+'%')
        proveedores=[]
        ingredientes=[]
        print(busqueda)
        
        result = ComprasDB.query \
        .with_entities(ComprasDB.id_pedido,ComprasDB.fecha_ingreso,ComprasDB.costo,ComprasDB.cantidad,ComprasDB.total,ComprasDB.ingrediente,ComprasDB.proveedor) \
        .filter(ComprasDB.estatus==1,ComprasDB.fecha_ingreso.like(busqueda)).all()
        
        #Cargar nombre del proveedor
        for i in result:
                result1 = ProveedoresDB.query \
                .with_entities(ProveedoresDB.nombre) \
                .filter(ProveedoresDB.id_proveedor.like(i.proveedor)).all()
                proveedores.append(result1[0].nombre)
        
        #Cargar nombre del Ingrediente
        for i in result:
                result1 = IngredientesDB.query \
                .with_entities(IngredientesDB.nombre) \
                .filter(IngredientesDB.id_ingrediente.like(i.ingrediente)).all()
                ingredientes.append(result1[0].nombre)

        aux=len(proveedores)

        context={
        'user_form':user_form,
        'res':result,
        'proveedores':proveedores,
        'ingredientes':ingredientes,
        'aux':aux
        }
        
        return render_template('tablaCompras.html',**context)

    return render_template('tablaCompras.html',**context)




@Compra.route("/cancelar",methods=['GET','POST'])
def actualizar():
    print('cancelar')
    
    user_form = ComprasForm()
    
    id = request.form.get('id')
    
    #aCTUALIZAR
    compra = ComprasDB.query.filter_by(id_pedido=id).first()
    compra.estatus =0 
    
    
    db.session.commit()
    flash("datos actualizados")
    return redirect(url_for('compra.cargarTabla'))


