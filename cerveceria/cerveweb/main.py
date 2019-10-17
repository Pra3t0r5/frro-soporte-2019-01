from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db, forms, models, FLASH_MSG
from random import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
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
    if request.method == 'POST':  # and form.validate():
        mocked = randint(10, 1000)
        # instancia objeto user con la data de la formx
        pedido = models.Pedido(form.username.data, form.email.data,
                           form.password.data,21, 21, 21, 21, 21, 21, 1)
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
    
    return render_template('mario.html')
