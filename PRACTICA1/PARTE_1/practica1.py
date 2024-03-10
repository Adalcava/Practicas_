'''
Adalberto Cabrera Vazquez 
No. boleta: 2023640791
Práctica 1

'''

import numpy as np   #Libreria numpty
import os              #Libreria paralimpiar la pantalla
import statistics as st     #Libreria para realizar la desviacion estandar
import random               #Libreria para poner datos pseudoaleatorios

#Funcion 'datos' que me sirve para la recopilacion de datos que va a ingresar el usuario
def datos(a, b):                
    for i in range(a):
        numero=int(input('Ingrese el numero de la posición '+str(i)+': '))
        b.append(numero)
        i=i+1

#Funcio 'datos_azar' que me sirve para la recopilacion de datos al azar con base a la cantidad de elementos 
# que ingrese el usuario
def datos_azar(c, d):
    for i in range(c):                  #for para la recopilacion de datos
        numero=random.randint(0,100)    #Asignacion de datos al azar
        d.append(numero)
        i=i+1


flag=False
while flag==False:     # While para saber si puso una opcion de la lista o no 
    print("Mi programa\n1. Media Aritmética\n2. Desviación Estándar\n3. Burbuja\n4. Salir\n\n")
    opc=input("Escriba su opcion: ")
    if opc=='1' or opc=='2' or opc=='3' or opc=='4':   # Verifica que hayas puesto una de la lista
        
        if opc=='1':    # Elegiste la opcion 1
            muestra=int(input('\nFavor de ingresar el numero de muestras:'))
            print('\n')
            elemento=[]
            datos(muestra,elemento)    #llama la funcion datos y asigna datos
            
            media=sum(elemento)/muestra     #Realiza la media de los datos
            print('\nLa media aritmetica del arreglo que ingreso es de: '+str(media))
        elif opc=='2':      # Elegiste la opcion 2
            
            muestra=int(input('\nFavor de ingresar el numero de muestras:'))
            print('\n')
            elemento=[]
            datos(muestra,elemento)     #llama la funcion datos y asigna datos
            
            desviacion=st.stdev(elemento)       #Realiza la desviacin de los datos
            print('\nLa desviacion estandar del arreglo que ingreso es de: '+str(desviacion))
        
        elif opc=='3':      #Elegiste la opcion 3
            muestra=int(input('\nFavor de ingresar el numero de muestras:'))
            print('\n')
            elemento=[]
            datos_azar(muestra,elemento)    #Llama la funcion de datos_azar y asigna datos

            print('Su arreglo desordenado es:') 
            print(elemento)
            

            for i in range(muestra-1):          #Metodo de burbuja para ordenar datos
                termino=False                   #Saber si ya estan todos los datos ordenados
                for j in range(muestra-1):
                    if elemento[j]<elemento[j+1]:               #Si un elemento es menor al siguiente del arreglo
                        elemento[j],elemento[j+1]=elemento[j+1],elemento[j]   #Intercambia los datos
                    else:
                        termino=True            #Ya estan ordenados
                    j=j+1
                i=i+1
            print('Su arreglo ordenado demayor a menor es:')   
            print(elemento)

        elif opc=='4':          #Elegiste la opcion 4
            print('Gracias por hacer uso del código, hasta la próxima')
        
        flag=True   
    else:       #Si no pone una opcion de la lista, limpia pantalla y vuelve a imprimir al principio
        flag=False
        os.system('cls')





