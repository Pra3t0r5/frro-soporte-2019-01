from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login

from . import DB_URI, db, models, lm


def create_app():
    """Crea el core de la aplicacion, inicializando el ORM y los dos controladores principales (auth y main)"""
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'C3rVew38bIrR4ru1e5'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI.get('local2')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #app.config.from_object('config.Config')

    login_manager = flask_login.LoginManager()

    db.init_app(app)
    lm.init_app(app)
    
    with app.app_context():
        # blueprint for auth routes in our app
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # blueprint for non-auth parts of app
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        db.create_all()

        return app


if __name__ == '__main__':
    app = create_app()
    app.run()
