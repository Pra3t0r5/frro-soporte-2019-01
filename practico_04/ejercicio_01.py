## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *
from tkinter import ttk, font, messagebox


def suma():
    n1 = float(oper1.get())
    n2 = float(oper2.get())
    suma = n1 + n2
    messagebox.showinfo("Resultado Suma", "El resultado de la suma es: %.2f" % suma)


def resta():
    n1 = oper1.get()
    n2 = oper2.get()
    resta = n1 - n2
    messagebox.showinfo("Resultado Resta", "El resultado de la resta es %.2f" % resta)
def multiplicacion():
    n1 = oper1.get()
    n2 = oper2.get()
    multiplicacion = n1 * n2
    messagebox.showinfo("Resultado Multiplicación", "El resultado de la multiplicacion es: %.2f" % multiplicacion)

def division():
    try:
        n1 = oper1.get()
        n2 = oper2.get()
        division = n1/ n2
    except ZeroDivisionError:
        messagebox.showinfo("Error de entrada", "No es posible la división por cero")
    else:
        messagebox.showinfo("Resultado Division", "El resultado de la division es: %.2f" % division)


root = Tk()
root.resizable(width=False,height=False)
root.title("Calculadora")
root.geometry("500x180")
fuente = font.Font(weight='bold')
oper1 = DoubleVar()
oper2 = DoubleVar()
entry1 = Entry(root, textvariable = oper1, width=10)
entry2 = Entry(root, textvariable = oper2, width=10)
label1 = Label(root, text="Primer operando", font= fuente)
label2 = Label(root, text="Segundo Operando", font= fuente)
botonSuma = ttk.Button(root, text="+",command=suma)
botonResta = ttk.Button(root, text="-",command=resta)
botonMultiplicación = ttk.Button(root, text="x",command= multiplicacion)
botonDivision = ttk.Button(root, text="/",command= division)
label1.pack(side=LEFT, expand=True, padx=2, pady=2)
entry1.pack(side=LEFT, expand=True, padx=2, pady=2)
label2.pack(side=LEFT, expand=True, padx=2, pady=2)
entry2.pack(side=LEFT, expand=True, padx=2, pady=2)
botonSuma.place(x= 10, y= 150)
botonResta.place(x= 100, y= 150)
botonMultiplicación.place(x= 190, y= 150)
botonDivision.place(x= 280, y= 150)
root.mainloop()




