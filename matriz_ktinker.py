## importar las librerías de tkinter##
from ctypes import resize, sizeof
from ctypes.wintypes import SIZE
from distutils import command
from sys import maxsize
from tkinter import *
from turtle import width
from xml.etree.ElementInclude import include

import numpy as np #matrix
import sys
from distutils import command
#===============================================================================================================================================================================================
##include matrix ##
## Crear la GUI ##
app = Tk()  # contenedor
app.title("Calculadora de Tránsito Vial") 
app.config(bg = "lavenderblush3")


# definir Gauss - Jordan#   
##def GAUSSJORDAN ##
# class GaussJordan:

def setMatrix():
    z = np.zeros((4,5))

    for i in range(4):
        for j in range(5):
            
        # Recuperamos los coeficientes de la ec.A
         z[0][0] = casilla00.get()
         z[0][1] = casilla01.get()
         z[0][2] = casilla02.get()
         z[0][3] = casilla03.get()
         z[0][4] = casilla04.get()

        # Recuperamos los coeficientes de la ec.B
         z[1][0] = casilla10.get()
         z[1][1] = casilla11.get()
         z[1][2] = casilla12.get()
         z[1][3] = casilla13.get()
         z[1][4] = casilla14.get()

        # Recuperamos los coeficientes de la ec.C    
         z[2][0] = casilla20.get()
         z[2][1] = casilla21.get()
         z[2][2] = casilla22.get()
         z[2][3] = casilla23.get()
         z[2][4] = casilla24.get()

        # Recuperamos los coeficientes de la ec.D
            
         z[3][0] = casilla30.get()
         z[3][1] = casilla31.get()
         z[3][2] = casilla32.get()
         z[3][3] = casilla33.get()
         z[3][4] = casilla34.get()

    return z

def GJ(z):
 x = np.zeros(4)
    # Leyendo los coeficientes de la matriz
# Eliminación de Gauss - Jordan
 for i in range(4):
                if z[i][i] == 0.0:
                    sys.exit('¡División entre cero!')
        
 for j in range(4):
    if i != j:
     ratio = z[j][i]/z[i][i]

     for k in range(5):
      z[j][k] = z[j][k] - ratio * z[i][k]

# Solución
    solucion = z[i]
 for i in range(4):
  z[i] = z[i][4]/[i][i]
  return solucion
#===============================================================================================================================================================================================
# Título#
T = Frame(app)
T.grid(column = 0, row = 0, sticky = NS)
T.config(bg = "lavenderblush3")
titulo = Label (T, text = "Método de Gauss - Jordan", font= ("Calibri", 25))
titulo.grid(column = 0, row = 0, sticky = NS, pady = 5)
titulo.config(bg = "lavenderblush3", fg = "white")

E = Frame(app)
E.grid(column = 7, row = 0, sticky = NS)
E.config(bg = "lavenderblush3")
titulo2 = Label (E, text = "Tránsito Vial", font= ("Calibri", 25))
titulo2.grid(column = 0, row = 0, sticky = NS, pady = 5)
titulo2.config(bg = "lavenderblush3", fg = "white")

#===============================================================================================================================================================================================
# imágenes (descripción y esquema)
img1 = PhotoImage(file ="descripción Small.png")

lbl_img1 = Label(app, image = img1)
lbl_img1.grid(column = 0, row = 1, rowspan = 7, ipadx= 20, ipady= 20)
lbl_img1.config(bg = "lavenderblush3")
lbl_img1.columnconfigure(0, weight=1)
lbl_img1.rowconfigure(1, weight= 250)

img2 = PhotoImage(file ="esquema Small.png")
lbl_img2 = Label(app, image = img2)
lbl_img2.grid(column = 7, row = 1, rowspan= 7, ipadx= 20, ipady= 20)
lbl_img2.config(bg = "lavenderblush3")
lbl_img2.columnconfigure(0, weight=1)
lbl_img2.rowconfigure(1, weight= 250)
#===============================================================================================================================================================================================
## Etiquetas formato GRID##

# espacio en blanco
etiqueta = Label(app)
etiqueta.grid(column = 1, row = 1)
etiqueta.config(bg = "lavenderblush3")

# Filas de intersección con cuadros de texto 
# A
A = Frame(app)
A.grid(column = 1, row = 2, ipadx = 5, ipady = 5, sticky = NS)
A.config(bg = "lavenderblush3")
etiqueta0 = Label (A, text = "A", width = 5)
etiqueta0.grid(column = 1, row = 2, ipadx = 5, ipady = 5, sticky = NS, pady = 5)
etiqueta0.config(bg = "lavenderblush3", fg = "white")

# Casillas por fila 0
casilla00 = Entry (app, width = 5)
casilla01 = Entry (app, width = 5)
casilla02 = Entry (app, width = 5)
casilla03 = Entry (app, width = 5)
casilla04 = Entry (app, width = 5)


casilla00.grid(column = 2, row = 2, sticky = N, padx = 2)
casilla01.grid(column = 3, row = 2, sticky = N, padx = 2)
casilla02.grid(column = 4, row = 2, sticky = N, padx = 2)
casilla03.grid(column = 5, row = 2, sticky = N, padx = 2)
casilla04.grid(column = 6, row = 2, sticky = N, padx = 2)

casilla00.insert(0, "1")
casilla01.insert(0, "1")
casilla02.insert(0, "0")
casilla03.insert(0, "0")

casilla00.configure(state='disabled')
casilla01 .configure(state='disabled')
casilla02 .configure(state='disabled')
casilla03 .configure(state='disabled')

#B
B = Frame(app)
B.grid(column = 1, row = 3, ipadx = 5, ipady = 5, sticky = NS)

B.config(bg = "lavenderblush3")

etiqueta1 = Label (B, text = "B", width = 5)
etiqueta1.grid(column = 1, row = 3, ipadx = 5, ipady = 5, pady = 5, sticky = NS)
etiqueta1.config(bg = "lavenderblush3", fg = "white")

#Casillas por fila 1
casilla10 = Entry (app, width = 5)
casilla11 = Entry (app, width = 5)
casilla12 = Entry (app, width = 5)
casilla13 = Entry (app, width = 5)
casilla14 = Entry (app, width = 5)


casilla10.grid(column = 2, row = 3, sticky = N, padx = 2)
casilla11.grid(column = 3, row = 3, sticky = N, padx = 2)
casilla12.grid(column = 4, row = 3, sticky = N, padx = 2)
casilla13.grid(column = 5, row = 3, sticky = N, padx = 2)
casilla14.grid(column = 6, row = 3, sticky = N, padx = 2)

casilla10.insert(0, "1")
casilla11.insert(0, "0")
casilla12.insert(0, "1")
casilla13.insert(0, "0")

casilla10.configure(state='disabled')
casilla11 .configure(state='disabled')
casilla12 .configure(state='disabled')
casilla13 .configure(state='disabled')


# C
C = Frame(app)
C.grid(column = 1, row = 4, ipadx = 5, ipady = 5, sticky = NS)

C.config(bg = "lavenderblush3")

etiqueta2 = Label (C, text = "C", width = 5)
etiqueta2.grid(column = 1, row = 4, ipadx = 5, ipady = 5, pady = 5, sticky = NS)
etiqueta2.config(bg = "lavenderblush3", fg = "white")

# Casillas por fila 2
casilla20 = Entry (app, width = 5)
casilla21 = Entry (app, width = 5)
casilla22 = Entry (app, width = 5)
casilla23 = Entry (app, width = 5)
casilla24 = Entry (app, width = 5)


casilla20.grid(column = 2, row = 4, sticky = N, padx = 2)
casilla21.grid(column = 3, row = 4, sticky = N, padx = 2)
casilla22.grid(column = 4, row = 4, sticky = N, padx = 2)
casilla23.grid(column = 5, row = 4, sticky = N, padx = 2)
casilla24.grid(column = 6, row = 4, sticky = N, padx = 2)

casilla20.insert(0, "0")
casilla21.insert(0, "0")
casilla22.insert(0, "1")
casilla23.insert(0, "1")

casilla20.configure(state='disabled')
casilla21 .configure(state='disabled')
casilla22 .configure(state='disabled')
casilla23 .configure(state='disabled')


# D
D = Frame(app)
D.grid(column = 1, row = 5, ipadx = 5, ipady = 5, sticky = NS)

D.config(bg = "lavenderblush3")

etiqueta3 = Label (D, text = "D", width = 5)
etiqueta3.grid(column = 1, row = 5, ipadx = 5, ipady = 5, pady = 5, sticky = NS)
etiqueta3.config(bg = "lavenderblush3", fg = "white")

# Casillas por fila 3
casilla30 = Entry (app, width = 5)
casilla31 = Entry (app, width = 5)
casilla32 = Entry (app, width = 5)
casilla33 = Entry (app, width = 5)
casilla34 = Entry (app, width = 5)


casilla30.grid(column = 2, row = 5, sticky = N, padx = 2)
casilla31.grid(column = 3, row = 5, sticky = N, padx = 2)
casilla32.grid(column = 4, row = 5, sticky = N, padx = 2)
casilla33.grid(column = 5, row = 5, sticky = N, padx = 2)
casilla34.grid(column = 6, row = 5, sticky = N, padx = 2)

casilla30.insert(0, "0")
casilla31.insert(0, "1")
casilla32.insert(0, "0")
casilla33.insert(0, "1")

casilla30.configure(state='disabled')
casilla31 .configure(state='disabled')
casilla32 .configure(state='disabled')
casilla33 .configure(state='disabled')


# Columnas f (flujos)
# f1
f1 = Frame(app)
f1.grid(column = 2, row = 1, ipadx = 5, ipady = 5, sticky = NS)
f1.config(bg = "lavenderblush3")
f1.columnconfigure(2, weight=1)
f1.rowconfigure(1, weight= 1)
etiqueta4 = Label (f1, text = "f1")
etiqueta4.grid(column = 2, row = 1, ipadx = 5, ipady = 5, padx = 5, sticky = NS)
etiqueta4.config(bg = "lavenderblush3", fg = "white")
etiqueta4.columnconfigure(2, weight=1)
etiqueta4.rowconfigure(1, weight= 1)
#f2
f2 = Frame(app)
f2.grid(column = 3, row = 1, ipadx = 5, ipady = 5, sticky = NS)

f2.config(bg = "lavenderblush3")
f2.columnconfigure(3, weight=1)
f2.rowconfigure(1, weight= 1)
etiqueta5 = Label (f2, text = "f2")
etiqueta5.grid(column = 3, row = 1, ipadx = 5, ipady = 5, padx = 5, sticky = NS)
etiqueta5.config(bg = "lavenderblush3", fg = "white")
etiqueta5.columnconfigure(3, weight=1)
etiqueta5.rowconfigure(1, weight= 1)
# f3
f3 = Frame(app)
f3.grid(column = 4, row = 1, ipadx = 5, ipady = 5, sticky = NS)

f3.config(bg = "lavenderblush3")
f3.columnconfigure(4, weight=1)
f3.rowconfigure(1, weight= 1)
etiqueta6 = Label (f3, text = "f3")
etiqueta6.grid(column = 4, row = 1, ipadx = 5, ipady = 5, padx = 5, sticky = NS)
etiqueta6.config(bg = "lavenderblush3", fg = "white")
etiqueta6.columnconfigure(4, weight=1)
etiqueta6.rowconfigure(1, weight= 1)
# f4
f4 = Frame(app)
f4.grid(column = 5, row = 1, ipadx = 5, ipady = 5, sticky = NS)

f4.config(bg = "lavenderblush3")
f4.columnconfigure(5, weight=1)
f4.rowconfigure(1, weight= 1)
etiqueta7 = Label (f4, text = "f4")
etiqueta7.grid(column = 5, row = 1, ipadx = 5, ipady = 5, padx = 5, sticky = NS)
etiqueta7.config(bg = "lavenderblush3", fg = "white")
etiqueta7.columnconfigure(5, weight=1)
etiqueta7.rowconfigure(1, weight= 1)
# k
f = Frame(app)
f.grid(column = 6, row = 1, ipadx = 5, ipady = 5, sticky = NS)

f.config(bg = "lavenderblush3")
f.columnconfigure(6, weight=1)
f.rowconfigure(1, weight= 1)
etiqueta8 = Label (f, text = "k")
etiqueta8.grid(column = 6, row = 1, ipadx = 5, ipady = 5, padx = 5, sticky = NS)
etiqueta8.config(bg = "lavenderblush3", fg = "white")
etiqueta8.columnconfigure(6, weight=1)
etiqueta8.rowconfigure(1, weight= 1)

# etiqueta cargando...#
label = Label(app,  
              text ="Calculando...", font = ("Calibri", 16)) 
  
label.grid (column = 3, row = 0, columnspan= 3)

#===============================================================================================================================================================================================
##Hacer que funcionen las clases##
# Enviar datos y aplicar GJ
botonenviar = Button(app, text = "Enviar", fg = "white", width = 5, command = (setMatrix, GJ)) #AGREGAR DEF DE GAUSS-JORDAN
botonenviar.grid(column = 3, row = 7, sticky = NS, columnspan= 3)
botonenviar.config(bg = "lavenderblush3", fg = "black")

## Ventana de resultados##
def openNewWindow(): 
    Window2 = Toplevel(app) 
    Window2.title("Resultados") 

    Window2.config(bg = "lavenderblush3")



# Botón para ir a la ventana resultados#
btn = Button(app,  
             text ="Obtener resultados",  
             command = openNewWindow) 
btn.grid(column = 3, row = 10, columnspan=3, sticky= NS, ipadx= 1, ipady= 1, pady= 10) 
label.config(bg = "lavenderblush3", fg = "white")

 

app.mainloop()

