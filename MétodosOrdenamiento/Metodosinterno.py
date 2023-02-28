
 
class MetodosInterno:
    
    def __init__(self) -> None:
        pass

    def burbuja_menor(self, datos:list) -> None:
        """
        Ordena los datos en orden ascendente llevando el elemento más pequño a la izquierda
        """
        n = len(datos)
        for i in range(n - 1): #Ciclo de iteraciones
            for j in range(n - 1, i, -1): #Ciclo de comparaciones
                if datos[j-1]> datos[j]:
                    datos[j], datos[j-1] = datos[j -1], datos[j]

    def burbuja_mayor(self, datos:list) -> None:
        """
        Ordena los datos en orden ascendente llevando el elmento más grande a la derecha
        """
        n = len(datos)
        for i in range(n - 1): #Ciclo de iteraciones
            for j in range(n - i, -1): #Ciclos de comparaciones
                if datos[j] > datos[j + 1]:
                    datos[j], datos[j+1] = datos[j+1], datos[j]

    def insercion(self, datos:list) -> None:
        """ 
        Método de inserción directa para ordenamiento ascendente
        """
        n = len(datos)
        for i in range(1,n):
            aux = datos[i]
            k = i - 1

            while (k>=0 and aux<datos[k]):
                datos[k+1] = datos[k]
                k-=1
            datos[k+1]= aux
