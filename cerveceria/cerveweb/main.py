from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db, forms, models, FLASH_MSG
from random import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    flash(FLASH_MSG.get("USU_BIENVENIDO"))
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/admin')
def admin():
    return render_template('admin.html')

@main.route('/productos')
def productos():
    return render_template('productos.html')

@main.route('/pedidom')
def pedidom():   
    if request.method == 'POST':
        mocked = randint(10, 1000)
        flash(FLASH_MSG.get("PED_MAIL_SENT"))
            
    return render_template('mario.html')
