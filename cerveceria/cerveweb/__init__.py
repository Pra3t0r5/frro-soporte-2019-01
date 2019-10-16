from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = {'local': 'mysql://cerveweb:beerjesus@localhost/cerveweb',
          'local2': 'mysql+mysqlconnector://cerveweb:beerjesus@localhost/cerveweb'
          }
          
db = SQLAlchemy()

FLASH_MSG = {'USU_REG_OK': 'Gracias por registrarte!',
         'USU_REG_FALLA': 'Error, Revisa los campos y reintenta.',
         'USU_BIENVENIDO':'Bienvenido de nuevo'}
