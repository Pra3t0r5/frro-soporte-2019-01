# Escriba ahora el programa de modo que almacene los números que el usuario introduzca
# en una lista y usa las funciones max() y min() para calcular los numeros maximos y minimos despues
# de que el bucle termine.


import sys
lista = []
maximo = 0
minimo = 0
numero = input("Ingrese un numero: ")

while numero != "fin":
    lista.append(float(numero))
    numero = input("Ingrese un numero: ")

if (numero == "fin") and (not lista):
    print("No hay numeros ingresados")
    sys.exit() #Termina el programa.

maximo = max(lista)
minimo = min(lista)
print("Maximo : ", maximo,"\nMinimo: ", minimo)
