class NodoBin:
    def __init__(self,dato=None,izq=None,der=None):
        self.__dato = dato
        self.__izq = izq
        self.__der = der

    @property
    def dato(self):
        return self.__dato
    @dato.setter
    def dato(self, dato):
        self.__dato = dato
    @property
    def izq(self):
        return self.__izq
    @izq.setter
    def izq(self, izq):
        self.__izq=izq
    @property
    def der(self):
        return self.__der
    @der.setter
    def der(self, der):
        self.__der=der
    #Recorridos del árbol
    def inorden(self):
        if self.izq != None:
            self.izq.inorden()
        print(self.dato)
        if self.der != None:
            self.der.inorden()
    def posorden(self):
        if self.izq != None:
            self.izq.posorden()
        if self.der != None:
            self.der.posorden()
        print(self.dato)
         
    def preorden(self):
        print(self.dato)
        if self.izq != None:
            self.izq.preorden()
        if self.der != None:
            self.der.preorden()
        
    