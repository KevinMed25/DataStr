class QuickSort:
    def sort(self, arr):
        """
        Ordena el arreglo 'arr' utilizando el algoritmo de Quick Sort
        """
        self._quick_sort(arr, 0, len(arr)-1)
        
    def _quick_sort(self, arr, low, high):
        """
        Implementación recursiva del algoritmo de Quick Sort
        """
        if low < high:
            # se divide el arreglo y se obtiene un índice 'pivote'
            p = self._partition(arr, low, high)
            
            # se ordenan recursivamente las sub-listas antes y después del pivote
            self._quick_sort(arr, low, p-1)
            self._quick_sort(arr, p+1, high)
    
    def _partition(self, arr, low, high):
        """
        Particiona el arreglo utilizando el último elemento como pivote
        """
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                # se intercambian los elementos
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # se coloca el pivote en su posición final y se devuelve su índice
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

if __name__ == '__main__':
    arreglo = [15,67,8,16,44,27,12,35,18,1,2]
    print(arreglo)
    qs = QuickSort()
    qs.sort(arreglo)
    print(arreglo)