class Shellsort:

    def metodo_shellsort(datos:list)->None:
        n = len(datos)
        grupo = n
        
        while grupo > 1: #iteracion por grupo
            grupo = int(grupo/2)
            band = True
            while band==True: 
                band = False
                cont = 0
                while ((cont+grupo)<n):
                    if datos[cont] > datos[grupo + cont]:
                        datos[cont], datos[cont+grupo]=datos[cont+grupo], datos[cont]
                        band = True
                    cont += 1

    if __name__ == '__main__':
        arreglo = [15, 67, 8, 16, 44, 27, 12, 35,18,1,2]
        print(arreglo)
        metodo_shellsort(arreglo)
        print(arreglo)