'''
Cabrera Vazuez Adalberto
2023640791
'''

class Pelicula:
    def __init__(self, titulo:str, año:str, duracion:str, clasificacion:str, director:str, actores:str, descripcion:str) -> None:
        self.__titulo=titulo
        self.__año = año
        self.__duracion = duracion
        self.__clasificacion = clasificacion
        self.__director = director
        self.__actores = actores
        self.__descripcion = descripcion
        
    def __str__(self) -> str:
        return f'Titulo: {self.__titulo} -- Año: {self.__año} -- Duracion (min): {self.__duracion} -- Clasificacion: {self.__clasificacion} -- Director: {self.__director} -- Actores principales: {self.__actores} -- Descripcion: {self.__descripcion}'
    
class Catalogo:
    def __init__(self ) -> None:
        self.__listapelis = []
        
    def agregarpelicula(self, elemento):
        self.__listapelis.append(elemento)
    
    def mostrarlistapelis(self):
        for elemento in self.__listapelis:
            print("")
            print(elemento)
    
class Contacto:
    def __init__(self, nombre:str, numero:str) -> None:
        self.__nombre= nombre
        self.__numero= numero
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def numero(self):
        return self.__numero
    
    def __str__(self) -> str:
        return f'Nombre: {self.__nombre} -- Numero: {self.__numero}'
    
class Agenda:
    def __init__(self ) -> None:
        self.__listanumeros = []
        
    def agregarcontacto(self, otro):
        self.__listanumeros.append(otro)
    
    def eliminarcontacto(self, otro):
        self.__listanumeros.remove(otro)
    
    def mostrarcontacto(self):
        for otro in self.__listanumeros:
            print("")
            print(otro)
            
    def buscarnombre(self,nombre):
        for otro in self.__listanumeros:
            if otro.nombre == nombre:
                return otro
        return None
    
    def buscarnumero(self, numero):
        for otro in self.__listanumeros:
            if otro.numero == numero:
                return otro
        return None
    
    