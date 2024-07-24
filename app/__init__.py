from flask import Flask, url_for, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Configuration
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)
    migrate.init_app(app,db)
    csrf = CSRFProtect(app)
    login_manager.init_app(app)
    login_manager.login_view = 'routes.inicio'
    
    from .models import Libro, Autor, User, AnonymousUser

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import routes as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
