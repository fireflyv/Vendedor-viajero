from Nodo import Nodo
class Arbol:
    def __init__(self, nCiudades):
        self.cantCiudades = nCiudades
        self.raiz = None
        self.ciudades = [i for i in range(self.cantCiudades)] 
        self.armarArbol()
    
    def armarArbol(self):
        if(not self.raiz):
            #poner la raiz
            self.raiz =  Nodo(0)
            self.armarArbol2(self.raiz)
    
    def armarArbol2(self, nodo):
        if (nodo):
            # Revisar el padre(de forma recursiva) y el nodo para ver las cidades existentes
            ciudadesExistentes = self.buscarPadres(nodo)
            # se ve que ciudades faltan
            ciudadesFaltantes = list(set(self.ciudades) - set(ciudadesExistentes))
            # se crear las ciudades faltantes
            for i, nombre in enumerate(ciudadesFaltantes):
                nodo.setHijos(nombre)
                # se recorre la lista de hijos y por cada uno se aplica armarArbol(nodo)
                self.armarArbol2(nodo.getHijo(i))

    def buscarPadres(self,nodo):
        padres = []
        while (nodo):
            padres.append(nodo.getNombre())
            nodo = nodo.getPadre()
        return padres

    def bestFirst(self, heuristica):
        open=[]
        close=[]
        orderByKey = lambda key : key[0]
        if(self.raiz): 
            open.append((0,self.raiz))
            return self.bestFirst2(heuristica, open,close,orderByKey)

    def bestFirst2(self,heuristica, open, close,orderByKey):
        if len(open)> 0:
            tempNodo= open.pop()
            close.append(tempNodo)
            if len(tempNodo[1].getHijos())==0:
                return close
            
            listaHijos = tempNodo[1].getHijos() 
            for i in range(len(listaHijos)): 
                val= heuristica[tempNodo[1].getNombre()][listaHijos[i].getNombre()]
                open.append((val,listaHijos[i]))  
            open.sort(reverse=True, key=orderByKey)
            return self.bestFirst2(heuristica, open, close, orderByKey)

    def getRaiz(self):
       return self.raiz
            
            
