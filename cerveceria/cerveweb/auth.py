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

    #Si el usuario ya esta logueado redirije a index
    if g.user is not None and g.user.is_authenticated:        
        return redirect(url_for('main.index'))
    #al recibir un GET, instancia el formulario para poder renderizarlo
    form = LoginUsuarioForm(request.form)    
    if request.method == 'POST':
        #al recibir un POST (submit) evalua los validadores del form, si no pasan avisa
        if not form.validate_on_submit():
            flash(FLASH_MSG.get("USU_REG_FALLA"), 'danger')
            return render_template('login.html', form=form)
        #en este punto se recibio un form valido, se procede a buscar el usuario
        usuarioEntrante = Usuario.query.filter_by(
            email=form.email.data).first()
        if usuarioEntrante:
            #el usuario existe, se procede a validar sus datos
            if usuarioEntrante.password == form.password.data:
                login_user(usuarioEntrante)
                session['logged_in'] = True
                printDatos()
                flash(FLASH_MSG.get("USU_BIENVENIDO"), 'success')
                next_pag = request.args.get('next')
                return redirect(next_pag or url_for('main.index'))
        else:
            #el usuario no existe, avisa
            flash(FLASH_MSG.get("USU_REG_FALLA"), 'danger')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)



@auth.route('/logout')
def logout():
    logout_user()
    session['logged_in'] = False
    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']
    flash(FLASH_MSG.get("USU_SALIENDO"), 'warning')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Crea un usuario"""

    form = RegistroUsuarioForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        nuevoUsuario = Usuario(form.username.data, form.email.data,
                               form.password.data, form.nombre.data,
                               form.apellido.data, form.cuit.data,
                               True, form.dni.data, form.razon.data, 1)
        db.session.add(nuevoUsuario)
        db.session.commit()
        flash(FLASH_MSG.get("USU_REG_OK"), 'success')
        return redirect(url_for('auth.login'))

    else:
        return render_template('register.html', form=form)


def printDatos():
    print("<Auth-Status: [{}]>".format(g.user.is_authenticated))
    print("<Auth-Data: [{}]>".format(current_user))
