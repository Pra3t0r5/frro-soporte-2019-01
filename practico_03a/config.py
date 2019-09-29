import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
