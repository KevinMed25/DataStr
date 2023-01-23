import array_queue as queue

Q = queue.ArrayQueue() 

# Tenemos disponibles las siguientes instrucciones:
# 32 enqueue operations
# 15 dequeue operations, de las cuales 5 marcan error debido a que la cola este vacia y se ignoran
# 10 first operat0ions

# Entonces, dependiendo del orden de las operaciones se tendrá un tamaño final
# de la cola distinto, haré tres versiones:

# Version 1:

# Metemos 10 elementos a la cola
Q.enqueue(1)
 # Las operaciones first se iran incorporando de froma aleatoria, ya que no afectan al tamaño de la pila
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(8)
Q.enqueue(9)
Q.enqueue(10)
print(Q)

# Sacamos 15 elementos de la cola
# Las operaciones first no afectan en el tamaño de la cola, asi que podemos colocarlas donde sea
print("utilizamos 15 instrucciones dequeue: ")
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())
Q.dequeue()
print("Sacamos el primer elemento en la cola: ")
print(Q.first())

print("\n Usamos las otras 5 instrucciones de dequeue, y nos marca vacio: ")
Q.dequeue() # A partir de aqui los siguiente enqueue se ignoran porque la cola estara vacia
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()

print(Q)
print("\n Utilizamos las 22 instrucciones que nos quedan de enqueue: ")
# Terminamos de gastar las 22 instrucciones enqueue que nos quedan:
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(8)
Q.enqueue(9)
Q.enqueue(10)
Q.enqueue(11)
Q.enqueue(12)
Q.enqueue(13)
Q.enqueue(14)
Q.enqueue(15)
Q.enqueue(16)
Q.enqueue(17)
Q.enqueue(18)
Q.enqueue(19)
Q.enqueue(20)
Q.enqueue(21)
Q.enqueue(22)
print(" ")
print(Q)
print( "\nEl Tamaño de la cola es: ")
print(Q.__len__())








