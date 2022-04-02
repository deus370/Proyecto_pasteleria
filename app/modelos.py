from email.policy import default
from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT
#Importamos las clases UserMixin y RoleMixin de flask_security
from flask_security import Security, UserMixin, RoleMixin
from flask_security import UserMixin, RoleMixin
from sqlalchemy.dialects.mysql import DOUBLE

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
    estatus=db.Column(db.Integer, nullable=False)

class IngredientesDB(db.Model):
    """Ingredientes account model"""
    
    __tablename__ = 'Ingrediente'
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad= db.Column(db.Float, nullable=False)
    unidad=db.Column(db.String, nullable=True)
    estatus=db.Column(db.Integer, nullable=True)
    proveedor=db.Column(db.Integer, nullable=True)
    
    
class ComprasDB(db.Model):
    """Compras account model"""
    __tablename__ = 'proveedor_ingrediente'
    id_pedido = db.Column(db.Integer, primary_key=True)
    fecha_ingreso= db.Column(db.Date, nullable=True)
    costo = db.Column(db.String(100), nullable=True)
    cantidad= db.Column(db.Float, nullable=True)
    total= db.Column(db.Float, nullable=True)
    estatus=db.Column(db.Integer, nullable=True)
    ingrediente=db.Column(db.Integer, nullable=True)
    proveedor=db.Column(db.Integer, nullable=True)
    
class ProductosDB(db.Model):
    """Compras account model"""
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=True)
    cantidad= db.Column(db.Float, nullable=True)
    descripccion = db.Column(db.String(100), nullable=True)
    precio= db.Column(db.Float, nullable=True)
    imagen= db.Column(LONGTEXT, nullable=False)
    estatus=db.Column(db.Integer, nullable=True)
    receta=db.Column(db.Integer, nullable=True)
    
class RecetasDB(db.Model):
    """Ingredientes account model"""
    
    __tablename__ = 'Receta'
    id_receta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad= db.Column(db.Float, nullable=False)
    estatus=db.Column(db.Integer, nullable=False)
    ingrediente=db.Column(db.Integer)


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
   
    