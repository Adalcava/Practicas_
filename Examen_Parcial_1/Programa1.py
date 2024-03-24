'''
Adalberto Cabrera Vazquez 
2023640791
Examen 1
'''

import clases as cd
#Creo las peliculas
pelicula_1=cd.Pelicula('Titanic', '2000', '210', 'AB', 'Adalberto Cabrera', 'Leonardo Dicaprio, Luis Diaz', 'Pelicula de un barco hundiendose') 
pelicula_2=cd.Pelicula('Interestelar', '2005', '180', 'RC', 'Christofer Nolan', 'Angel Alvarez, Julieta Angel', 'Pelicula del espacio')
pelicula_3=cd.Pelicula('Los increibles', '2004', '120', 'B', 'Adalberto Cabrera', 'Miguel, Angel, Paola', 'Peliucla de superheroes')
#las guardo en el catalogo
catalogo = cd.Catalogo()
catalogo.agregarpelicula(pelicula_1)
catalogo.agregarpelicula(pelicula_2)
catalogo.agregarpelicula(pelicula_3)
#las imprimo
print("Lista de Peliculas:")
catalogo.mostrarlistapelis()