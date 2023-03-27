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

    def preorden(self):
        if self.raiz is not None:
            self.raiz.preorden()

    def posorden(self):
        if self.raiz is not None:
            self.raiz.posorden()
    
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

    def __buscar(self, nodo:NodoBin, padre:NodoBin, dato)->tuple:
        if int(dato)<int(nodo.dato):
            if nodo.izq is None: return None,None
            else: 
                return self.__buscar(nodo.izq,nodo,dato)
        elif int(dato)>int(nodo.dato):
            if nodo.der is None: return None,None
            else: return self.__buscar(nodo.der, nodo,dato)
        else:
            return nodo,padre
    
    def buscar(self,nodo,dato):
        return self.__buscar(nodo,None,dato)
    
    """ 
    MÉTODO PARA BUSCAR EL ELEMENTO MÁS PEQUEÑO (nodos a la izquierda) EN EL NODO DERECHO

    def __buscar_minimo(self, nodo:NodoBin)->NodoBin:
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo """
    
    # Método añadido
    """ Método que busca el elemento más grande (nodos a la derecha) del subárbol izquierdo """
    def __buscar_max(self, nodo:NodoBin)->NodoBin:
        while nodo.der is not None:
            nodo = nodo.der
        return nodo
    
    # Método añadido
    """ Método que borra el elemento más grande del nodo izquierdo """
    def __borrar_max(self, nodo:NodoBin)->NodoBin:
        if nodo.der is not None:
            nodo.der = self.__borrar_max(nodo.der)
            return nodo
        else: return nodo.izq
    
    """
    MÉTODO PARA BORRAR EL ELEMENTO MÁS PEQUEÑO DEL NODO DERECHO
    
    def __borrar_minimo(self, nodo:NodoBin)->NodoBin:
        if nodo.izq is not None:
            nodo.izq = self.__borrar_minimo(nodo.izq)
            return nodo
        else: return nodo.der """
    
    """ 
    MÉTODO QUE USA EL ELEMENTO MÁS PEQUEÑO DEL SUBÁRBOL DERECHO

    def __borrar(self, nodo:NodoBin,dato):
        n,padre = self.buscar(nodo,dato)
        if n is None: 
            print('Elemento no encontrado')
            return None
        else:
            if n.der != None and n.izq != None:
                #Se aplica el criterio de eliminación con 2 hijos
                #Buscar el elemento más pequeño en el subárbol derecho
                minimo = self.__buscar_minimo(n.der)
                n.dato = minimo.dato
                n.der = self.__borrar_minimo(n.der)
            else:
                if n.izq is None: 
                    n = n.der
                else:
                    n = n.izq
                if padre.izq.dato == dato:
                    padre.izq = n
                elif padre.der.dato ==dato:
                    padre.der = n
        return dato """
    
    # Método añadido
    """Método que borra el elemento más grande del subárbol izquierdo """
    def __borrar(self, nodo: NodoBin, dato):
        n, padre = self.buscar(nodo, dato)
        if n is None:
            print("Elemento no encontrado")
            return None
        else:
            if n.der != None and n.izq != None:
                # Buscar el elemento más grande en el subárbol izquierdo
                maximo = self.__buscar_max(n.izq)
                n.dato = maximo.dato
                n.izq = self.__borrar_max(n.izq)
            else:
                if n.der is None:
                    n = n.izq
                else:
                    n = n.der
        
                if padre != None and padre.der != None and padre.der.dato == dato:
                    padre.der = n
                elif padre != None and padre.izq != None and padre.izq.dato == dato:
                    padre.izq = n
            return dato

    
    def borrar(self, dato):
        return self.__borrar(self.raiz,dato)

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
    arbol.insertar(92)

print("RECORRIDO EN INORDEN")
arbol.inorden()
encontrado, padre = arbol.buscar(arbol.raiz,536)
if encontrado is None: print('No se encontró')
else: print('Localizado: ',encontrado.dato)
eliminado = 93
print('Eliminado:',arbol.borrar(eliminado))
arbol.inorden()

""" print("RECORRIDO EN PREORDEN")
arbol.preorden()
encontrado, padre = arbol.buscar(arbol.raiz,56)
if encontrado is None: print("No se encontró")
else: print("Localizado: ", encontrado.dato)
eliminado = 65
print ("Eliminado: ", arbol.borrar(eliminado))
arbol.preorden() """

""" print("RECORRIDO EN POSORDEN")
arbol.posorden()
encontrado, padre = arbol.buscar(arbol.raiz,24)
if encontrado is None: print ("No se encontró")
else: print("Localizado: ", encontrado.dato)
eliminado = 22
print ("Eliminado: ", arbol.borrar(eliminado))
arbol.posorden() """
