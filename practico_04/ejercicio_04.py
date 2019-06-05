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