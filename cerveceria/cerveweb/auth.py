from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db, forms, models, FLASH_MSG


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
    #completa objeto form con datos de la request
    form = forms.RegistroUsuarioForm(request.form)
    #entra al bloque a continuacion unicamente si es post y valida
    if request.method == 'POST' and form.validate():
        #instancia objeto user con la data de la form
        user = models.User(form.username.data, form.email.data,
                           form.password.data)
        #persiste modelo usuario instanciado en la db                   
        if models.crear(user):
            flash(FLASH_MSG.get("USU_REG_OK"))
            return redirect(url_for('login')) #envia usuario a login (testear si puede autocompletar login)
        else:
            flash(FLASH_MSG.get("USU_REG_FALLA"))        
    return render_template('register.html', form=form) #carga register con la data presente en el form para poder editar


@auth.route('/index_login')
def index_login():
    return render_template('index_login.html')
