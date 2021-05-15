from Nodo import Nodo
from queue import PriorityQueue
class Arbol:
    def __init__(self, nCiudades):
        self.cantCiudades = nCiudades
        self.raiz = None
        self.ciudades= [i+1 for i in range(self.cantCiudades)]
        self.armarArbol(self)
    
    def armarArbol(self):
        if(not self.raiz):
            #poner la raiz
            self.raiz =  Nodo("1")
        else:
            self.armarArbol(self.raiz)
    
    """ armarArbol(nodo)"""
    # se revisa si hay nodo
    # Revisar el padre(de forma recursiva) y el nodo para ver sus valores
    # se comparan los valores del paso anterior con nCiudades
    # se crear los hijos que falten en comparacion a nCiudades
    # se recorre la lista de hijos y por cada uno se aplica armarArbol(nodo)
    def armarArbol(self, nodo):
        if(nodo):
        ciudadesExistentes= self.buscarPadres(nodo)
        ciudadesFaltantes= lis(set(self.ciudades)-set(ciudadesExistentes))
        for i, nombre in enumerate(ciudadesFaltantes):
            nodo.setHijos()
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

    def bestFirst(self, heuristica):
        lista=[]
        #open=[]
        #close=[]
        if(not self.raiz):
            open.append(self.raiz)
            #bestFirts(self, heuristica, open)

    def bestFirts(self,heuristica, open):
        open=[] #no visitado
        close=[] #visitado
        if len(open)==0:
            open.append(self.raiz)
        while len(open)> 0:
            open.sort()
            tempNodo= open.pop(0)
            padre= tempNodo
            close.append(tempNodo)
            
            if tempNodo


            

