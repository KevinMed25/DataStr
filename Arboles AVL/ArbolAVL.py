from NodoAVL import *

class ArbolAVL:
    def __init__(self,dato=None) -> None:
        self.__raiz = NodoAVL(dato=dato)
    
    @property
    def raiz(self):
        return self.__raiz
    @raiz.setter
    def raiz(self,dato):
        self.__raiz=dato

    def inorden(self):
        if self.raiz is not None:
            self.raiz.inorden()

    #------------------Rotaciones------------------------
    def __rotacion_ii(self, nodo:NodoAVL):
        #Establecer los apuntadores..
        padre = nodo.padre
        p = nodo #Nodo
        q = p.izq #Nodo1
        b = q.der #Hijo derecho de Nodo1

        #Ajustar hijos
        #Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.der == p: padre.der = q 
            else: padre.izq = q
        else: self.raiz = q
        #Reconstruir el arbol
        p.izq = b
        q.der = p
        #Reasignar Padres
        p.padre = q
        if b is not None: b.padre = p
        q.padre = padre
        #Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_dd(self, nodo:NodoAVL):
        #Establecer los apuntadores..
        padre = nodo.padre
        p = nodo #Nodo
        q = p.der #Nodo1
        b = q.izq #Hijo izquierdo de Nodo1

        #Ajustar hijos
        #Al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente
        if padre is not None:
            if padre.izq == p: padre.izq = q
            else: padre.der = q
        else: self.raiz = q
        #Reconstruir el arbol
        p.der = b
        q.izq = p

        #Reasignar Padres
        p.padre=q
        if b is not None: b.padre = p
        q.padre = padre
    
        #Establecer el factor de equilibrio
        p.f_eq = 0
        q.f_eq = 0

    def __rotacion_id(self, nodo:NodoAVL):
        padre = nodo.padre
        p = nodo #Nodo
        q = p.izq #Nodo1
        r = q.der #Nodo2
        b = r.izq
        c = r.der
     
        if padre is not None:
            if padre.der == p: padre.der = r
            else: padre.izq = r
        else: self.raiz = r

        #Reconstrucción del árbol
        q.der = b #Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo1
        p.izq = c #Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo
        #Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.izq = q
        r.der = p 
        #Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p
        
        #Ajusta los valores de los factores de equilibrio 
        if r.f_eq == -1: #Nodo2
             p.f_eq = 0 #Nodo
             q.f_eq = 1 #Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0 #Nodo
            q.f_eq = 0 #Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1 #Nodo
            q.f_eq =  0 #Nodo1
        r.f_eq = 0
    
    def __rotacion_di(self, nodo):
        padre = nodo.padre
        p = nodo #Nodo
        q = p.der #Nodo1
        r = q.izq #Nodo2
        b = r.der
        c = r.izq
        
        if padre is not None:
            if padre.izq == p: padre.izq = r
            else: padre.der = r
        else: self.raiz = r
        
        #Reconstrucción del árbol
        q.izq = b #Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo1
        p.der = c #Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo
        #Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo
        r.der = q
        r.izq = p 
        #Reasignación de padres
        r.padre = padre
        p.padre = r
        q.padre = r
        if b is not None: b.padre = q
        if c is not None: c.padre = p
        
        #Ajusta los valores de los factores de equilibrio 
        if r.f_eq == -1: #Nodo2
             p.f_eq = 0 #Nodo
             q.f_eq = 1 #Nodo1
        elif r.f_eq == 0:
            p.f_eq = 0 #Nodo
            q.f_eq = 0 #Nodo1
        elif r.f_eq == 1:
            p.f_eq = -1 #Nodo
            q.f_eq =  0 #Nodo1
        r.f_eq = 0
    
    def __balancear(self, nodo:NodoAVL):
        fe_actual = nodo.f_eq
        if fe_actual == 2:
            #Determinar la rotación
            fe_hijo_der = nodo.der.f_eq
            if fe_hijo_der == 0:
                pass
            elif fe_hijo_der == 1:
                self.__rotacion_dd(nodo)
                print("Aplicando rotación DD...")
            elif fe_hijo_der == -1:
                self.__rotacion_di(nodo)
                print("Aplicando rotación DI...")
        else:
            fe_hijo_izq = nodo.izq.f_eq
            if fe_hijo_izq == 0:
                pass
            elif fe_hijo_izq == -1:
                self.__rotacion_ii(nodo)
                print("Aplicando rotación II...")
            elif fe_hijo_izq == 1:
                self.__rotacion_id(nodo)
                print("Aplicando rotación ID...")

    def __recalcular_fe(self, nodo:NodoAVL):
        if nodo is not None:
            nodo.f_eq = NodoAVL.altura(nodo.der)-NodoAVL.altura(nodo.izq)
            if abs(nodo.f_eq) == 2:
                self.__balancear(nodo)
            else:
                self.__recalcular_fe(nodo.padre)
    def __inserta_ordenado(self, nodo:NodoAVL,dato):
        
        #if type(nodo.dato) is not int: n = nodo.dato.dato
        n = nodo.dato
        if dato < n:
            if nodo.izq is None:
                nodo.izq = NodoAVL(dato,None,None,nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.izq,dato)
        elif dato > n:
            if nodo.der is None:
                nodo.der = NodoAVL(dato,None,None, nodo)
                self.__recalcular_fe(nodo)
            else:
                self.__inserta_ordenado(nodo.der,dato)
    
    def insertar(self, dato):
        self.__inserta_ordenado(self.raiz,dato)

if __name__ == '__main__':
    arbol = ArbolAVL(58)
    arbol.insertar(43)
    arbol.insertar(75)
    arbol.insertar(86)
    arbol.insertar(65)
    arbol.inorden()
    arbol.insertar(70)
    arbol.insertar(67)
    arbol.insertar(73)
    arbol.insertar(93)
    arbol.insertar(69)
    arbol.insertar(25)
    arbol.insertar(66)
    arbol.insertar(68)
    arbol.insertar(47)
    arbol.insertar(62)
    arbol.insertar(10)
    arbol.insertar(60)
    #arbol.insertar(1000);    
    arbol.inorden()
