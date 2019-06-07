# 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
# Ciudades Argentinas y su código postal ( por lo menos 5 ciudades )
import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import *
from tkinter import ttk

root=tk.Tk()
root.title("Codigos Postales")
root.marco=ttk.Frame(root, borderwidth=2, relief="raised", padding=(10,10))
root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
root.treeview = ttk.Treeview(root.marco, selectmode=tk.BROWSE)
root.treeview = ttk.Treeview(root.marco, columns= "cp")
root.treeview.heading("#0", text="Ciudad")
root.treeview.heading("cp", text="Codigo Postal")
root.treeview.insert("", tk.END, text="Rosario", values="2000")
root.treeview.insert("", tk.END, text="Salto", values="2741")
root.treeview.insert("", tk.END, text="Cordoba", values="5000")
root.treeview.insert("", tk.END, text="Mar del Plata", values="7600")
root.treeview.insert("", tk.END, text="San Lorenzo", values="2200")
root.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
root.treeview.grid(column=0, row=0, sticky=(E, W),columnspan=3, padx=5, pady=5)
root.mainloop()
