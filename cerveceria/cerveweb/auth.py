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
    print(g)
    print(g.user.is_authenticated)
    print(current_user)
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('main.index'))
    formLogin = LoginUsuarioForm(request.form)
    if form.validate_on_submit():
        login_user(g.user)
    '''if request.method == 'POST':
        try:
            # exists = db.session.query(models.Usuario.id_usuario).filter_by(
            #    email=form.email.data).scalar() is not None
            print('ENTRA POST')
            # user = models.Usuario(
            #   email=formLogin.email.data, passw=formLogin.password.data, tipo=1)
            # print('INSTANCIADO')
            # if db.session.query(db.exists().where(db.and_(
            #    Usuario.email == formLogin.email.data,
            #    Usuario.password == formLogin.password.data))
            # ).scalar():
            usuarioEntrante = Usuario.query.filter_by(
                email=formLogin.email.data).first()
            print('INSTANCIADO')
            if usuarioEntrante:
                if usuarioEntrante.password == formLogin.password.data:
                    login_user(usuarioEntrante)
                    flash(FLASH_MSG.get("USU_BIENVENIDO"), 'success')
                    print('ENTRO')
                    next_pag = request.args.get('next')
                    return redirect(next_pag or url_for('main.index'))
            else:
                print('NO ENTRO')
                flash(FLASH_MSG.get("USU_REG_FALLA"), 'danger')
                return render_template('login.html', form=formLogin)
        except:
            print('ERROR')
            print(traceback.format_exc())
    else:'''
    return render_template('login.html', form=formLogin)

    """
    Dejo comentado esto, estaba probando a ver si andaba(reemplazaria a lo de arriba)
    @auth.route('/login', methods=['GET', 'POST'])
        def login():
                # Here we use a class of some kind to represent and validate our
                # client-side form data. For example, WTForms is a library that will
                # handle this for us, and we use a custom LoginForm to validate.
                form = LoginForm()
                if form.validate_on_submit():
                    # Login and validate the user.
                    # user should be an instance of your `User` class
                    login_user(user)

                    flask.flash('Logged in successfully.')

                    next = flask.request.args.get('next')
                    # is_safe_url should check if the url is safe for redirects.
                    # See http://flask.pocoo.org/snippets/62/ for an example.
                    if not is_safe_url(next):
                        return flask.abort(400)

                    return flask.redirect(next or flask.url_for('index'))
                return flask.render_template('login.html', form=form)
    """

@app.route('/logout')
@login_required
def logout():
    logout_user()
    if session.get('was_once_logged_in'):
        # prevent flashing automatically logged out message
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
    return redirect('auth.login')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Crea un usuario"""
    # completa objeto form con datos de la request
    formRegistro = RegistroUsuarioForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # entra al bloque a continuacion unicamente si es post y valida
    if request.method == 'POST':  # and form.validate():
        mocked = randint(10, 1000)
        # instancia objeto user con la data de la form
        nuevoUsuario = Usuario(formRegistro.username.data, formRegistro.email.data,
                               formRegistro.password.data, mocked, mocked, mocked, mocked, mocked, mocked, 1)
        # persiste modelo usuario instanciado en la db
        db.session.add(nuevoUsuario)
        db.session.commit()

        flash(FLASH_MSG.get("USU_REG_OK"), 'success')
        #formlogin = forms.LoginUsuarioForm(form.email.data)
        # envia usuario a login (testear si puede autocompletar login)
        return redirect(url_for('auth.login'))
        # flash(FLASH_MSG.get("USU_REG_FALLA"))

    else:
        return render_template('register.html', form=formRegistro)


@auth.route('/contact')
def contact():
    return render_template('contact.html')


@auth.before_request
def before_request():
    g.user = current_user

