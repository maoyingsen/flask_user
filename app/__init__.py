from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
# create the db object before app object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mys3326999@localhost/test'
    app.config['SECRET_KEY'] = 'mysecret'
    # create the db first and init the app with the db beforehand later
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    # the import has to be put below becasue db has to be created first
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app