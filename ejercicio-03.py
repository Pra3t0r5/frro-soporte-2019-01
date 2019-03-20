#Definir una funcion que calcule la longitud de una lista o una cadena dada

cadena= "Hola Mundo"
array= ["Matías","Lucas",3,"Fernando"]

def longitud(cad):
    return len(cad)

assert(longitud(cadena)==10)
assert(longitud(array)==4)
