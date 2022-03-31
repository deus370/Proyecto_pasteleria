from . import db
from flask_sqlalchemy import SQLAlchemy
#Importamos las clases UserMixin y RoleMixin de flask_security
from flask_security import UserMixin, RoleMixin
from sqlalchemy.dialects.mysql import DOUBLE

users_roles = db.Table('users_roles',
    db.Column('userId', db.Integer, db.ForeignKey('user.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    """User account model"""
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role',
        secondary=users_roles,
        backref= db.backref('users', lazy='dynamic'))

class Role(RoleMixin, db.Model):
    """Role model"""

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description =  db.Column(db.String(255))


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
    
class IngredientesDB(db.Model):
    """Ingredientes account model"""
    
    __tablename__ = 'Ingrediente'
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad= db.Column(db.Float, nullable=False)
    unidad=db.Column(db.String, nullable=False)
    proveedor=db.Column(db.Integer, nullable=False)
   
    