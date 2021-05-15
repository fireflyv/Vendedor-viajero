"""
nombre string
padre nmodo
hijos nodo[]
nodo(nombre string)
gets set
"""
class Nodo:


    def __init__(self, nombre):
        self.nombre= nombre
        self.padre= None
        self.hijos= [] #quede con duda en esta 

    def getNombre(self):
        return self.nombre
    
    def getPadre(self):
        return self.padre
    
    def getHijos(self):
        return self.hijos
        
    def getHijo(self,posicion):
        return self.hijos[posicion]

    def setNombre(self, newNombre):
        self.nombre= newNombre
    
    def setPadre(self, newPadre):
        self.padre= newPadre

    def setHijos(self, nombre):
        hijo = Nodo(nombre)
        hijo.setPadre(self)
        self.hijos.append(hijo)