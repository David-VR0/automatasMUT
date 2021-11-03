import tkinter as tk
import transiciones2
import cinta
#Funciones
listaFinal=[]
def iniciar():
    limpiar()
    wl=['#']
    print(cadena.get())
    for i in list(cadena.get()):
        wl.append(i)
    wl.append('#')
    global listaFinal
    valida=False
    listaFinal,valida = transiciones2.paso1(wl, 0)
    if valida:
        etiqueta3 = tk.Label(text="CADENA VALIDA")
        etiqueta3.place(x=100, y=150)
    else :
        etiqueta3 = tk.Label(text="CADENA INVALIDA")
        etiqueta3.place(x=100, y=150)
def cinta1():
    global listaFinal
    cinta.ventana2(listaFinal, True)

#Funcion limpiar las variables cadena, transiciones.lista=[], transiciones.posicion=0

def limpiar():
    transiciones2.lista=[]
    transiciones2.posicion=0
    transiciones2.cantidad=0
#Creamos la ventana

root = tk.Tk() #creamos la ventana
root.title("PIA")
root.resizable(0,0)
root.config(width=400, height=300)

#variable de entrada
cadena = tk.StringVar()

etiqueta1 = tk.Label(text="{a^n+1 (aba)^n c^2| n>=0}")
etiqueta1.place(x=100,y=40)

etiqueta2 = tk.Label(text="Cadena: ")
etiqueta2.place(x=50,y=70)

entrada = tk.Entry(width=40,textvariable=cadena)
entrada.place(x=100,y=70)

boton1 = tk.Button(text="Iniciar",command=iniciar)
boton1.place(x=200,y=100)

#boton2 = tk.Button(text="Limpiar")
#boton2.place(x=300,y=200)

boton3 = tk.Button(text="ver",command=cinta1)
boton3.place(x=100,y=200)


root.mainloop()

