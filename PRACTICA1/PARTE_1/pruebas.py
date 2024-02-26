import numpy as np

'''def datos(a, b):
    for i in range(a):
        numero=int(input('Ingrese el numero de la posición '+str(i)+': '))
        b.append(numero)
        i=i+1'''
fila=[]
B=[]
for i in range(3):
    fila=[]
    for j in range(3):
        numero=int(input('Ingrese el numero de la fila '+str(i+1)+' columna '+str(j+1)+': '))
        fila.append(numero)
        j+=1
    B.append(fila)
    i+=1
    
print(B)
