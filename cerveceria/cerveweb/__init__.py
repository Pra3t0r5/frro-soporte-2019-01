from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = {'local': 'mysql://cerveweb:beerjesus@localhost/cerveweb',
          'remote': 'mysql://cerveweb:beerjesus@localhost/cerveweb'
          }
db = SQLAlchemy()
