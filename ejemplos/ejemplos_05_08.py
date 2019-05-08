# manejo de excepciones
'''
#excepciones basicas
while True:
    try:
        x = int(input('escriba un nro: '))
        print(x)
        break
    except:
        print('No es un numero! Intente de nuevo.')

while True:
    try:
        y = float(input('Escriba un flotante: '))
        print(y)
        break
    except:
        print('No es un flotante! Reintente')


#ejemplo de manejo de excepciones
def divide(i, j):
    try:
        result = i / j
    except ZeroDivisionError:
        print("Division por cero!")
    else:
        print('El resultado es:', result)
    finally:
        print('al final de todo se ejecuta esto')


divide(3, 0)
divide(2, 2)
divide(1, 20)

#anidacion de errores
def accion2():
    print(1+[])

def accion1():
    try:
        accion2()
    except TypeError:
        print('excepcion disparada en accion1')
        raise #sin esto el error se lanza desde esta posicion y no de la superior

try:
    accion1()
except TypeError:
    print('Excepcion disparada en nivel superior')
  
#creacion manejadores de errores
class MiError(Exception):
    pass

def fun1():
    print("Funcion 1- levanta excepcion")
    raise MiError('Excepcion propia!!', 24)

try:
    fun1()
    print('Codigo que viene despues de fun1')
except MiError as e:
    print("Error: ", e.args)
    if e.args[1] == 25:
        print("Error nro 25")
    else: 
        print("Otro error")
  '''
  #errores de conexion a DB
  