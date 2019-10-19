from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_URI = {'local': 'mysql://cerveweb:beerjesus@localhost/cerveweb',
          'local2': 'mysql+mysqlconnector://cerveweb:beerjesus@localhost/cerveweb'
          }

db = SQLAlchemy()
lm = LoginManager()

FLASH_MSG = {'USU_REG_OK': dict(message='Gracias por registrarte!', category='info'),
             'USU_REG_FALLA': dict(message='Error, Revisa los campos y reintenta.', category='warning'),
             'USU_REG_EXISTE': dict(message='Error, ya existe un usuario con esos datos', category='warning'),
             'USU_BIENVENIDO': dict(message='Bienvenido de nuevo', category='success'),
             'PED_MAIL_SENT': dict(message='Gracias! Enviamos una copia de tu pedido a tu email', category='sucess'),
             '500': dict(message='Se ha producido un error en el servidor, contacte al administrador.', category='error'),
             '404': dict(message='Contenido no encontrado, vuelva por donde vino.', category='error')}
