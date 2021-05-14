import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#crea la heuristica del problema en una matriz de nxn
def crearHeuristica(n):
    #los valores de la heuristica son al azar del 0 al 100
    heuristica = np.random.randint(0, 100, (ciudades,ciudades))
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
    #tiempo = y
    #ciudades =x
    plt.plot(x, y)
    plt.xlabel("Cantidad de ciudades")
    plt.ylabel("Tiempo [ms]")
    plt.title("Ciudades vs tiempo")
    plt.xticks(x)
    plt.savefig(f"plots/grafico{len(x)}.png")

ciudades = 4
x= []
y =[]
while True:
    #Se calcula la heuristica
    heuristica = crearHeuristica(ciudades)
    #se resulve el problema
    #se guardan los resultados
    x.append(ciudades)
    y.append(np.random.randint(0, 100))
    #se grafican
    graficar(x,y)
    #las ciudades se incrementan en 2
    ciudades += 2
    if ciudades == 10:
        break
