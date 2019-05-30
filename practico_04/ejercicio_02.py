## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import *
from tkinter import ttk, messagebox

def cero():
    tx =entry1.get()
    entry1.set(tx+'0')
def uno():
    tx= entry1.get()
    entry1.set(tx+'1')
def dos():
    tx=entry1.get()
    entry1.set(tx+'2')
def tres():
    tx=entry1.get()
    entry1.set(tx+'3')
def cuatro():
    tx=entry1.get()
    entry1.set(tx+'4')
def cinco():
    tx=entry1.get()
    entry1.set(tx+'5')
def seis():
    tx=entry1.get()
    entry1.set(tx+'6')
def siete():
    tx=entry1.get()
    entry1.set(tx+'7')
def ocho():
    tx=entry1.get()
    entry1.set(tx+'8')
def nueve():
    tx=entry1.get()
    entry1.set(tx+'9')

def suma():
    tx=entry1.get()
    entry1.set(tx+'+')
def resta():
    tx=entry1.get()
    entry1.set(tx+'-')
def division():
    tx=entry1.get()
    entry1.set(tx+'/')
def multiplicacion():
    tx = entry1.get()
    entry1.set(tx+'*')

def igual():
    tx = entry1.get()
    if any(c.isalpha() for c in tx):
        messagebox.showinfo("Error", "Error de entrada")
        clean()
    else:
        entry1.set(eval(tx))


def clean():
    entry1.set(str())

root = Tk()
root.resizable(width=False,height=False)
root.title("Calculadora")
root.geometry("400x300")

entry1 = StringVar()
cadenaEntrada= Entry(root, textvariable = entry1, width=50)
boton0 = ttk.Button(root, text="0",command = cero)
boton1 = ttk.Button(root, text="1", command = uno)
boton2 = ttk.Button(root, text="2", command = dos)
boton3 = ttk.Button(root, text="3", command = tres)
boton4 = ttk.Button(root, text="4",command = cuatro)
boton5 = ttk.Button(root, text="5", command = cinco)
boton6 = ttk.Button(root, text="6", command = seis)
boton7 = ttk.Button(root, text="7", command = siete)
boton8 = ttk.Button(root, text="8", command = ocho)
boton9 = ttk.Button(root, text="9", command = nueve)
botonSuma = ttk.Button(root, text="+",command = suma )
botonResta = ttk.Button(root, text="-", command = resta)
botonMultiplicacion = ttk.Button(root, text="x", command = multiplicacion)
botonDivision = ttk.Button(root, text="/", command = division)
botonIgual= ttk.Button(root, text="=",width=25, command = igual)
botonC= ttk.Button(root, text="C",width=25, command = clean)
cadenaEntrada.place(x=10, y=40)
boton7.place(x=10, y=70)
boton8.place(x=100, y=70)
boton9.place(x=190, y=70)
boton4.place(x=10, y=120)
boton5.place(x=100, y=120)
boton6.place(x=190, y=120)
boton1.place(x=10, y=170)
boton2.place(x=100, y=170)
boton3.place(x=190, y=170)
boton0.place(x=10, y=220)
botonSuma.place(x=280, y= 70)
botonResta.place(x=280, y= 120)
botonMultiplicacion.place(x=280, y= 170)
botonDivision.place(x=280, y= 220)
botonIgual.place(x= 100, y=220)
botonC.place(x= 100, y = 270)

root.mainloop()




