from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db, forms, models, FLASH_MSG
from random import *


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
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
    if request.method == 'POST':
        print("paso validacion")
        # instancia objeto user con la data de la form
        user = models.Usuario(randrange(100),randrange(100),randrange(100), randrange(100) )
        print("creacion")
        # persiste modelo usuario instanciado en la db
        db.session.add(user)
        db.session.commit()    
        print("persistido")
        flash(FLASH_MSG.get("USU_REG_OK"))
        # envia usuario a login (testear si puede autocompletar login)
        return redirect(url_for('auth.login'))
    else:
        flash(FLASH_MSG.get("USU_REG_FALLA"))
    # carga register con la data presente en el form para poder editar
    return render_template('register.html', form=form)


@auth.route('/index_login')
def index_login():
    return render_template('index_login.html')
