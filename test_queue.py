import array_queue as queue


Q = queue.ArrayQueue()              # contents: [ ]
Q.enqueue(5) 
print(Q)                       # contents: [5]
Q.enqueue(3)
print(Q)                        # contents: [5, 3]
print('tamaño de cola', len(Q))                    # contents: [5, 3];    outputs 2
print('Se eliminó el elemento',Q.dequeue())                   # contents: [5];       outputs 3
print('Cola vacía:',Q.is_empty())              # contents: [5];       outputs False
print('Se eliminó el elemento', Q.dequeue())                   # contents: [ ];       outputs 5
print('Cola vacía:',Q.is_empty()) 
#print('Se eliminó el elemento',S.pop())             # contents: [ ];       outputs True
print(Q)
Q.enqueue(7)                        # contents: [7]
print(Q)
Q.enqueue(9)
print(Q)                        # contents: [7, 9]
print('El primer elemento de la cola es;',Q.first())                   # contents: [7, 9];    outputs 9
Q.enqueue(4)
print(Q)                        # contents: [7, 9, 4]
print('tamaño de cola:',len(Q))                    # contents: [7, 9, 4]; outputs 3
print('Se eliminó el elemento', Q.dequeue())                   # contents: [7, 9];    outputs 4
Q.enqueue(6)
print(Q)                        # contents: [7, 9, 6]
Q.enqueue(8)
print(Q)                        # contents: [7, 9, 6, 8]
print('Se eliminó el elemento',Q.dequeue())                   # contents: [7, 9, 6]; outputs 8
print(Q)