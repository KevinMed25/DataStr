
def ordenar(path1, path2, path3):
    f1 = open(path1, "r")
    f2 = open(path2, "r")
    f3 = open(path3, "w")
    
    while True:
        dato1 = f1.readline()
        dato2 = f2.readline()
        if dato1 == "":
            #El archivo 1 ya no tiene más datos
            f3.write("\n")
            while dato2 != "":
                dato2 = f2.readline()
                f3.write(dato2)
            break
        
        elif dato2 == "":
            #El archivo 2 ya no tiene más datos
              #El archivo 1 ya no tiene más datos
            f3.write("\n")
            while dato1 != "":
                dato1 = f1.readline()
                f3.write(dato1)
            break
            
        elif int(dato1) <= int(dato2):
            f3.write(dato1 + "\n")
            dato1 = f1.readline()
        else:
            f3.write(dato2 + "\n")
            dato2 = f2.readline()

ordenar("ManejoArchivos/Lista1.txt", "ManejoArchivos/Lista2.txt", "ManejoArchivos/Lista3.txt")

