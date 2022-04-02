from email import message
from subprocess import CalledProcessError
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField,EmailField
from wtforms.fields import PasswordField,StringField,IntegerField
from wtforms import StringField,SubmitField, IntegerField, RadioField
from wtforms.fields import PasswordField,StringField,IntegerField,SelectField,DecimalField
from wtforms import validators

class proveedoresForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    calle=StringField('Calle',
                          [validators.DataRequired(message='Ingrese un dato'),
                          validators.length(min=5, message='Ingrese un valor valido')])
    numero=IntegerField('Numero',
                        [validators.DataRequired(message='Ingrese el numero'),
                         validators.number_range(min=1, message='Ingrese un valor valido'),
                         validators.length(min=1, max=5, message='Ingrese un CP valido')])
    cp=IntegerField('Codigo Postal',
                    [validators.DataRequired(message='Ingrese el Codigo Postal'),
                     validators.length(min=5, max=5, message='Ingrese un CP valido')])
    colonia=StringField('Colonia',
                        [validators.DataRequired(message='Ingrese una colonia'),
                         validators.length(min=5, max=30, message='Ingrese una colonia valida')])
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')
    
class loginForm(FlaskForm):
    correo = EmailField('Correo de usuario',
                         [validators.DataRequired(message='Ingrese correo de usuario'),
                          validators.length(min=5, message='Inrese un correo valido')])
    password = PasswordField('Contraseña', 
                             [validators.DataRequired(message='Ingrese su password'),
                             validators.length(min=5, message='Inrese un valor valido')])
    


class EmpleadosForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    a_paterno = StringField('Apellido Paterno',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    a_materno = StringField('Apellido Materno',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    telefono = StringField('Telefono',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    correo = EmailField('Correo',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    contrasena = PasswordField('Contraseña',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    calle=StringField('Calle',
                          [validators.DataRequired(message='Ingrese un dato'),
                          validators.length(min=5, message='Ingrese un valor valido')])
    numero=IntegerField('Numero',
                        [validators.DataRequired(message='Ingrese el numero'),
                         validators.number_range(min=1, message='Ingrese un valor valido'),
                         validators.length(min=1, max=5, message='Ingrese un CP valido')])
    cp=IntegerField('Codigo Postal',
                    [validators.DataRequired(message='Ingrese el Codigo Postal'),
                     validators.length(min=5, max=5, message='Ingrese un CP valido')])
    colonia=StringField('Colonia',
                        [validators.DataRequired(message='Ingrese una colonia'),
                         validators.length(min=5, max=30, message='Ingrese una colonia valida')])
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')
    
    
class insumoForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=3, message='Inrese un valor valido')])
    Cantidad = DecimalField('Cantidad',
                            [validators.DataRequired(message='Ingrese un valor'),
                             validators.number_range(max=100)])
    unidad = SelectField('Unidad',
                         choices=[('Lt', 'Litros'), ('Kg', 'Kilogramos')])
    
    proveedor=SelectField('Proveedor',coerce=int)
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')


class RecetaForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    cantidad = DecimalField('Cantidad(n.o panquecitos)',
                            [validators.DataRequired(message='Ingrese un valor'),
                             validators.number_range(max=100)])
    ingrediente=SelectField('Ingrediente',coerce=int)
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')
    

class ComprasForm(FlaskForm):
    costo = DecimalField('Costo (Kg,Lt)',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
    cantidad = DecimalField('Cantidad',
                            [validators.DataRequired(message='Ingrese un valor'),
                             validators.number_range(max=100,message="El valor debe ser menor a 100")])
    ingrediente=SelectField('Ingrediente',coerce=int)
    
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')
    
    
class ProductosForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=3, message='Inrese un valor valido')])
    cantidad = DecimalField('Cantidad',
                            [validators.DataRequired(message='Ingrese un valor'),
                             validators.number_range(max=100)])
    descripcion = StringField('Descripcion',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=3, message='Inrese un valor valido')])
    precio = DecimalField('Precio',
                            [validators.DataRequired(message='Ingrese un valor'),
                             validators.number_range(max=100)])
    receta=SelectField('Receta',coerce=int)
    
    hornear=SelectField('Cantidad',
                        choices=[(6,'Media Docena'),(12,'Docena')])
    
    busqueda=StringField('Busqueda')
    submit=SubmitField('Guardar')