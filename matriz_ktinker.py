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
from GaussJ import * # importamos la función de GaussJordan 
#===============================================================================================================================================================================================
##include matrix ##
## Crear la GUI ##
app = Tk()  # ventana principal
app.title("Calculadora de Tránsito Vial") # Título de la ventana principal
app.config(bg = "lavenderblush3") # Definir el color del background de la ventana principal

#===============================================================================================================================================================================================
# Título 1 que corresponde a la descripción del problema#
T = Frame(app) # Ubicamos el frame del Título en la ventana principal
T.grid(column = 0, row = 0, sticky = NS) #Damos una posición al frame (sticky corresponde a la orientación del frame centrado)
T.config(bg = "lavenderblush3") # Definimos el color del frame

titulo = Label (T, text = "Método de Gauss - Jordan", font= ("Calibri", 25)) #Agregamos texto al frame del título
titulo.grid(column = 0, row = 0, sticky = NS, pady = 5) # Damos posición al texto del título (pady se refiere al margen exterior del grid)
titulo.config(bg = "lavenderblush3", fg = "white") # Configura el color del fondo y de texto

# Seguir los mismos pasos para el segundo título, este título corresponde a la imagen del esquema

E = Frame(app)
E.grid(column = 7, row = 0, sticky = NS)
E.config(bg = "lavenderblush3")
titulo2 = Label (E, text = "Tránsito Vial", font= ("Calibri", 25))
titulo2.grid(column = 0, row = 0, sticky = NS, pady = 5)
titulo2.config(bg = "lavenderblush3", fg = "white")

#===============================================================================================================================================================================================
# imágenes (descripción y esquema)
img1 = PhotoImage(file ="descripción Small.png") # Usamos PhotoImage para insertar una imagen 

lbl_img1 = Label(app, image = img1) # Con una etiqueta posicionamos la imágen en la ventana principal
lbl_img1.grid(column = 0, row = 1, rowspan = 7, ipadx= 20, ipady= 20) # Posicionamos la imagen, rowspan sirve para seleccionar las filas que desees agrupar, ipadx y ipady son los parámetros que se definen para el margen interno del grid

lbl_img1.config(bg = "lavenderblush3") # configuramos el fondo de la imagen
lbl_img1.columnconfigure(0, weight=1) # la configuración de las columnas y filas sirven para especificar el tamaño que desees para la casilla
lbl_img1.rowconfigure(1, weight= 250)

# Damos los mismos parámetros para la imagen del esquema

img2 = PhotoImage(file ="esquema Small.png") 
lbl_img2 = Label(app, image = img2)
lbl_img2.grid(column = 7, row = 1, rowspan= 7, ipadx= 20, ipady= 20)
lbl_img2.config(bg = "lavenderblush3")
lbl_img2.columnconfigure(0, weight=1)
lbl_img2.rowconfigure(1, weight= 250)
#===============================================================================================================================================================================================
## Etiquetas formato GRID##

# espacio en blanco, corresponde a la casilla que va entre las intersecciones y variables
etiqueta = Label(app)
etiqueta.grid(column = 1, row = 1)
etiqueta.config(bg = "lavenderblush3")

# Filas de intersección con cuadros de texto, primero hacemos un frame para posicionar cada etiqueta 
# A
A = Frame(app)
A.grid(column = 1, row = 2, ipadx = 5, ipady = 5, sticky = NS)
A.config(bg = "lavenderblush3")
etiqueta0 = Label (A, text = "A", width = 5)
etiqueta0.grid(column = 1, row = 2, ipadx = 5, ipady = 5, sticky = NS, pady = 5)
etiqueta0.config(bg = "lavenderblush3", fg = "white")

# Usamos un Entry por cada casilla correspondiente a la matriz aumentada que nos proporcionará el usuario
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

# Para facilitar el llenado de la matriz damos valores predeterminados que están dados por defecto para cada intersección 
casilla00.insert(0, "1")
casilla01.insert(0, "1")
casilla02.insert(0, "0")
casilla03.insert(0, "0")
# Dejamos los valores predeterminados como un modo de lectura para que el usuario no modifique por error las variables
casilla00.configure(state='disabled')
casilla01 .configure(state='disabled')
casilla02 .configure(state='disabled')
casilla03 .configure(state='disabled')

#Repetimos los pasos para cada fila 
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


# Columnas f (flujos), agregamos los encabezados de las variables por columnas 
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

# Esta etiqueta es para dejar un comentario en la ventana principal
# etiqueta cargando...#
label = Label(app,  
              text ="Calculando...", font = ("Calibri", 16)) 
  
label.grid (column = 3, row = 0, columnspan= 3)

#===============================================================================================================================================================================================
##Hacer que funcionen las clases## Aún está en proceso
# La idea es que con el parámetro command se pueda llamar a las funciones del archivo de Gauss Jordan que arroje los valores que proporciona el usuario y devuelva una respuesta en otra ventana
# Enviar datos y aplicar GJ
botonenviar = Button(app, text = "Enviar", fg = "white", width = 5) ##command = setMatrix)
botonenviar.grid(column = 3, row = 7, sticky = NS, columnspan= 3)
botonenviar.config(bg = "lavenderblush3", fg = "black")

## Ventana de resultados, definimos una nueva ventana para devolver los resultados de las variables 
def openNewWindow(): 
    Window2 = Toplevel(app) 
    Window2.title("Resultados") 

    Window2.config(bg = "lavenderblush3")
    resultados = Frame(Window2)## command = GJ)


#Insertamos un botón en la ventana principal para ir a la ventana de resultados
# Botón para ir a la ventana resultados#
btn = Button(app,  
             text ="Obtener resultados",  
             command = openNewWindow) 
btn.grid(column = 3, row = 10, columnspan=3, sticky= NS, ipadx= 1, ipady= 1, pady= 10) 
label.config(bg = "lavenderblush3", fg = "white")

 
# Con esto agregamos todos los widgets que creamos en la interfaz
app.mainloop()

