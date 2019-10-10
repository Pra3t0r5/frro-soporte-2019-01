from flask import Blueprint, render_template
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/contact')
def contact():
    return render_template('contact.html')

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/index_login')
def index_login():
    return render_template('index_login.html')
