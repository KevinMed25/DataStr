

class MergeSort:

    def __init__(self, datos:list):
        self.data = []

    def mergesort(self, datos:list) -> list:
        n = len(datos)
        m = n//2
        if n > 1:
            l1 = datos[:m]
            l2 = datos[m:]
            return self.__merge(self.mergesort(l1), self._merge(self.mergesort(l2)))
        else:
                            
    def __merge(self, l1:list, L2:list)-> list:
        