from tkinter import *
#from filtro1 import filtro1
#from filtro2 import filtro2
#from filtro3 import filtro3

window = Tk()

window.title("Menu de Filtros")

window.geometry('400x300')

lbl = Label(window, text="Ingresa el nombre de la imagen")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():
   
    nombre = txt.get()
    numero = 3
    lbl.configure(text= "Selecciona uno de los filtros de abajo")
    boton_filtro1 = Button(window, text="Filtro 1", command=lambda: filtro1(nombre))
    boton_filtro1.grid(column=0, row=1)

    boton_filtro2 = Button(window, text="Filtro 2", command=lambda: filtro2(nombre))
    boton_filtro2.grid(column=0, row=2)

    boton_filtro3 = Button(window, text="Filtro 3", command=lambda: filtro3(nombre))
    boton_filtro3.grid(column=0, row=3)
 
btn = Button(window, text="Ok", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()