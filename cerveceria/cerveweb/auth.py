from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db, forms, models, FLASH_MSG
from random import *

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """Valida ingreso de un Usuario"""
    form = forms.LoginUsuarioForm(request.form)
    if request.method == 'POST':  # and form.validate():

        try:
            #exists = db.session.query(models.Usuario.id_usuario).filter_by(
            #    email=form.email.data).scalar() is not None
            if db.session.query(exists().where(and_(
                models.Usuario.email == form.email.data,
                models.Usuario.password == form.password.data))
            ).scalar():
                flash(FLASH_MSG.get("USU_BIENVENIDO"))
                return redirect(url_for('main.index'))
        except:
            # carga register con la data presente en el form para poder editar
            flash(FLASH_MSG.get("USU_REG_FALLA"))
            return render_template('register.html', form=form)

    return render_template('login.html')


@auth.route('/contact')
def contact():
    return render_template('contact.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Crea un usuario"""
    # completa objeto form con datos de la request
    form = forms.RegistroUsuarioForm(request.form)
    # entra al bloque a continuacion unicamente si es post y valida
    if request.method == 'POST':  # and form.validate():
        mocked = randint(10, 1000)
        # instancia objeto user con la data de la form
        user = models.Usuario(form.username.data, form.email.data,
                              form.password.data, mocked, mocked, mocked, mocked, mocked, mocked, mocked, 1)
        # persiste modelo usuario instanciado en la db
        try:
            db.session.add(user)
            db.session.commit()
            flash(FLASH_MSG.get("USU_REG_OK"))
            # envia usuario a login (testear si puede autocompletar login)
            return redirect(url_for('auth.login'))
        except:
            # carga register con la data presente en el form para poder editar
            flash(FLASH_MSG.get("USU_REG_FALLA"))
            return render_template('register.html', form=form)
    else:
        return render_template('register.html')
