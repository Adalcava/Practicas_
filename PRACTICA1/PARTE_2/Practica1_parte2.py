import numpy as np


B=np.array([[15],[5],[20]])
A=np.array([[2,-4,-3],[1,5,-5],[4,2,67]])
a_inversa=np.linalg.inv(A)
X=np.dot(a_inversa,B)

print('Resolviendo el siguiente sistemas de ecuaciones con funciones de numpy:\n')
print('2x-4y-3z=15\nx+5y-5z=5\n4x+2y+67z=20')
print('\nLas soluciones son x='+str(X[0])+', y='+str(X[1])+', z='+str(X[2])+'\n')

comprobacion=np.dot(A,X)

print('Para comprobarlo vamos a realizar el producto punto de cada fila de A con el vector columna X y eso da:\n'+str(comprobacion))

X=[]
A=[]
B=[]
a_inversa=[]
print('\nAhora para resolver cualquier sistema de ecuaciones 3x3 vamos a ingresar los datos en una matriz\nEmpezamos con la matriz Anm:\n')
fila=[]
for i in range(3):
    fila=[]
    for j in range(3):
        numero=int(input('Ingrese el numero de la fila '+str(i+1)+' columna '+str(j+1)+': '))
        fila.append(numero)
        j+=1
    A.append(fila)
    print('\n')
    i+=1

print('\nAhora vamos con la matriz Bn:\n')

for i in range(3):
    fila=[]
    for j in range(1):
        numero=int(input('Ingrese el numero de la fila '+str(i+1)+' columna '+str(j+1)+': '))
        fila.append(numero)
        j+=1
    B.append(fila)
    i+=1
a_inversa=np.linalg.inv(A)
X=np.dot(a_inversa,B)

print('\nLas soluciones son x='+str(X[0])+', y='+str(X[1])+', z='+str(X[2])+'\n')
