import array_stack as stack


S = stack.ArrayStack()                 		# contents: [ ]
S.push(5) 
print(S)                      			# contents: [5]
S.push(3)                        			# contents: [5, 3]
print('tamaño de pila', len(S))                 # contents: [5, 3];    outputs 2
print('Se eliminó el elemento',S.pop())         # contents: [5];       outputs 3
print('Pila vacía:',S.is_empty())              	# ontents: [5];       outputs False
print('Se eliminó el elemento', S.pop())        # contents: [ ];       outputs 5
print('Pila vacía:',S.is_empty()) 
#print('Se eliminó el elemento',S.pop())        # contents: [ ];       outputs True
S.push(7)                        # contents: [7]
S.push(9)                        # contents: [7, 9]
print('El tope de la pila es;',S.top())                   # contents: [7, 9];    outputs 9
S.push(4)                        # contents: [7, 9, 4]
print('tamaño de pila:',len(S))                    # contents: [7, 9, 4]; outputs 3
print('Se eliminó el elemento', S.pop())                   # contents: [7, 9];    outputs 4
S.push(6)                        # contents: [7, 9, 6]
S.push(8)                        # contents: [7, 9, 6, 8]
print('Se eliminó el elemento',S.pop())                   # contents: [7, 9, 6]; outputs 8