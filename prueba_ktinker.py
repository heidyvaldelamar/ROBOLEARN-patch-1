
## importar las librerías de tkinter##
from tkinter import *
#===============================================================================================================================================================================================
## Crear la GUI ##
# Se recomienda uso de sympy para el uso de ecuaciones#
ventana = Tk()  # contenedor
ventana.title("Calculadora de Tránsito Vial")
ventana.geometry("1200x500")  # tamaño de la ventana
ventana.config(bg = "lavenderblush3")
#===============================================================================================================================================================================================
## Añadir elementos a la ventana ##
# Etiquetas
titulo = Label(
    ventana, 
    text = "Método de Gauss-Jordan", 
    font = ("Calibri", 25, "bold"),
    
    )  
titulo.config(bg = "lavenderblush4", fg = "white")
titulo.grid(row= 0 , column = 0)
titulo.pack(fill = BOTH)
instrucciones = Label(
    ventana,
   text = "Para realizar el cálculo de tránsito de entradas y salidas de las intersecciones A, B, C, D, insertar las ecuaciones correspondientes a las intersecciones del tránsito.",
   font = ("Calibri", 16)
)
instrucciones.config(
    bg = "lavenderblush3",
     fg = "white",
     width = 5, height= 5
     )
instrucciones.pack(fill = BOTH)
#===============================================================================================================================================================================================
##Insertar las ecuaciones##

# ecuación A
ecuacionA = Label(
    ventana,
   text = "Ecuación A",
   font = ("Calibri", 16),
   fg = "white"
)
ecuacionA.config(bg = "lavenderblush3")
ecuacionA.pack()

# Caja de texto de la ecuación A
cajatextoA = Entry(ventana)
cajatextoA.pack()

 #Para imprimir la ecuación A en la consola 
def ecA():
    A = cajatextoA.get()
    print(A)

#Botón que envía la ecuación A a la consola
botonA = Button(
    ventana, 
    text = "enviar", 
    command = ecA
    )
botonA.pack()


# ecuación B
ecuacionB = Label(
    ventana,
   text = "Ecuación B",
   font = ("Calibri", 16),
   fg = "white"
)
ecuacionB.config(bg = "lavenderblush3")
ecuacionB.pack()

# Caja de texto de la ecuación B
cajatextoB = Entry(ventana)
cajatextoB.pack()

#Para imprimir la ecuación B en la consola 
def ecB():
    B = cajatextoB.get()
    print(B)

#Botón que envía la ecuación B a la consola
botonB = Button(
    ventana, 
    text = "enviar", 
    command = ecB
    )
botonB.pack()


# ecuación C
ecuacionC = Label(
    ventana,
   text = "Ecuación C",
   font = ("Calibri", 16),
   fg = "white"
)
ecuacionC.config(bg = "lavenderblush3")
ecuacionC.pack()

# Caja de texto de la ecuación C
cajatextoC = Entry(ventana)
cajatextoC.pack()

#Para imprimir la ecuación C en la consola 
def ecC():
    C = cajatextoC.get()
    print(C)

#Botón que envía la ecuación C a la consola
botonC = Button(
    ventana, 
    text = "enviar", 
    command = ecC
    )
botonC.pack()


# ecuación D
ecuacionD = Label(
    ventana,
   text = "Ecuación D",
   font = ("Calibri", 16),
   fg = "white"
)
ecuacionD.config(bg = "lavenderblush3")
ecuacionD.pack()
# Caja de texto de la ecuación D
cajatextoD = Entry(ventana)
cajatextoD.pack()

#Para imprimir la ecuación D en la consola 
def ecD():
    D = cajatextoD.get()
    print(D)

#Botón que envía la ecuación D a la consola
botonD = Button(
    ventana, 
    text = "enviar", 
    command = ecD
    )
botonD.pack()
#===============================================================================================================================================================================================

ventana.mainloop()  # lleva el registro de la ventana