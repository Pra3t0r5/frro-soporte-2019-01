from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_URI = {'local': 'mysql://cerveweb:beerjesus@localhost/cerveweb',
          'local2': 'mysql+mysqlconnector://cerveweb:beerjesus@localhost/cerveweb'
          }
          
db = SQLAlchemy()
lm = LoginManager()

FLASH_MSG = {'USU_REG_OK': 'Gracias por registrarte!',
         'USU_REG_FALLA': 'Error, Revisa los campos y reintenta.',
         'USU_REG_EXISTE': 'Error, Revisa los campos y reintenta.',
         'USU_BIENVENIDO':'Bienvenido de nuevo',
         '500':'Se ha producido un error en el servidor, contacte al administrador.',
         '404':'Contenido no encontrado, vuelva por donde vino.'}
