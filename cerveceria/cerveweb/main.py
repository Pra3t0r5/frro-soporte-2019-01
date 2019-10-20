import os
import traceback
import smtplib
from random import *

from flask import Blueprint
from flask import current_app as app
from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText


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


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contactoForm = ContactoForm(request.form)
        sendEmail("[Contacto] %s" %
                  contactoForm.contacto.data, contactoForm.mensaje.data)
        return redirect(url_for('main.index'))
    else:
        return render_template('contact.html')


@main.route('/pedidom', methods=['GET', 'POST'])
@login_required
def pedidom():
    if request.method == 'POST':
        mocked = randint(10, 1000)
        sendEmail("Gracias por tu pedido!",
                  "Tu ID de pedido es %s, puedes utilizarlo para consultar el estado del mismo desde nuestro sitio. Recuerda que los pedidos express se retiran en nuestros locales si no nos das mas detalles!" % mocked)
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
