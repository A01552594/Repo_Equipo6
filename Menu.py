from tkinter import *
from filtro import outline
#Tambien se importaran en las versiones mas actualizadas los demas filtros

window = Tk()

window.title("Menu de Filtros")

window.geometry('400x300')

lbl = Label(window, text="Ingresa el nombre de la imagen")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():
   
    nombre = txt.get()
    
    lbl.configure(text= "Selecciona uno de los filtros de abajo")
    boton_filtro1 = Button(window, text="Blur", command=lambda: outline(nombre,1))
    boton_filtro1.grid(column=0, row=1)

    boton_filtro2 = Button(window, text="Bottom Solbel", command=lambda: filtro2(nombre,2))
    boton_filtro2.grid(column=0, row=2)

    boton_filtro3 = Button(window, text="Emboss", command=lambda: filtro3(nombre,3))
    boton_filtro3.grid(column=0, row=3)

    boton_filtro4 = Button(window, text="Left Sobel", command=lambda: filtro3(nombre,4))
    boton_filtro4.grid(column=0, row=4)

    boton_filtro5 = Button(window, text="Outline", command=lambda: filtro3(nombre,5))
    boton_filtro5.grid(column=0, row=5)

    boton_filtro6 = Button(window, text="Night Sobel", command=lambda: filtro3(nombre,6))
    boton_filtro6.grid(column=0, row=6)

    boton_filtro7 = Button(window, text="Sharpen", command=lambda: filtro3(nombre,7))
    boton_filtro7.grid(column=0, row=7)

    boton_filtro8 = Button(window, text="Top Sobel", command=lambda: filtro3(nombre,8))
    boton_filtro8.grid(column=0, row=8)
 
btn = Button(window, text="Ok", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()

