from flask import render_template, redirect, url_for, flash, Blueprint,request
from flask_login import login_required, current_user, login_user, logout_user
from .forms import LibroForm, AutorForm, SearchForm,LoginForm, RegisterForm

from .models import Libro,Autor, db, AnonymousUser,User

routes = Blueprint('routes', __name__)

# ******************************************************************
# ************************ RUTAS LOGIN *****************************
# ******************************************************************

@routes.route('/login_inicio')
def inicio():
    if not current_user.is_authenticated:   
        return render_template('base_template.html')
    return redirect(url_for('routes.index'))

# Ruta de Login
@routes.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(usuario=form.usuario.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=form.recuerdame.data)
            flash('Inicio de sesión exitosa!','success')
            return redirect(url_for('routes.index'))
        else:
            flash('Inicio de sesión fallida. Por favor revisa tus credenciales.','warning')
    return render_template('auth/login.html',form=form)


# Ruta de Registro
@routes.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        usuario = form.usuario.data
        email = form.email.data
        if User.query.filter_by(usuario=usuario).first() or User.query.filter_by(email=email).first():
            flash('Los valores introducidos ya se encuentran en uso, por favor intente con otro','warning')
        else:
            new_user = User(
                usuario=usuario,
                email=email,
                nombre=form.nombre.data,
                apellido=form.apellido.data
            )
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario registrado satisfactoriamente','success')
            return redirect(url_for('routes.login'))
    return render_template('auth/register.html',form=form)


# Ruta de Cierre de Sesion
@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Cierre de sesión exitosa!','success')
    return redirect(url_for('routes.inicio'))

# Ruta de Ingreso como Usuario Anónimo
@routes.route('/anonymous')
def anonymous():
    anonymous_user = User.query.filter_by(usuario='Anonimo').first()
    if anonymous_user:
        login_user(anonymous_user)
        flash('Has ingresado como usuario anónimo.','info')
        return redirect(url_for('routes.index'))
    else:
        flash('No se encuentra el usuario anónimo, por favor contacte con el administrador','warning')
        return redirect(url_for('routes.inicio'))


# ******************************************************************
# ************************ CRUD LIBROS *****************************
# ******************************************************************


@routes.route('/')
@login_required
def index():
    # En pantalla me mostraría los 10 primeros libros y los 10 primeros autores
    libros = Libro.query.order_by(Libro.titulo).limit(10).all()
    autores = Autor.query.order_by(Autor.nombre).limit(10).all()
    return render_template('index.html',libros=libros,autores=autores)

# CRUD de libros
# Inicio

@routes.route('/libros',methods=['GET','POST'])
@login_required
def inicio_libro():
    page = request.args.get('page',1,type=int)
    libros_paginacion = Libro.query.order_by(Libro.titulo).paginate(page=page,per_page=10)
    return render_template('libros.html',libros_paginacion=libros_paginacion)


@routes.route('/nuevo_libro',methods=['GET','POST'])
@login_required
def nuevo_libro():
    libro = Libro()
    libroform = LibroForm(obj=libro)
    if current_user.is_authenticated and not current_user.is_anonymous:
        if libroform.validate_on_submit():
            libro.titulo = libroform.titulo.data
            libro.genero = libroform.genero.data
            libro.precio = libroform.precio.data
            libro.cantidad = libroform.cantidad.data
            libro.autor_id = libroform.autor_id.data
            db.session.add(libro)
            db.session.commit()
            flash('Libro guardado exitosamente!','success')
            return redirect(url_for('routes.inicio_libros'))
    return render_template('nuevo_libro.html',libroform=libroform)

@routes.route('/detalle_libro/<int:id>',methods=['GET'])
def detalle_libro(id):
    libro = Libro.query.get_or_404(id)
    return render_template('detalle_libro.html',libro=libro)

@routes.route('/editar_libro/<int:id>',methods=['GET','POST'])
@login_required
def editar_libro():
    libro = Libro.query.get_or_404(id)
    libroForm = LibroForm(obj=libro)
    if current_user.is_authenticated and not current_user.is_anonymous:
        if libroForm.validate_on_submit():
            libro.titulo = libroForm.titulo.data
            libro.genero = libroForm.genero.data
            libro.precio = libroForm.precio.data
            libro.cantidad = libroForm.cantidad.data
            libro.autor_id = libroForm.autor_id.data
            db.session.add(libro)
            db.session.commit()
            flash('Libro actualizado exitosamente!','success')
            return redirect(url_for('routes.inicio_libros'))
    return render_template('nuevo_libro.html',libroform=libroForm)

@routes.route('/eliminar_libro/<int:id>',methods=['GET','POST'])
@login_required
def eliminar_libro():
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    flash('Libro eliminado exitosamente!','success')
    return redirect(url_for('routes.inicio_libros'))

# ******************************************************************
# ************************ CRUD LIBROS *****************************
# ******************************************************************

@routes.route('/autores')
@login_required
def inicio_autor():
    autor = Autor.query.order_by(Autor.nombre).limit(10).all()
    return render_template('autores.html',autor=autor)

@routes.route('/nuevo_autor',methods=['GET','POST'])
@login_required
def nuevo_autor():
    if current_user.is_authenticated and not current_user.is_anonymous:
        flash('Hola')
    else:
        flash('No podes acceder')
