# 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
# Ciudades Argentinas y su código postal ( por lo menos 5 ciudades )
import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("CP Search")

        ciudades = {"Rosario":"2000", "Granadero Baigorria":"2152", "Salto":"2742", "Cordoba":"5000", "Mar del Plata":"7600"}
        self.treeview = ttk.Treeview(self)
        item = self.treeview.insert("", tk.END, text="Codigos Postales")
        for k in ciudades:
            subitem = self.treeview.insert(item, tk.END, text=k)
            self.treeview.insert(subitem, tk.END, text=ciudades.get(k))
        
        self.treeview.pack()

        self.pack()


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
