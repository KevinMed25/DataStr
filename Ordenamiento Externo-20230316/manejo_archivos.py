import os.path as ruta_archivo

def abrir_archivo(ruta:str,modo:str='r'):
    try:
        check_file = ruta_archivo.isfile(ruta)
        if check_file and modo=='r':
            f = open(ruta,modo)
        elif check_file==False and modo=='r':
            print('El archivo no existe. Se creará uno nuevo')
            f = open(ruta,'w')
        else:
            f = open(ruta,modo)
        return f
    except FileNotFoundError:
        print('No se encontró el archivo')
    except:
        pass

def tamaño_archivo(ruta):
    """Determina el número de elementos en el archivo"""
    with open(ruta) as archivo:
        total_lineas = sum(1 for linea in archivo)
    return total_lineas

def cerrar_archivo(archivo):
    archivo.close()
