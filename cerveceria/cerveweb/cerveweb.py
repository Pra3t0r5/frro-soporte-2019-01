from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import DB_URI, db

# init SQLAlchemy para poder usarlo en todos los demas modelos


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI.get('local')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
