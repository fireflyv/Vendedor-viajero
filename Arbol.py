from Nodo import Nodo
class Arbol:
    def __init__(self, nCiudades):
        self.cantCiudades = nCiudades
        self.raiz = None
        self.ciudades = [i for i in range(self.cantCiudades)] 
        self.__armarArbol()
    
    def __armarArbol(self):
        if(not self.raiz):
            #poner la raiz
            self.raiz =  Nodo(0)
            self.__armarArbol2(self.raiz)
    
    def __armarArbol2(self, nodo):
        if (nodo):
            # Revisar el padre(de forma recursiva) y el nodo para ver las cidades existentes
            ciudadesExistentes = self.__buscarPadres(nodo)
            # se ve que ciudades faltan
            ciudadesFaltantes = list(set(self.ciudades) - set(ciudadesExistentes))
            # se crear las ciudades faltantes
            for i, nombre in enumerate(ciudadesFaltantes):
                nodo.setHijos(nombre)
                # se recorre la lista de hijos y por cada uno se aplica __armarArbol(nodo)
                self.__armarArbol2(nodo.getHijo(i))

    def __buscarPadres(self,nodo):
        padres = []
        while (nodo):
            padres.append(nodo.getNombre())
            nodo = nodo.getPadre()
        return padres

    def bestFirst(self, heuristica):
        open=[]
        orderByKey = lambda key : key[0]
        if(self.raiz): 
            open.append((0,self.raiz))
            solucion = self.__bestFirst2(heuristica, open,orderByKey)
            return self.__obtenerRecorrido(solucion,heuristica)

    def __bestFirst2(self,heuristica, open,orderByKey,lastNode = None):
        if len(open)> 0:
            tempNodo= open.pop()
            lastNode = tempNodo[1]
            if len(tempNodo[1].getHijos())==0:
                return lastNode
            listaHijos = tempNodo[1].getHijos() 
            for i in range(len(listaHijos)): 
                val= heuristica[tempNodo[1].getNombre()][listaHijos[i].getNombre()]
                open.append((val,listaHijos[i]))  
            open.sort(reverse=True, key=orderByKey)
            return self.__bestFirst2(heuristica, open, orderByKey,lastNode)

    def __obtenerRecorrido(self,nodo,heuristica):
        recorrido = []
        while (nodo.getPadre()):
            ciudad = nodo.getNombre()
            padre = nodo.getPadre().getNombre()
            valor = heuristica[ciudad][padre]
            recorrido.append(f"[A{ciudad}]")
            recorrido.append(valor)
            nodo = nodo.getPadre()
        recorrido.append(f"[A{padre}]")
        recorrido.reverse()
        recorrido = " -> ".join(map(str, recorrido)) 
        return recorrido
