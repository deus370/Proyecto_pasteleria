from email import message
from subprocess import CalledProcessError
from flask_wtf import FlaskForm
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
    
class insumoForm(FlaskForm):
    nombre = StringField('Nombre',
                         [validators.DataRequired(message='Ingrese un datos'),
                          validators.length(min=5, message='Inrese un valor valido')])
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
    cantidad = DecimalField('Cantidad',
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

<<<<<<< HEAD
=======
    
>>>>>>> 002f3dc208a38aa70feef7e7e1d4fc107f1fec17
