import json
import os
import smtplib
import traceback
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText
from random import *

from flask import Blueprint
from flask import current_app as app
from flask import (flash, g, jsonify, redirect, render_template, request,
                   session, url_for)
from sqlalchemy import or_
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import FLASH_MSG, db, forms, models
from .auth import *
from .forms import *
from .models import *
from . import enconder

main = Blueprint('main', __name__)


@main.route('/')
def index():
    print("GET index")
    if request.method == "POST":

        flash("PRD_BSQ_FAIL", "warning")
        print("POST index")
    return render_template('index.html')


@main.route('/buscar', methods=['GET', 'POST'])
def buscar():
    print("GET buscar")

    if request.method == "POST":
        # Inicializacion y obtencion de request
        session['results'] = ''
        text = request.get_json(force=True)
        if text == '':
            # si entra vacia obtiene todo
            results = db.session.query(Producto).all()
        else:
            # sino, busca una coincidencia
            results = Producto.query.filter(
                or_(Producto.nombre.like(text), Producto.descripcion.like(text)))\
                .first()

            if results:
                # si encontro coincidencia, trae todas las que coincidan
                results = Producto.query.filter(
                    or_(Producto.nombre.like(text), Producto.descripcion.like(text)))\
                    .all()
            else:
                # sino retorna que no hay nada
                flash("%s%s" % (FLASH_MSG.get("PRD_BSQ_FAIL"), text), "warning")

        # Mapea el resultado de acuerdo a la clase de SQLAlchemy correspondiente
        prod_schema = ProductoSchema(many=True)
        # funciona
        session['results'] = prod_schema.dump(results)
        # no detecta variable en frontend
        jsonResults = prod_schema.dump(results)

        return jsonify(dict(redirect=url_for('main.buscar'), results=jsonResults))
    else:
        return render_template('busqueda.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


@main.route('/productos', methods=['GET', 'POST'])
@login_required
def productos():
    print("llego aca")
    if request.method == "POST":
        print("POST hijo de puta")
        text = request['cantidad']
        print(text)
    else:
        productos = db.session.query(Producto).all()
        return render_template('productos.html', productos=productos)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    contactoForm = ContactoForm(request.form)
    if request.method == 'POST':
        sendEmail("[Contacto] %s" %
                  contactoForm.contacto.data, contactoForm.mensaje.data)
        return redirect(url_for('main.index'))
    else:
        return render_template('contact.html', form=contactoForm)


@main.route('/pedidom', methods=['GET', 'POST'])
@login_required
def pedidom():
    if request.method == 'POST':
        mocked = randint(10, 1000)
        sendEmail("Gracias por tu pedido!",
                  "Tu ID de pedido es 2001%s200%s, puedes utilizarlo para consultar el estado del mismo desde nuestro sitio. Recuerda que los pedidos express se retiran en nuestros locales si no nos das mas detalles!" % (mocked*23, mocked))
        return render_template('mario.html')

    return render_template('mario.html')


def sendEmail(contacto, mensaje):
    try:
        msg = MIMEMultipart()

        password = "beerjesus"
        msg['From'] = "webmaster.cerveweb@gmail.com"
        msg['To'] = "webmaster.cerveweb@gmail.com"
        msg['CC'] = "fernando.albertengo@gmail.com, mulassimatias@gmail.com, lucaspavan.lp@gmail.com"
        msg['Subject'] = "[Cerveweb] %s" % contacto
        msg.attach(MIMEText(mensaje, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        flash(FLASH_MSG.get("PED_MAIL_SENT"), 'info')
    except:
        flash(FLASH_MSG.get("PED_MAIL_FAIL"), 'danger')
