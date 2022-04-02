from email import message
from subprocess import CalledProcessError
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField,EmailField
from wtforms.fields import PasswordField,StringField,IntegerField
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
    
from wtforms import validators

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