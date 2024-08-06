from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# Clase Usuario
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    usuario = db.Column(db.String(50),nullable=False,unique=True)
    password_hash = db.Column(db.Text)
    nombre = db.Column(db.String(50),nullable=False)
    apellido =  db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f'Usuario: {self.usuario}'
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

# Clase Anónima
class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.usuario = 'anonimo'

# Clase Autor
class Autor(db.Model):
    id =  db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)
    apellido =  db.Column(db.String(50),nullable=False)
    descripcion = db.Column(db.Text,default='Sin descripción')
    imagen_autor = db.Column(db.String,default='Sin imagen')
    libros = db.relationship('Libro',backref='autor',lazy=True)

# Clase Libro
class Libro(db.Model):
    id =  db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(200),nullable=False)
    genero = db.Column(db.String(100),nullable=False)
    precio = db.Column(db.Float,default=0)
    cantidad = db.Column(db.Integer,default=0)
    imagen_url = db.Column(db.String,default='Sin imagen')
    descripcion = db.Column(db.Text,default='Sin descripción')
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)