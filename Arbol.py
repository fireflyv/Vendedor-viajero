from Nodo import Nodo

class Arbol:
    def __init__(self, nCiudades):
        self.cantCiudades = nCiudades
        self.raiz = None
        self.armarArbol(self)
    
    def armarArbol(self):
        if(not self.raiz):
            #poner la raiz
            self.raiz =  Nodo("1")
        else:
            self.armarArbol(self.raiz)
    
    # def armarArbol(self, nodo):
    #     if (not nodo):

    """ armarArbol(nodo)"""
    # se revisa si hay nodo
    # Revisar el padre(de forma recursiva) y el nodo para ver sus valores
    # se comparan los valores del paso anterior con nCiudades
    # se crear los hijos que falten en comparacion a nCiudades
    # se recorre la lista de hijos y por cada uno se aplica armarArbol(nodo)


    """Best first(heuristica)   -> solo la raiz"""
    #heuristica = 0
    #meterlo a la lista
    # se utiliza bestFirts(heuristica, open)

    """ Best firts (heuristica, open)"""
    # revisar si la lista esta vacia
    # se hace pop
    #revisar condicion de termino (es hoja?) si cumple con la condicion se termina la busqueda //
    #asignar valor de heuristica a sus hijos y meterlos a la lista de prioridad (open)
    # se ordena la lista (mayor a menor)
    # best first (heuristica, open)