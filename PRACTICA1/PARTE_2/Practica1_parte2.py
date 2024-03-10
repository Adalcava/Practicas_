'''
Adalberto Cabrera Vazquez 
No. boleta: 2023640791
Práctica 1
28/02/2024
'''

import numpy as np

#Definimos las atrices del ejemplo del sistemas de ecuaciones
B=np.array([[15],[5],[20]])         
A=np.array([[2,-4,-3],[1,5,-5],[4,2,67]])
a_inversa=np.linalg.inv(A)      #Sacamos la inversa 
X=np.dot(a_inversa,B)       #Multiplicamos la inversa por la matriz de A

print('Resolviendo el siguiente sistemas de ecuaciones con funciones de numpy:\n')
print('2x-4y-3z=15\nx+5y-5z=5\n4x+2y+67z=20')
print('\nLas soluciones son x='+str(X[0])+', y='+str(X[1])+', z='+str(X[2])+'\n') #Imprimimos las soluciones

comprobacion=np.dot(A,X)  # Esta operacion es para poder comprobar que las soluciones estan bien

print('Para comprobarlo vamos a realizar el producto punto de cada fila de A con el vector columna X y eso da:\n'+str(comprobacion))
#Vaciamos los valores de las matrices 
X=[] 
A=[]
B=[]
a_inversa=[]
print('\nAhora para resolver cualquier sistema de ecuaciones 3x3 vamos a ingresar los datos en una matriz\nEmpezamos con la matriz Anm:\n')
fila=[] 
for i in range(3):  #For para ingresar los valores en las matrices de 3x3
    fila=[]
    for j in range(3):
        numero=int(input('Ingrese el numero de la fila '+str(i+1)+' columna '+str(j+1)+': '))
        fila.append(numero)
        j+=1
    A.append(fila)
    print('\n')
    i+=1

print('\nAhora vamos con la matriz Bn:\n')

for i in range(3):  #For para ingresar los valores de la matriz 3x1
    fila=[]
    for j in range(1):
        numero=int(input('Ingrese el numero de la fila '+str(i+1)+' columna '+str(j+1)+': '))
        fila.append(numero)
        j+=1
    B.append(fila)
    i+=1
a_inversa=np.linalg.inv(A)  #Realizamos la inversa y posteriormente la multiplicación 
X=np.dot(a_inversa,B)
#Imprimimos las soluciones
print('\nLas soluciones son x='+str(X[0])+', y='+str(X[1])+', z='+str(X[2])+'\n')
