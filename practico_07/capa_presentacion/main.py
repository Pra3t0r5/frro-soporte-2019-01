import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from frro_soporte_2019_01.practico_07.capa_negocio.controlador import ControllerSocio
from frro_soporte_2019_01.practico_07.capa_datos.entidad import Socio
from frro_soporte_2019_01.practico_07.util.exceptions import DniRepetido,NoExisteDni

ctrlSocio = ControllerSocio()

def limpiar():
    for i in ventanaPrincipal.treeview.get_children():
        ventanaPrincipal.treeview.delete(i)


def mapearAForm(ventanaPrincipal):
    limpiar()
    listaSocios = ctrlSocio.get_all()
    for ls in listaSocios:
        ventanaPrincipal.treeview.insert("", tk.END, text=ls.dni, values=(ls.nombre,ls.apellido,ls.id))


def mapearDeForm(root):
    socio = Socio()
    socio.dni = root.DNI.get()
    socio.nombre = root.NOM.get()
    socio.apellido = root.APE.get()
    return socio

def alta():
    root=tk.Tk()
    root.title("Nuevo Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.dni= StringVar()
    root.nombre=StringVar()
    root.apellido=StringVar()
    root.ldni=Label(root.marco, text= "Dni del nuevo socio:")
    root.lnom=Label(root.marco, text= "Nombre:")
    root.lape=Label(root.marco, text= "Apellido:")
    root.DNI=ttk.Entry(root.marco, textvariable=root.dni)
    root.NOM=ttk.Entry(root.marco, textvariable=root.nombre)
    root.APE=ttk.Entry(root.marco, textvariable=root.apellido)
    root.bot=ttk.Button(root.marco, text="Guardar", command=lambda: cargardatos(root,mapearDeForm(root)))
    root.bot2=ttk.Button(root.marco, text="Cancelar", command=lambda: root.destroy())
    root.ldni.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.lnom.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.lape.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)
    root.DNI.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.NOM.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.APE.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
    root.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    root.bot2.grid(column=2, row=4, sticky=(E, W), padx=5, pady=5)
    root.mainloop()
def cargardatos(root,socio):
    try:
        ctrlSocio.alta(socio)
    except DniRepetido as dn:
        messagebox.showinfo("Error",dn.args)
        root.destroy()
    except:
        messagebox.showinfo("Error","Error al intentar dar de alta un nuevo socio")
        root.destroy()
    else:
        ventanaPrincipal.treeview.insert("", tk.END, text=root.DNI.get(), values=(root.NOM.get(),root.APE.get(),(ctrlSocio.get_by_dni(socio.dni)).id))
        root.destroy()

def borrardatos(root):
    try:
        ctrlSocio.baja(root.DNI.get())
    except NoExisteDni as nodni:
        messagebox.showinfo("Error",nodni.args)
        root.destroy()
    except:
        messagebox.showinfo("Error","Error al intentar dar de baja un socio")
        root.destroy()
    else:
        root.destroy()
        mapearAForm(ventanaPrincipal)


def baja():
    root=tk.Tk()
    root.title("Baja Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.dni= StringVar()
    root.ldni=Label(root.marco, text= "Dni del socio a borrar:")
    root.DNI=ttk.Entry(root.marco, textvariable=root.dni)
    root.ldni.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.DNI.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.bot=ttk.Button(root.marco, text="Eliminar", command=lambda: borrardatos(root))
    root.bot2=ttk.Button(root.marco, text="Cancelar", command=lambda: root.destroy())
    root.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    root.bot2.grid(column=2, row=4, sticky=(E, W), padx=5, pady=5)
    root.mainloop()
def modificacion():
    root=tk.Tk()
    root.title("Modificación Socio")
    root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
    root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
    root.dni= StringVar()
    root.nombre=StringVar()
    root.apellido=StringVar()
    root.ldni=Label(root.marco, text= "Dni del socio a modificar:")
    root.lnom=Label(root.marco, text= "Nombre:")
    root.lape=Label(root.marco, text= "Apellido:")
    root.DNI=ttk.Entry(root.marco, textvariable=root.dni)
    root.NOM=ttk.Entry(root.marco, textvariable=root.nombre)
    root.APE=ttk.Entry(root.marco, textvariable=root.apellido)
    root.ldni.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
    root.lnom.grid(column=0, row=2, sticky=(E, W), padx=5, pady=5)
    root.lape.grid(column=0, row=3, sticky=(E, W), padx=5, pady=5)
    root.DNI.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
    root.NOM.grid(column=1, row=2, sticky=(E, W), padx=5, pady=5)
    root.APE.grid(column=1, row=3, sticky=(E, W), padx=5, pady=5)
    root.bot=ttk.Button(root.marco, text="Aceptar", command=lambda: editardatos(root,mapearDeForm(root)))
    root.bot2=ttk.Button(root.marco, text="Cancelar", command=lambda: root.destroy())
    root.bot.grid(column=1, row=4, sticky=(E, W), padx=5, pady=5)
    root.bot2.grid(column=2, row=4, sticky=(E, W), padx=5, pady=5)
    root.mainloop()

def editardatos(root,socio):
    try:
        ctrlSocio.modificacion(socio)
    except NoExisteDni as nondni:
        messagebox.showinfo("Error",nondni.args)
        root.destroy()
    except:
        messagebox.showinfo("Error","Error al intentar modificar un socio")
        root.destroy()
    else:
        root.destroy()
        mapearAForm(ventanaPrincipal)


ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Gestión Socios")
ventanaPrincipal.marco=ttk.Frame(ventanaPrincipal, borderwidth=2, relief="raised", padding=(10,10))
ventanaPrincipal.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
ventanaPrincipal.treeview = ttk.Treeview( ventanaPrincipal.marco, height=17, columns=('dni', 'nombre', 'apellido', 'id'), selectmode=tk.BROWSE)
ventanaPrincipal.treeview.heading('#0', text='dni', anchor=tk.CENTER)
ventanaPrincipal.treeview.heading('#1', text='nombre', anchor=tk.CENTER)
ventanaPrincipal.treeview.heading('#2', text='apellido', anchor=tk.CENTER)
ventanaPrincipal.treeview.heading('#3', text='id', anchor=tk.CENTER)
ventanaPrincipal.treeview.column('#1', stretch=tk.YES, minwidth=50, width=100)
ventanaPrincipal.treeview.column('#2', stretch=tk.YES, minwidth=50, width=100)
ventanaPrincipal.treeview.column('#3', stretch=tk.YES, minwidth=50, width=100)
ventanaPrincipal.treeview.column('#0', stretch=tk.YES, minwidth=50, width=100)
ventanaPrincipal.treeview.grid(column=0, row=0, sticky=(E, W),columnspan=3, padx=5, pady=5)
ventanaPrincipal.btAlta=Button(ventanaPrincipal.marco, text="Alta", command=alta)
ventanaPrincipal.btBaja=Button(ventanaPrincipal.marco, text="Baja", command=baja)
ventanaPrincipal.btModif=Button(ventanaPrincipal.marco, text="Modificación", command=modificacion)
ventanaPrincipal.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
ventanaPrincipal.btAlta.grid(column=0, row=1, sticky=(E, W), padx=5, pady=5)
ventanaPrincipal.btBaja.grid(column=1, row=1, sticky=(E, W), padx=5, pady=5)
ventanaPrincipal.btModif.grid(column=2, row=1, sticky=(E, W), padx=5, pady=5)
mapearAForm(ventanaPrincipal)
ventanaPrincipal.mainloop()




