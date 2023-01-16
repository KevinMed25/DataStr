
class Stack:

    def __init__(self):
        self.data = []

    # Para saber si la pila esta vacía:
    def is_empty(self):
        return len(self.data) == 0

    # Para saber el número de elementos en la pila:
    def __len__(self):
        return len(self.data)

    # Para insertar un elemento:
    def push(self, element):
        self.data.append(element)
    
    # Para sacar un elemento:
    def pop(self):
        if self.is_empty():     # Si la pila esta vacía:
            print("The stack is empty")
            return None 
        return self.data.pop()  # Usamos método pop para retornar el último elemento
    
    # Para saber el último elemento:
    def top(self):
        if self.is_empty():
            print("The stack is empty")
            return None
        return self.data[-1]

    # Para limpiar la pila:
    def clean(self):
        del self.data[:]
    
    # Para mostrar los elementos de la pila:
    def display(self):
        print("The elements in the stack are: ")
        print(self.data)

