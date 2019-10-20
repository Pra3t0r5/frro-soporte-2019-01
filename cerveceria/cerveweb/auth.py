import os
import traceback
from random import *

from flask import Blueprint
from flask import current_app as app
from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import FLASH_MSG, db, forms,  models
from .forms import *
from .models import Usuario

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Valida ingreso de un Usuario"""

    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('main.index'))
    formLogin = LoginUsuarioForm(request.form)
    if request.method == 'POST':
        usuarioEntrante = Usuario.query.filter_by(
            email=formLogin.email.data).first()
        if usuarioEntrante:
            if usuarioEntrante.password == formLogin.password.data:
                login_user(usuarioEntrante)
                session['logged_in'] = True
                printDatos()
                flash(FLASH_MSG.get("USU_BIENVENIDO"), 'success')
                next_pag = request.args.get('next')
                return redirect(next_pag or url_for('main.index'))
        else:
            flash(FLASH_MSG.get("USU_REG_FALLA"), 'danger')
            return render_template('login.html', form=formLogin)
    return render_template('login.html', form=formLogin)


@auth.route('/logout')
def logout():
    logout_user()
    session['logged_in'] = False
    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Crea un usuario"""

    formRegistro = RegistroUsuarioForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        mocked = randint(10, 1000)
        nuevoUsuario = Usuario(formRegistro.username.data, formRegistro.email.data,
                               formRegistro.password.data, mocked, mocked, mocked, mocked, mocked, mocked, 1)
        db.session.add(nuevoUsuario)
        db.session.commit()
        flash(FLASH_MSG.get("USU_REG_OK"), 'success')
        return redirect(url_for('auth.login'))

    else:
        return render_template('register.html', form=formRegistro)


def printDatos():
    print("<Auth-Status: [{}]>".format(g.user.is_authenticated))
    print("<Auth-Data: [{}]>".format(current_user))
