import Stack as Stack

pila_S = Stack.Stack()
pila_T = Stack.Stack()

pila_S.push(6)
pila_S.push(7)
pila_S.push(8)
pila_S.push(9)
pila_S.push(10)

pila_T.push(1)
pila_T.push(2)
pila_T.push(3)
pila_T.push(4)
pila_T.push(5)

pila_T.display()
pila_S.display()

def intercambiar(Pila_S, Pila_T):
