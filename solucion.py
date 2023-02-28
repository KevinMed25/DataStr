class NodoDoble:
    
    def __init__(self, dato = None, anterior = None, siguiente = None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

class EditorSimple:
    
    def __init__(self):
        self.inicio = NodoDoble()
        self.final = NodoDoble()
        self.inicio.siguiente = self.final
        self.final.anterior = self.inicio
        #Añadinmos al cursor
        self.cursor = self.inicio
    def izquierda(self):
        #Si el nodo anterior no está vació avazamos a la izquierda
        if self.cursor.anterior is not None:
            self.cursor = self.cursor.anterior

    def derecha(self):
        #Si el nodo siguiente no está vació avanzamos a la derecha
        if self.cursor.siguiente is not None:
            self.cursor = self.cursor.siguiente
    
    def insertar(self, dato):
        nodo_nuevo = NodoDoble(dato,self.cursor, self.cursor.siguiente)
        self.cursor.siguiente = nodo_nuevo
        self.cursor= nodo_nuevo
    
    def borrar(self):
        #verificamos que no esté en el nodo final:
        if self.cursor == self.final:
            return
        # if self.cursor.anterior == None:
        #     self.cursor.anterior = None
        #     self.cursor.anterior.siguiente = self.cursor.siguiente
        self.cursor.anterior.siguiente = self.cursor.siguiente
        self.cursor.siguiente.anterior = self.cursor.anterior

    def imprimir(self):

        nodo_actual = self.inicio.siguiente
        cadena = ""

        #Impresión de la cadena
        while nodo_actual != self.final:
            cadena += nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        print(cadena)

        #Impresión del cursor
        posicion_cursor = -2
        nodo_actual = self.inicio
        while nodo_actual != self.cursor.siguiente:
            posicion_cursor += 1
            nodo_actual = nodo_actual.siguiente
        print(" " * posicion_cursor + "^")

if __name__ == "__main__":

    editor = EditorSimple()

    editor.insertar('H')
    editor.insertar('o')
    editor.insertar('H')
    editor.insertar('o')
    editor.imprimir()
    editor.borrar()
    editor.imprimir()
    editor.borrar()
    editor.borrar()
    editor.imprimir()