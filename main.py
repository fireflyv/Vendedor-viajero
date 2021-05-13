import numpy as np

#crea la heuristica del problema en una matriz de nxn
def crearHeuristica(n):
    #los valores de la heuristica son al azar del 0 al 100
    heuristica = np.random.random_integers(0, 100, (ciudades,ciudades))
    # se reemplaza la diagonal por 0s
    np.fill_diagonal(heuristica,0)
    for i in range(len(heuristica)):
        for j in range(len(heuristica[0])):
            # se copia el triangulo superior de la matriz en el inferior
            if i > j :
                heuristica[i][j] = heuristica[j][i]
    return heuristica

ciudades = 2
while True:
    heuristica = crearHeuristica(ciudades)
    print(heuristica)
    #las ciudades se incrementan en 2
    ciudades += 2
    if ciudades == 6:
        break
