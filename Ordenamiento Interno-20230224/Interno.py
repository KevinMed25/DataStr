class MetodosInterno:
    def __init__(self) -> None:
        pass

    def burbuja_menor(self,datos:list)->None:
        """
        Ordena los datos en orden ascendente llevando el elemento más
        pequeño a la izquierda
        """
        n = len(datos)
        for i in range(n-1):#ciclo de iteraciones
            for j in range(n-1,i,-1):#ciclo de comparaciones
                if datos[j-1]>datos[j]:
                    datos[j], datos[j-1] = datos[j-1], datos[j]
    
    def burbuja_mayor(self,datos:list)->None:
        """
        Ordena los datos en orden ascendente llevando el elemento más
        grande a la derecha
        """
        n = len(datos)
        for i in range(n-1):#ciclo de iteraciones
            for j in range(n-i-1):#ciclo de comparaciones
                if datos[j]>datos[j+1]:
                    datos[j], datos[j+1] = datos[j+1], datos[j]
    
    def insercion(self, datos:list)->None:
        """Método de inserción directa para ordenamiento ascendente"""
        n = len(datos)
        for i in range(1,n):
            aux = datos[i]
            k = i-1
            while(k>=0 and aux<datos[k]):
                datos[k+1] = datos[k]
                k-=1
            datos[k+1] = aux

    def __crea_secuencia_grupos(self,num_datos:float,tipo:int)->list:
        """Determina el número de grupos para el Shellsort
        con respecto a una funcion establecida"""
        num=1
        secuencia_grupos = []
        while True:
            if tipo == 1:
                num_grupos = 2**num - 1
            elif tipo == 2:
                num_grupos = 3*(num-1) + 1
            elif tipo == 3:
                num_grupos = int((num - 1)/3)
            if num_grupos >= num_datos: break
            num+=1
            secuencia_grupos.insert(0,num_grupos)
        return secuencia_grupos
    
    def shellsort(self, datos:list, funcion:int)->None:
        """Algoritmo de ordenamiento Shell"""
        n = len(datos)
        secuencia_grupos = self.__crea_secuencia_grupos(n,funcion)
        for salto in secuencia_grupos:
            band = True
            while band:
                band = False
                i=0
                while (salto+i) < n:
                    if datos[i] > datos[salto+i]:
                        datos[i], datos[salto+i] = datos[salto+i], datos[i]
                        band = True
                    i+=1

    def __merge(self,l1:list,l2:list)->list:
        n1, n2 = len(l1), len(l2)
        i, j = 0, 0
        lista = []
        while True:
            if l1[i]<l2[j]:
                lista.append(l1[i])
                i+=1
            else:
                lista.append(l2[j])
                j+=1
            if i==n1: #La lista l1 se quedó sin elementos
                lista.extend(l2[j:])
                break
            elif j==n2: #La lista l2 se quedó sin elementos
                lista.extend(l1[i:])
                break
        return lista

    def mergesort(self,datos:list)->list:
        n = len(datos)
        if n>1:
            m = n//2
            l1 = datos[:m]
            l2 = datos[m:]
            return self.__merge(self.mergesort(l1),self.mergesort(l2))
        else:
            return datos

    def __posiciona_quicksort(self,ini:int,fin:int)->int:
        pass
    
    def quicksort(self, datos:list)->None:
        pass
