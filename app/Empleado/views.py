#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash,Flask
import sqlalchemy
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

#Importamos el método login_required de flask_security
from flask_security import login_required
#Importamos el modelo del usuario
from ..modelos import Usuario, Persona, users_roles
#Importamoes el objeto de la BD y userDataStore desde __init__
from .. import db, userDataStore
from sqlalchemy import insert,Column,Text
from flask_security.decorators import roles_required
from ..forms import EmpleadosForm
from ..Empleado import Empleado




@Empleado.route('/FormularioEmpleados',methods=['GET','POST'])
def Formulario():
    
    user_form = EmpleadosForm()
    
    context={
        'user_form':user_form
    }
    
    
    if user_form.is_submitted():
        n=str(user_form.nombre.data)
        ap=str(user_form.a_paterno.data)
        am=str(user_form.a_materno.data)
        telefono= str(user_form.telefono.data)
        correo = str(user_form.correo.data)
        contrasena = str(user_form.contrasena.data)
        c=str(user_form.calle.data)
        nu=int(user_form.numero.data)
        cp=int(user_form.cp.data)
        colonia=str(user_form.colonia.data)
        
            #Consultamos si existe un usuario ya registrado con el email.
        user = Persona.query.filter_by(correo=correo).first()
        if user: #Si se encontró un usuario, redireccionamos de regreso a la página de registro
            flash('El correo electrónico ya existe')
            #return redirect(url_for('auth.register'))
            return render_template('personaFormulario.html',**context)
        
        persona = Persona(nombre=n,a_paterno=ap,a_materno=am,telefono=telefono,correo=correo,calle=c,numero=nu,cp=cp,colonia=colonia)
        print(persona)
        db.session.add(persona)
        db.session.commit()
        
        persona_nuevo = Persona.query.filter_by(correo=correo).first()
        personaId = persona_nuevo.id_persona;
        print(personaId)
        
        userDataStore.create_user(
            usuario=correo,contrasena=generate_password_hash(contrasena, method='sha256'),persona=personaId,estatus=1
        )   
        
        db.session.commit()
        
        print("usuario creado")
        #usuario = Usuario(usuario=correo,contrasena=contrasena,persona=personaId,rol=2)
        
        flash("Datos guardados")
        #return redirect(url_for('proveedor.cargarTabla'))
        return render_template('personaFormulario.html',**context)

    return render_template('personaFormulario.html',**context)


@Empleado.route('/cargarTablaEmpleado',methods=['GET','POST'])
def cargarTabla():    
    result = db.session.query(Persona.id_persona,Persona.nombre, Persona.a_materno, Persona.a_materno,Persona.calle,Persona.numero,
            Persona.cp,Persona.colonia).filter(Persona.correo == Usuario.usuario).filter(Usuario.estatus == 1).all()
    user_form = EmpleadosForm()
    
    context={
        'user_form':user_form,
        'res':result
    }
    
    if request.method=="POST":
        busqueda=request.form.get('busqueda')+'%'
        
        
        result = db.session.query(Persona.id_persona,Persona.nombre, Persona.a_materno, Persona.a_materno,Persona.calle,Persona.numero,
            Persona.cp,Persona.colonia).filter(Persona.nombre.like(busqueda)).filter(Persona.correo == Usuario.usuario).all()
        
        context={
        'user_form':user_form,
        'res':result
        }
        
        return render_template('tablaEmpleados.html',**context)

    return render_template('tablaEmpleados.html',**context)

@Empleado.route("/eliminarEmpleado",methods=['GET','POST'])
def eliminar():
    id_persona = request.form.get('id')
    print(id_persona)
    
    usuario = Usuario.query.filter_by(persona=id_persona).first()
    usuario.estatus = 0
    db.session.delete(usuario)
    db.session.commit()
    
    flash("datos Eliminados")
    return redirect(url_for('empleado.cargarTablaEmpleado'))

'''@Empleado.route("/cargarActualizar",methods=['GET','POST'])
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


@Empleado.route("/actualizar",methods=['GET','POST'])
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


'''