from flask import Flask,render_template
from frro_soporte_2019_01.ejemploFlask.data import Articles

app= Flask(__name__)
app.debug = True #Actuliza automaticamente la pagina ante un cambio.
Articles = Articles()
@app.route('/') #Aca se define la direccion de ruta de la pagina.

def index():
    return render_template('home.html') #redireccion a una pagina html

@app.route('/about') #Aca se define la direccion de ruta a la pagina about.html.
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

if __name__ == '__main__':
    app.run()

