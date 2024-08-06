from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  FloatField, IntegerField, SelectField, RadioField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import Autor

# Creación de Libros y Autores

class LibroForm(FlaskForm):
    titulo = StringField('Título',validators=[DataRequired()])
    genero = StringField('Género',validators=[DataRequired()])
    precio = FloatField('Precio',validators=[DataRequired()])
    cantidad = IntegerField('Cantidad',validators=[DataRequired()])
    imagen = FileField('Imagen')
    autor_id = SelectField('Autor',coerce=int,validators=[DataRequired()])
    descripcion = StringField('Descripción')
    enviar = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super(LibroForm,self).__init__(*args, **kwargs)
        self.autor_id.choices=[(autor.id, f'{autor.nombre} {autor.apellido}') for autor in Autor.query.all()]

class AutorForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido',validators=[DataRequired()])
    descripcion = StringField('Descripción')
    imagen_autor = FileField('Imagen')
    enviar = SubmitField('Guardar')

# BUSQUEDA EN EL INDEX

class SearchForm(FlaskForm):
    buscar_por_tipo = RadioField('Buscar por:', choices=[('autor','Autor'),('libro','Libro')], default='libro',validators=[DataRequired()])
    buscar_por_query = StringField('Término de búsqueda:',validators=[DataRequired()])
    enviar = SubmitField('Buscar')

# Login y Registro de usuarios

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    recuerdame = BooleanField('Recuérdame')
    enviar = SubmitField('Login')

class RegisterForm(FlaskForm):
    usuario = StringField('Usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirme Password',validators=[DataRequired(),EqualTo('password')])
    email = StringField('Email',validators=[DataRequired(),Email()])
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido',validators=[DataRequired()])
    enviar = SubmitField('Registrar')