class Contacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def buscar_contacto_por_nombre(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

# Uso de las clases
mi_agenda = Agenda()
mi_agenda.agregar_contacto(Contacto("Juan", "123456789"))
mi_agenda.agregar_contacto(Contacto("María", "987654321"))

nombre_buscar = "María"
contacto_encontrado = mi_agenda.buscar_contacto_por_nombre(nombre_buscar)

if contacto_encontrado:
    print(f"Se encontró a {contacto_encontrado.nombre} en la agenda con el número {contacto_encontrado.numero}")
else:
    print(f"No se encontró a {nombre_buscar} en la agenda")