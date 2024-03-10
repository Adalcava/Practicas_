class Alumno:
    
    def __init__(self, nombre:str, boleta:str, edad:int) -> None:
        self.__nombre = nombre
        self.__boleta = boleta
        self.__edad = edad
    
    @property
    def boleta(self):
        return self.__boleta
    
    @boleta.setter
    def boleta(self, nuevaBoleta:str):
        self.__boleta = nuevaBoleta   
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad:int):
        self.__edad = edad
    
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre:str):
        if(len(nuevoNombre) != 0):
            self.__nombre = nuevoNombre
          
    
        
alumno1 = Alumno("Jose Luis", "202456779", 25)

alumno1.nombre = "asas"
print(alumno1.edad)

'''class Persona:
    def __init__(self, nombre:str, edad:int)->None:
        self.__nombre=nombre
        self.__edad= edad
    
    def presentar(self):
        print(f'Hola mi nombre es{self.__nombre} y tengo {self.__edad} años')
        
class Alumno(Persona):
    def __init__(self, nombre:str, edad:int ,peso:str)->None:
        super().__init__(nombre,edad)
        self.__peso= peso

    def __str__(self)->str:
        return f'Hola mi nombre es {self.__peso}'
    
    
alumno1=Alumno("Jose luis", 20, '12')
alumno1.presentar()
print(alumno1)'''