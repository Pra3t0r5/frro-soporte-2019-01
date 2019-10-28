from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from flask_admin import Admin
from flask import Blueprint
from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_marshmallow import Marshmallow


DB_URI = {'local': 'mysql://cerveweb:beerjesus@localhost/cerveweb',
          'local2': 'mysql+mysqlconnector://cerveweb:beerjesus@localhost/cerveweb'
          }

FLASH_MSG = {'USU_REG_OK': 'Gracias por registrarte!',
             'USU_REG_FALLA': 'Error, Revisa los campos y reintenta.',
             'USU_REG_EXISTE': 'Error, ya existe un usuario con esos datos',
             'USU_BIENVENIDO': 'Bienvenido de nuevo',
             'USU_SALIENDO': 'Has salido de tu cuenta, vuelve pronto!',
             'NO_PERMITIDO':'Debes ingresar para ver este contenido.',
             'PED_MAIL_SENT': 'Gracias! Hemos enviado el email!',
             'PED_MAIL_FAIL': 'Lo sentimos. Fallo el envio del email.',
             'PRD_BSQ_FAIL':'No tenemos productos que coincidan con: ',
             '500': 'Se ha producido un error en el servidor, contacte al administrador.',
             '404': 'Contenido no encontrado, vuelva por donde vino.'}

db = SQLAlchemy()
ma = ''

def create_app():
    """Crea el core de la aplicacion, inicializando el ORM y los dos controladores principales (auth y main)"""

    app = Flask(__name__)

    app.debug = True
    app.config['SECRET_KEY'] = 'C3rVew38bIrR4ru1e5'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI.get('local2')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    

    
    db.init_app(app)
    with app.app_context():
        lm = LoginManager()
        lm.login_view = 'auth.login'
        lm.init_app(app)
        
        global ma
        ma = Marshmallow(app)
        #admin = Admin(app)
        #admin.init_app(app)
      

        from .models import Usuario

        @lm.user_loader
        def load_user(id):
            # since the user_id is just the primary key of our user table, use it in the query for the user
            return Usuario.query.get(int(id))
        
        @app.before_request
        def before_request():
            g.user = current_user

        # blueprint for auth routes in our app
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # blueprint for non-auth parts of app
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        db.create_all()

        return app
