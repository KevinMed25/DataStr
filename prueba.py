class NodoDoble:
    def __init__(self, valor=None, previo=None, siguiente=None):
        self.valor = valor
        self.previo = previo
        self.siguiente = siguiente

class EditorSimple:
    def __init__(self):
        self.inicio = NodoDoble()
        self.final = NodoDoble()
        self.inicio.siguiente = self.final
        self.final.previo = self.inicio
        self.cursor = self.final

    def insertar(self, c):
        nuevo_nodo = NodoDoble(c, self.cursor.previo, self.cursor)
        self.cursor.previo.siguiente = nuevo_nodo
        self.cursor.previo = nuevo_nodo

    def borrar(self):
        if self.cursor == self.final:
            return
        self.cursor.previo.siguiente = self.cursor.siguiente
        self.cursor.siguiente.previo = self.cursor.previo

    def izquierda(self):
        if self.cursor.previo is not None:
            self.cursor = self.cursor.previo

    def derecha(self):
        if self.cursor.siguiente is not None:
            self.cursor = self.cursor.siguiente

    def imprimir(self):
        nodo_actual = self.inicio.siguiente
        cadena = ""
        while nodo_actual != self.final:
            cadena += nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
        print(cadena)
        cursor_pos = 0
        nodo_actual = self.inicio
        while nodo_actual != self.cursor:
            cursor_pos += 1
            nodo_actual = nodo_actual.siguiente
        print(" " * cursor_pos + "^")

if __name__ == "__main__":
    editor = EditorSimple()
    editor.insertar('H')
    editor.imprimir()
    editor.insertar('o')
    editor.imprimir()
    editor.insertar('l')
    editor.imprimir()
    editor.insertar('a')
    editor.imprimir()
    editor.izquierda()
    editor.imprimir()
    editor.insertar('o')
    editor.imprimir()
    # editor.derecha()
    editor.borrar()
    editor.imprimir()
    # editor.insertar(' ')
    # editor.insertar('M')
    # editor.insertar('u')
    # editor.insertar('n')
    # editor.insertar('d')
    # editor.insertar('o')
    # editor.derecha()
    # editor.borrar()
    # editor.imprimir()
