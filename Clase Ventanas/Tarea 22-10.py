#Desarrolle una app que conatruya la sig ventana

from tkinter import *

ventana= Tk()

ventana.title("Ventana Azul")
ventana.geometry("300x500")
#no deja que se modifique el tamaño de la ventana
ventana.resizable(False, False)
ventana.config(background="SlateBlue3")
ventana.mainloop()