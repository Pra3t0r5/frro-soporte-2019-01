from flask import Flask

app= Flask(__name__)
app.debug = True #Actuliza automaticamente la pagina ante un cambio.
@app.route('/') #Aca se define la direccion de ruta de la pagina'''
def index():
    return "Hello Word!!!"

if __name__ == '__main__':
    app.run()



