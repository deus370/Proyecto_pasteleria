from email.policy import default
from . import db
from flask_sqlalchemy import SQLAlchemy
#Importamos las clases UserMixin y RoleMixin de flask_security
from flask_security import Security, UserMixin, RoleMixin

users_roles = db.Table('usuario_roles',
    db.Column('id_usuario', db.Integer, db.ForeignKey('Usuario.id_usuario')),
    db.Column('id_rol', db.Integer, db.ForeignKey('Rol.id_rol')))

class Usuario(db.Model, UserMixin):
    """User account model"""
    
    __tablename__ = 'Usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), unique=True)
    contrasena = db.Column(db.String(250), nullable=False)
    persona = db.Column(db.Integer, nullable=False)
    estatus = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    #confirmed_at = db.Column(db.DateTime)
    '''persona = db.reltionship('Persona',
        secondary=personaU,
        backref= db.backref('persona', lazy='dynamic')
        )'''
    roles = db.relationship('Rol',
        secondary=users_roles,
        backref= db.backref('Uruario', lazy='dynamic'))

class Rol(RoleMixin, db.Model):
    """Role model"""

    __tablename__ = 'Rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Productos(db.Model):
    """Productos account model"""
    
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    precio= db.Column(db.Integer, nullable=False)
    
class ProveedoresDB(db.Model):
    """Proveedores account model"""
    
    __tablename__ = 'proveedor'
    id_proveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    calle= db.Column(db.String(100), nullable=False)
    numero=db.Column(db.Integer, nullable=False)
    cp=db.Column(db.Integer, nullable=False)
    colonia=db.Column(db.String(100), nullable=False)
    
class Persona(db.Model):
    """Persona account model"""
    
    __tablename__ = 'Persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    a_paterno = db.Column(db.String(100), nullable=False)
    a_materno = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    calle= db.Column(db.String(100), nullable=False)
    numero=db.Column(db.Integer, nullable=False)
    cp=db.Column(db.Integer, nullable=False)
    colonia=db.Column(db.String(100), nullable=False)
   
    