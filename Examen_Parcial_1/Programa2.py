'''
Adalberto Cabrera Vazquez 
2023640791
Examen 1
'''

import clases as cd

persona_1=cd.Contacto('Adalberto', '9984037473')
persona_2=cd.Contacto('Emilio', '5598472265')
persona_3=cd.Contacto('Itzel', '9981007887')

agenda = cd.Agenda()
agenda.agregarcontacto(persona_1)
agenda.agregarcontacto(persona_2)
agenda.agregarcontacto(persona_3)

input('Presiona cualquier tecla para continuar')

print("Lista de Peliculas:\n")
agenda.mostrarcontacto()

#Borrar un contacto de la persona 1

agenda.eliminarcontacto(persona_1)
input('\nPresiona cualquier tecla para continuar')
print("Eliminar el contacto 1:\n")
agenda.mostrarcontacto()

#Buscar contacto por nombre
input('\nPresiona cualquier tecla para continuar\n')
# Si se encontro
nombreencontrado = agenda.buscarnombre('Itzel')
if nombreencontrado:
    print(f"Si se encpntro a {nombreencontrado.nombre} en la agenda con el número {nombreencontrado.numero}\n")
else:
    print(f"No se encontró a la persona en la agenda")
#No se encontro
nombreencontrado = agenda.buscarnombre('Luis')
if nombreencontrado:
    print(f"Si se encpntro a {nombreencontrado.nombre} en la agenda, y tiene el número {nombreencontrado.numero}\n")
else:
    print(f"\nNo se encontró a la persona en la agenda")



#Buscar contacto por numero

input('\nPresiona cualquier tecla para continuar')
# Si se encontro
numeroencontrado = agenda.buscarnumero('5598472265')
if numeroencontrado:
    print(f"Si se encpntro a {numeroencontrado.nombre} en la agenda con el número {numeroencontrado.numero}")
else:
    print(f"No se encontró a la persona en la agenda")
#No se encontro
numeroencontrado = agenda.buscarnumero('556846258')
if numeroencontrado:
    print(f"Si se encpntro a {numeroencontrado.nombre} en la agenda, y tiene el número {numeroencontrado.numero}")
else:
    print(f"No se encontró a la persona en la agenda")
