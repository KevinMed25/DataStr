from Interno import MetodosInterno

if __name__ == '__main__':
    arreglo = [8780, 8439, 9698, 5319, 6145, 2166, 7116, 6236,
        2404, 7432, 7868, 3513, 5310, 8054, 4935, 8034]

    arreglo = [15, 6, 8, 2, 1]
    metodos = MetodosInterno()

    print(arreglo)
    arreglo_ordenado = metodos.burbuja_mayor(arreglo)
    if arreglo_ordenado is not None:
        print(arreglo_ordenado)
    else:
        print(arreglo)








