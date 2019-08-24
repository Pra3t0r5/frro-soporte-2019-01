# a) Reescriba el programa que pide al usuario una lista de numeros e imprime en pantalla el maximo y minimo de
# los numeros introducidos al final, cuando el usuario introduce "fin".

lista = []
maximo = 0
minimo = 0
numero = input("Ingrese un numero: ")

while numero != "fin":
    lista.append(float(numero))
    maximo = max(lista)
    minimo = min(lista)
    numero = input("Ingrese un numero: ")

if (numero == "fin") and (not lista):
    print("No hay numeros ingresados")
else:
    print("Maximo : ", maximo,"\nMinimo: ", minimo)
