import tkinter as tk
from tkinter import *
from tkinter import ttk


def alta():
    root=tk.Tk()
    root.title("Nueva Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.dni= StringVar()
    root.nombre=StringVar()
    root.apellido=StringVar()
    root.ldni=Label(root.marco, text= "Dni:")
    root.lnom=Label(root.marco, text= "Nombre:")
    root.lape=Label(root.marco, text= "Apellido:")
    root.DNI=ttk.Entry(root.marco, textvariable=root.dni)
    root.NOM=ttk.Entry(root.marco, textvariable=root.nombre)
    root.APE=ttk.Entry(root.marco, textvariable=root.apellido)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: cargardatos(root))
    root.ldni.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.lnom.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.lape.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)
    root.DNI.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.NOM.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.APE.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def cargardatos(root):
    ventanaPrincipal.treeview.insert("", tk.END, text=root.EC.get(), values=root.ECod.get())
    root.destroy()


def baja():
    elementoSeleccionado=ventanaPrincipal.treeview.focus()
    ventanaPrincipal.treeview.delete(elementoSeleccionado)

def modificacion():
    root=tk.Tk()
    root.title("Modificar Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.dni=StringVar()

    root.nDNI=Label(root.marco, text= "DNI:")
    root.EDNI=ttk.Entry(root.marco, textvariable=root.dni)
    root.bot=ttk.Button(root.marco, text="Buscar", command=lambda: editar(root))

    root.nDNI.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.EDNI.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def editar(root):
    elementoSeleccionado=ventanaPrincipal.treeview.focus()
    ventanaPrincipal.treeview.item(elementoSeleccionado, values=root.ECod.get())
    root.destroy()

ventanaPrincipal = tk.Tk()

ventanaPrincipal.title("Gestión Socios")
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
