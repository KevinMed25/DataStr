from NodoBin import *

class ArbolABB:
    def __init__(self, dato):
        self.__raiz = NodoBin(dato=dato)
    @property
    def raiz(self):
        return self.__raiz
    @raiz.setter
    def raiz(self,dato):
        self.__raiz.dato=dato
    def inorden(self):
        if self.raiz is not None:
            self.raiz.inorden()
    def __inserta_ordenado(self,nodo:NodoBin, dato):
        if int(dato)<int(nodo.dato):
            if nodo.izq is None:
                nodo.izq = NodoBin(dato)
            else:
                self.__inserta_ordenado(nodo.izq,dato)
        elif int(dato)>int(nodo.dato):
            if nodo.der is None:
                nodo.der = NodoBin(dato)
            else:
                self.__inserta_ordenado(nodo.der,dato)
    def insertar(self, dato):
        self.__inserta_ordenado(self.raiz,dato)
    def __buscar(self, nodo:NodoBin, dato)->NodoBin:
        if int(dato)<int(nodo.dato):
            if nodo.izq is None: return None
            else: return self.__buscar(nodo.izq,dato)
        elif int(dato)>int(nodo.dato):
            if nodo.der is None: return None
            else: return self.__buscar(nodo.der, dato)
        else:
            return nodo
    def buscar(self,nodo,dato):
        return self.__buscar(nodo,dato)
    def __buscar_minimo(self, nodo:NodoBin)->NodoBin:
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo
    def __borrar_minimo(self, nodo:NodoBin)->NodoBin:
        if nodo.izq is not None:
            nodo.izq = self.__borrar_minimo(nodo.izq)
            return nodo
        else: return nodo.der
    
    def __borrar(self, nodo:NodoBin,dato):
        n = self.__buscar(nodo,dato)
        if n is None: print('Elemento no encontrado')
        else:
            if n.der != None and n.izq != None:
                #Se aplica el criterio de eliminación con 2 hijos
                #Buscar el elemento más pequeño en el subárbol derecho
                minimo = self.__buscar_minimo(n.der)
                n.dato = minimo.dato
                n.der = self.__borrar_minimo(n.der)
            else:
                n = n.izq if n.izq is None else n.der
        return n
    def borrar(self, dato):
        self.__borrar(self.raiz,dato)

if __name__=='__main__':
    arbol = ArbolABB(120)
    arbol.insertar(87)
    arbol.insertar(140)
    arbol.insertar(43)
    arbol.insertar(99)
    arbol.insertar(130)
    arbol.insertar(22)
    arbol.insertar(65)
    arbol.insertar(93)
    arbol.insertar(135)
    arbol.insertar(56)
    arbol.insertar(95)
    print("RECORRIDO EN INORDEN")
    arbol.inorden()
    x = arbol.buscar(arbol.raiz,578)
    if x is None: print('No se encontró')
    else: print(x.dato)
    eliminado = 548
    print ('Eliminado el elemento:',eliminado)
    arbol.borrar(eliminado)
    arbol.inorden()

