from Nodo import Nodo
from Arbol import Arbol

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crea la heuristica del problema en una matriz de nxn

def crearHeuristica(n):
    #los valores de la heuristica son al azar del 0 al 100
    heuristica = np.random.randint(0, 100, (cantCiudades,cantCiudades))
    # se reemplaza la diagonal por 0s
    np.fill_diagonal(heuristica,0)
    for i in range(len(heuristica)):
        for j in range(len(heuristica[0])):
            # se copia el triangulo superior de la matriz en el inferior
            if i > j :
                heuristica[i][j] = heuristica[j][i]
    return heuristica
# grafica cantidad de ciudades vs tiempo[ms] y lo guarda en plots
def graficar(x,y):
    plt.plot(x, y)
    plt.xlabel("Cantidad de ciudades")
    plt.ylabel("Tiempo [ms]")
    plt.title("Ciudades vs tiempo")
    plt.xticks(x)
    plt.savefig(f"plots/plot{len(x)}.png")
#crea un csv con la cantidad de ciudades y el tiempo[ms]
def crearCSV(x,y):
    df =pd.DataFrame(x,y)
    df.to_csv("plots/data.csv", header=False)


cantCiudades = 4
x= []
y =[]
while True:
    #Se calcula la heuristica
    heuristica = crearHeuristica(cantCiudades)
    #se resulve el problema
    arbol = Arbol(cantCiudades)
    #se guardan los resultados
    x.append(cantCiudades)
    y.append(np.random.randint(0, 100))
    #se grafican y se guardan los datos
    graficar(x,y)
    crearCSV(x,y)
    # Se incrementan las ciudades en 2
    cantCiudades += 2
    if cantCiudades == 10:
        break
<<<<<<< HEAD
 #====================================== 
"""
node= Nodo("Miranda")   

node2= Nodo("A")
node3= Nodo("B")
node.setHijos(node2)
node.setHijos(node3)
print(node.getHijos()[1].getPadre().getNombre())
print(node.getHijos())
"""      
=======
 
>>>>>>> c74429a09c8113e4f8b354ce87b0182794c9060c
