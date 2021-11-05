import tkinter as tk
#from PIL import Image, ImageTk
from tkinter import * 
import os, sys
import transiciones
import cinta
#Funciones
listaFinal=[]
def iniciar():
    limpiar()
    global listaFinal
    wl=['#']
    #print(cadena.get())
    for i in list(cadena.get()):
        wl.append(i)
        if(i!='a' and i!='b' and i!='c'):
            etiqueta3 = tk.Label(text="---------CADENA INVALIDA :(----------", font=("Arial", 10), fg='#FF0000')
            etiqueta3.place(x=80, y=200)
            listaFinal=['Cadena Invalida, '
                        'introducir solo las letras : a b c']
            return 0
        
    wl.append('#')
    valida=False
    listaFinal,valida = transiciones.principal(wl)
    if valida:
        etiqueta3 = tk.Label(text="CADENA VALIDA! Mostrando secuencia...", font=("Arial", 10), fg='#008f39')
        etiqueta3.place(x=80, y=200)
        cinta1()
    else :
        etiqueta3 = tk.Label(text="---------CADENA INVALIDA :(----------", font=("Arial", 10), fg='#FF0000' )
        etiqueta3.place(x=80, y=200)
        cinta1()
        
def cinta1():
   
    global listaFinal
    cinta.ventana2(listaFinal, True)

#Funcion limpiar las variables cadena, transiciones.lista=[], transiciones.posicion=0

def limpiar():
    transiciones.lista=[]
    entrada.text= " "
#Creamos la ventana

root = tk.Tk() #creamos la ventana
root.title("Teoria de autómatas -Equipo 7-")
root.resizable(0,0)
root.geometry("400x300+500+100")

#variable de entrada
cadena = tk.StringVar()



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#def imagen():
#img = Image.open('xd.png')
m = Canvas(root, width=200, height=300)
m.pack(fill="x")
img = resource_path("xd.png")
img2 = tk.PhotoImage(file = img)
m.create_image(200,60, image=img2, anchor="center")

etiqueta1 = tk.Label(text="Gramática", font=("Arial", 15))
etiqueta1.place(x=150,y=10)

#render = ImageTk.PhotoImage(img)
#img1 = tk.Label(root, image = render)
#img1.image = render
#img1.place(x= 55, y=40)

#img_gif = tk.PhotoImage(file = 'xd.png')
#label_img = tk.Label(root, image = img_gif)
#label_img.pack(side = "bottom", expand = "yes")

#etiqueta1 = tk.Label(text="{a^n+1 (aba)^n c^2| n>=0}")
#etiqueta1.place(x=100,y=40)

etiqueta2 = tk.Label(text="Ingrese cadena a validar", font=("Arial", 10))
etiqueta2.place(x=120,y=100)

entrada = tk.Entry(width=40,textvariable=cadena)
entrada.place(x=70,y=130)

boton1 = tk.Button(text="Iniciar",command=iniciar)
boton1.place(x=180,y=160)

#boton2 = tk.Button(text="Limpiar")
#boton2.place(x=300,y=200)

#boton3 = tk.Button(text="ver",command=cinta1)
#boton3.place(x=100,y=200)


root.mainloop()

