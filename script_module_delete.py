from os import walk
import shutil

def ls(ruta = 'D:\Estudios'):
    # listaarchivos = []
    for (a, b, archivos) in walk(ruta):
        for c in b:
            if(c == 'node_modules'):
                shutil.rmtree('{}\{}'.format(a,c))
print(ls())