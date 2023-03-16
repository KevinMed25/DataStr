from manejo_archivos import *

class MetodosExterno:
    def __init__(self) -> None:
        pass
    def __fusionar(self,ruta_f1,ruta_f2,ruta,part):
        r1, r2, b1, b2 = 0,0,True,True
        f1 = abrir_archivo(ruta_f1,'r')
        f2 = abrir_archivo(ruta_f2,'r')
        f3 = abrir_archivo(ruta,'w')
        r1 = f1.readline()
        if r1 != '':b1=False
        r2 = f2.readline()
        if r2 != '':b2=False
        while (r1!='' or not b1) and (r2!='' or not b2):
            k=0
            l=0
            while (k < part and not b1 and l < part and not b2):
                if int(r1) <= int(r2):
                    if r1[-1]!='\n':r1+='\n'
                    f3.write(r1)
                    b1 = True
                    k+=1
                    r1=f1.readline()
                    if r1 != '':b1=False
                else:
                    if r2[-1]!='\n':r2+='\n'
                    f3.write(r2)
                    b2 = True
                    l+=1
                    r2=f2.readline()
                    if r2 != '':b2=False
            if (k<part):
                while(k<part and not b1):
                    if r1[-1]!='\n':r1+='\n'
                    f3.write(r1)
                    b1=True
                    k+=1
                    r1 = f1.readline()
                    if r1 != '':b1=False
            if (l<part):
                while(l<part and not b2):
                    if r2[-1]!='\n':r2+='\n'
                    f3.write(r2)
                    b2=True
                    l+=1
                    r2 = f2.readline()
                    if r2 != '':b2=False
        if not b1:
            if r1[-1]!='\n':r1+='\n'
            f3.write(r1)
        if not b2:
            if r2[-1]!='\n':r2+='\n'
            f3.write(r2)
        while True:
            r1 = f1.readline()
            if r1=='':break
            if r1[-1]!='\n':r1+='\n'
            f3.write(r1)
        while True:
            r2 = f2.readline()
            if r2=='':break
            if r2[-1]!='\n':r2+='\n'
            f3.write(r2)
            
        f1.close()
        f2.close()
        f3.close()
        
    def __particionar(self,ruta,part):
        """Particiona el archivo con respecto al número de partes 
            indicadas en part"""
        archivo = abrir_archivo(ruta,'r')
        f1 = abrir_archivo('f1.txt','w')
        f2 = abrir_archivo('f2.txt','w')
        while True:
            k=0
            while k<part:
                linea=archivo.readline()
                if linea=='': break
                else: f1.write(linea)
                k+=1
            l=0
            while l<part:
                linea=archivo.readline()
                if linea=='': break
                else: f2.write(linea)
                l+=1
            if linea=='':break
        archivo.close()
        f1.close()
        f2.close()
    
    def mezcla_directa(self,ruta):
        n = tamaño_archivo(ruta)
        part = 1
        while part<n:
            self.__particionar(ruta,part)
            self.__fusionar('f1.txt','f2.txt',ruta,part)
            part*=2
        