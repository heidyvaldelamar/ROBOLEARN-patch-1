# Importamos la librería NumPy
import numpy as np
# Importamos sys para salir del programa cuando se divida entre 0
import sys
#Importamos el py de Tkinter para obtener las casillas#
from matriz_ktinker import *
class matrix:

def setMatrix()


# Pedimos al usuario que ingrese el número de variables
v = 4

# Hacemos un arreglo (matriz) de v x v + 1
# v + 1 --> # columnas = # variables + 1 (columna de solución)
# La inicializamos en 0 con np.zeros
z = np.zeros((v,v + 1))

# Hacemos un arrglo para la solución
# Tamaño: n x 1 (para que sea vector columna) #no salió :(
# Lo inicializamos en 0
x = np.zeros((v , 1))

# Método de Gauss Jordan
for i in range(v):
  if z[i][j] == 0.0:
    sys.exit('Alto! Divides entre 0!')
  for j in range(v):
    if i != j:
      r = z[j][i] / z[i][i]
      for k in range (v + 1):
        z[j][k] = z[j][k] - r * z[i][k]

# Para la solución
for i in range (v):
  x[i] = z[i][v] / z[i][i]

def GJ () :

# Mostrar la solución en consola
    for i in range(v):
        print('X%d = %0.2f' %(i, x[i]), end = '\t')
