import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from Arbol import Arbol

#crea la heuristica del problema en una matriz de nxn
def crearHeuristica(n):
    #los valores de la heuristica son al azar del 0 al 100
    heuristica = np.random.randint(1, 100, (cantCiudades,cantCiudades))
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
    # Se calcula la heuristica
    heuristica = crearHeuristica(cantCiudades)
    # Se arma el arbol y se obtiene el recorrido con best first
    arbol = Arbol(cantCiudades)
    inicio = datetime.now()
    recorrido = arbol.bestFirst(heuristica)
    fin = datetime.now()
    print(recorrido)
    # Se muestra el recorrido
    # Se guardan los resultados
    x.append(cantCiudades)
    y.append(round((fin - inicio).total_seconds()*1000,2))
    # Se grafican y se guardan los datos
    graficar(x,y)
    crearCSV(x,y)
    # Se incrementan las ciudades en 2
    cantCiudades += 2
    if cantCiudades > 20:
        break
 
