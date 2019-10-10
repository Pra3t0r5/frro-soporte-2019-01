from flask import Blueprint, render_template
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/contacto')
def contacto():
    return render_template('contact.html')

@auth.route("/registro", methods=['GET', 'POST'])
def register():
    form = RegistrationForm() #create an instance of RegistrationForm Class. we have given our object a name form
    if form.validate_on_submit(): # check if all form fields are valid
        flash(f'Account created for {form.username.data}!', 'success') # show an alert message to the user on screen
        return redirect(url_for('home')) # Redirect the user back to the home after successful login
    return render_template('register.html', title='Register', form=form)
