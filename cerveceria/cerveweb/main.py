import os
import traceback
from random import *

from flask import Blueprint
from flask import current_app as app
from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import FLASH_MSG, db, forms, models
from .forms import *
from .models import Usuario
from .auth import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


@main.route('/productos')
@login_required
def productos():
    return render_template('productos.html')


@main.route('/pedidom')
@login_required
def pedidom():
    if request.method == 'POST':
        mocked = randint(10, 1000)
        flash(FLASH_MSG.get("PED_MAIL_SENT"), 'info')

    return render_template('mario.html')
