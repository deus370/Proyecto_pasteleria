import os
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig

db = SQLAlchemy()
from .modelos import Usuario, Rol, ProveedoresDB

userDataStore = SQLAlchemyUserDatastore(db, Usuario, Rol)

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    #Registramos el blueprint para las rutas
    from .Proveedor.views import Proveedor
    app.register_blueprint(Proveedor)
    
    from .Insumos.views import Insumo
    app.register_blueprint(Insumo)
    
    from .Compra.views import Compra
    app.register_blueprint(Compra)
    
    from .Receta.views import Receta
    app.register_blueprint(Receta)
    
    from .Producto.views import Producto
    app.register_blueprint(Producto)
    
    from .Empleado.views import Empleado
    app.register_blueprint(Empleado)
    
    from .Inicio.views import Inicio
    app.register_blueprint(Inicio)
    
    from .login.views import Login
    app.register_blueprint(Login)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    #Definimos la ruta a la BD: mysql://user:password@localhost/bd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pasteleria'
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
    app.config['SECURITY_PASSWORD_SALT'] = 'thisissecretsalt'

    #Inicializamos y creamos la BD
    db.init_app(app)
    @app.before_first_request
    def create_all():
        db.create_all()

    #Conectando los modelos a fask-security usando SQLAlchemyUserDatastore
    security = Security(app, userDataStore)
    
    return app