from Stack import Stack

def validation(string):
    
    s = Stack()

    for element in string:
        # insertamos los los caracteres a la pila
        if element == '{'or element == '[' or element == '(':
            s.push(element)
        # Si se encuentra un un parentesis/corchete/llave de cierre, entonces:
        if element == '}'or element == ']' or element == ')':
            # Verificamos que no este vacía:
            if s.is_empty():
                return False
            Aux = s.pop()
            # comparamos la variable element con un auxiliar para validar lo siguiente:
            if (Aux == '{' and element != '}') or (Aux == '[' and element != ']') or (Aux == '(' and element != ')'):
                return False
            
    return s.is_empty()

# Ejemplos pruba:
Exp1 = '((()))'     # Se espera true
Exp2 = '[]{()[()]}' # Se espera true
Exp3 = '{[}()(]]'   # Se espera flase
Exp4 = '()()()[{[]}]'   # Se espera true
Exp5 = '{[](]}))'   # Se espera false
Exp6 = '{[()]}'     # Se espera true

print(validation(Exp1))
print(validation(Exp2))
print(validation(Exp3))
print(validation(Exp4))
print(validation(Exp5))
print(validation(Exp6))