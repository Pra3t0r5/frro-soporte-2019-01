<<<<<<< HEAD
## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(root)
        main_window.title("CP Manager")
        

        ciudades = {"Rosario":"2000", "Granadero Baigorria":"2152", "Salto":"2742", "Cordoba":"5000", "Mar del Plata":"7600"}
        self.treeview = ttk.Treeview(self)
        
        item = self.treeview.insert("", tk.END, text="Codigos Postales")
        for k in ciudades:
            subitem = self.treeview.insert(item, tk.END, text=k)
            self.treeview.insert(subitem, tk.END, text=ciudades.get(k))
        
        self.treeview.pack()

        self.pack()


root = tk.Tk()


root.resizable(width=False,height=False)
root.geometry("300x400")

btnCrear = ttk.Button(root, text="Alta",command = '')
btnBorrar = ttk.Button(root, text="Baja", command = '')
btnModificar = ttk.Button(root, text="Modificar", command = '')
btnCrear.pack(side='bottom', expand=True, padx=2, pady=2)
btnBorrar.pack(side='bottom', expand=True, padx=2, pady=2)
btnModificar.pack(side='bottom', expand=True, padx=2, pady=2)
btnCrear.place(x= 10, y= 250)
btnBorrar.place(x= 100, y= 250)
btnModificar.place(x= 190, y= 250)

app = Application(root)
app.mainloop()
=======
## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

import tkinter as tk
from tkinter import *
from tkinter import ttk


def alta():
    root=tk.Tk()
    root.title("Nueva Ciudad")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.ciudad= StringVar()
    root.cod=StringVar()
    root.nciu=Label(root.marco, text= "Ciudad:")
    root.ncp=Label(root.marco, text= "Codigo Postal:")
    root.EC=ttk.Entry(root.marco, textvariable=root.ciudad)
    root.ECod=ttk.Entry(root.marco, textvariable=root.cod)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: cargardatos(root))
    root.nciu.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.ncp.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.EC.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.ECod.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def cargardatos(root):
    ventanaPrincipal.treeview.insert("", tk.END, text=root.EC.get(), values=root.ECod.get())
    root.destroy()


def baja():
    elementoSeleccionado=ventanaPrincipal.treeview.focus()
    ventanaPrincipal.treeview.delete(elementoSeleccionado)

def modificacion():
    root=tk.Tk()
    root.title("Modificar Ciudad")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.cod=StringVar()

    root.ncp=Label(root.marco, text= "Codigo Postal:")
    root.ECod=ttk.Entry(root.marco, textvariable=root.cod)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: editar(root))

    root.ncp.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.ECod.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def editar(root):
    elementoSeleccionado=ventanaPrincipal.treeview.focus()
    ventanaPrincipal.treeview.item(elementoSeleccionado, values=root.ECod.get())
    root.destroy()

ventanaPrincipal = tk.Tk()

ventanaPrincipal.title("Codigos Postales")
ventanaPrincipal.marco=ttk.Frame(ventanaPrincipal, borderwidth=2, relief="raised", padding=(10,10))
ventanaPrincipal.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
ventanaPrincipal.treeview = ttk.Treeview(ventanaPrincipal.marco, selectmode=tk.BROWSE)
ventanaPrincipal.treeview = ttk.Treeview(ventanaPrincipal.marco, columns= "cp")
ventanaPrincipal.treeview.heading("#0", text="Ciudad")
ventanaPrincipal.treeview.heading("cp", text="Codigo Postal")
ventanaPrincipal.treeview.insert("", tk.END, text="Rosario", values="2000")
ventanaPrincipal.treeview.insert("", tk.END, text="Salto", values="2741")
ventanaPrincipal.treeview.insert("", tk.END, text="Cordoba", values="5000")
ventanaPrincipal.treeview.insert("", tk.END, text="Mar del Plata", values="7600")
ventanaPrincipal.treeview.insert("", tk.END, text="San Lorenzo", values="2200")

ventanaPrincipal.btAlta=Button(ventanaPrincipal.marco, text="Alta", command=alta)
ventanaPrincipal.btBaja=Button(ventanaPrincipal.marco, text="Baja", command=baja)
ventanaPrincipal.btModif=Button(ventanaPrincipal.marco, text="Modificación", command=modificacion)

ventanaPrincipal.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
ventanaPrincipal.treeview.grid(column=0, row=0, sticky=(E, W),columnspan=3, padx=5, pady=5)
ventanaPrincipal.btAlta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
ventanaPrincipal.btBaja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
ventanaPrincipal.btModif.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)

ventanaPrincipal.mainloop()
>>>>>>> 1d53ddfd511b8e4f6f420c3c1a04c7e0b28a0fc1
