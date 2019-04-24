cuadrados = [x**2 for x in range(10)]

cuad_imp = [x**2 for x in range(10) if x % 2 == 1]
cuad_par = [x**2 for x in range(10) if x % 2 == 0]

print("todos", cuadrados)

# Clases

x = MiClase()  # se sobreentiende como clase porque inicia en mayuscula, por lo que no es funcion (por convencion)


def __init__(self):  # por convencion se define al inicio y las funciones llamadas dentro no necesitan ser definidas ANTES como en funcones normales
    self.datos = []


# llamada
# la instanciacion de una clase lo llama automaticamente (constructor)
__init__(self)


class Cuadrado:
    def __init__(self):
        self.lados = 4


ocuadrado = Cuadrado()
print(ocuadrado.lados)

# Clases--------------------------------------


class Auto:
    def __init__(self, color):
        self.color = color

# Herencia--------------------------------------


class Figura:
    nlados = 0

    def muestra(self):
        print(nlados)


class Cuadrado(Figura):
    def __init__(self):
        self.nlados = 4

    def muestra(self):
        Figura.muestra(self)
        print('cuadrado tiene otras cualidades')

# Metodos de Formato--------------------------------------
# El fuerte de py esta en todo lo que corre en el servidor. La interfaz nativa de python server es pobre, solo muestra textos en consola, excepto que se le anadan librerias

#Conversion a mayuscula de la primer letra
cadena = 'hola clase'
cadena.capitalize() #Hola clase
cadena.upper()
cadena.lower()
print(cadena.center(40,'=')) #centra la cadena en medio de un string de 40 iguales

# Metodos de Busqueda--------------------------------------

#cantidad de veces que aparece
coount(subcadena[,inicio,fin])
cadena = 'hola clase'
cadena.count('a')
#buscar en una subcadena

# Metodos de Validacion--------------------------------------
cadena.startswith('ho') #true
cadena.startswith('ho',3) #false
cadena.endswith(texto[ini,fin])
cadena.isalum()
#hay mas

# Metodos de Sustitucion--------------------------------------
format(*args,**kwargs) #**kwargs son estructuras cadena valor

#reemplazo de posicion, la cadena no cambia, y le pasas varios datos. 0 y 1 son placeholders
cadena = 'hola {0} que tengas un {1}'
cadena.format('Juan','buen dia')

#reemplazo por palabras clave
cadena = 'hola {nombre} que tengas un {saludo}'
cadena.format(saludo='buen dia',nombre='Juan') #deja de importar el orden

#reemplazo de texto en una cadena
#sintaxis replace.(txt a buscar, txt reemplazo)
cadena = 'hola nombre'
cadena.replace('nombre', 'joaquin') #las cadenas son inmutables, devuelve una nueva

#eliminar caracteres (x def: espacios)
strip([caracter]) #de derecha a izquierda
#hay variantes

# Metodos de Union--------------------------------------
sep = '-'
sep.join(('a','b','c')) #a-b-c

formato_nro_fac = ("N 0000-0","-0000(ID:",")")
#nro=275......................

# Metodos de Division--------------------------------------
#partition(separador)
tupla = "https://www.google.com".partition("www.")
print(tupla) #entrega lo que esta antes, el separador y lo que esta despues entre comas simples y separadas por comas
print("Protocolo:{0}\nDominio{1}".format(protocolo,dominio))
#Protocolo: http://
#Dominio: google.com

#split(separador) separa string en elementos
cadena = "libro, cuaderno, lapiz"
lista = cadena.split(',') #entrega [libro, cuaderno, lapiz]
#splitlines() separa por retorno de carro, muy bueno para procesar archivos de texto

# Metodos de Print--------------------------------------
#Metodos viejos 
#Metodos nuevos (con format)






