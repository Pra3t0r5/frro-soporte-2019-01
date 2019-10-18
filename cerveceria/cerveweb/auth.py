import os
import traceback
from random import *

from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import FLASH_MSG, db, forms, login_manager, models
from .forms import *
from .models import Usuario, db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Valida ingreso de un Usuario"""
    formLogin = LoginUsuarioForm(request.form)
    if request.method == 'POST':
        try:
            # exists = db.session.query(models.Usuario.id_usuario).filter_by(
            #    email=form.email.data).scalar() is not None
            print('ENTRA POST')
            #user = models.Usuario(
            #   email=formLogin.email.data, passw=formLogin.password.data, tipo=1)
            print('INSTANCIADO')
            if db.session.query(db.exists().where(db.and_(
                Usuario.email == formLogin.email.data,
                Usuario.password == formLogin.password.data))
            ).scalar():
                flash(FLASH_MSG.get("USU_BIENVENIDO"))
                print('EXISTE')
                return redirect(url_for('main.index'))
            else:
                print('NO EXISTE')
                flash(FLASH_MSG.get("USU_REG_FALLA"))
                return render_template('login.html', form=formLogin)
        except:
            print('ERROR')
            print(traceback.format_exc())            
    else:
        return render_template('login.html',form=formLogin)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Crea un usuario"""
    # completa objeto form con datos de la request
    formRegistro = RegistroUsuarioForm(request.form)
    # entra al bloque a continuacion unicamente si es post y valida
    if request.method == 'POST':  # and form.validate():
        mocked = randint(10, 1000)
        # instancia objeto user con la data de la form
        nuevoUsuario = Usuario(formRegistro.username.data, formRegistro.email.data,
                              formRegistro.password.data, mocked, mocked, mocked, mocked, mocked, mocked, 1)

        # persiste modelo usuario instanciado en la db
        db.session.add(nuevoUsuario)
        db.session.commit()

        flash(FLASH_MSG.get("USU_REG_OK"))
        #formlogin = forms.LoginUsuarioForm(form.email.data)
        # envia usuario a login (testear si puede autocompletar login)
        return redirect(url_for('auth.login'))
        # flash(FLASH_MSG.get("USU_REG_FALLA"))

    else:
        return render_template('register.html', form=formRegistro)


@auth.route('/contact')
def contact():
    return render_template('contact.html')
