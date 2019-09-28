from flask import Flask, render_template

app = Flask(__name__)
#Esto es para no tener que parar y arrancar el server a cada rato
app.debug = True 



#Definicion de rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar')
def ingreso():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()