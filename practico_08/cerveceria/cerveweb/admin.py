from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request
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

class AdminView(ModelView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        return session.get('user') == 'Administrator'

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('home', next=request.url))