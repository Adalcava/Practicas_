class Alumno:
    def __init__(self, nombre: str, boleta: str, edad: int) -> None:
        self.nombre = nombre
        self.boleta = boleta
        self.edad = edad
    
    def habla(self, msj):
        print(f"Me llamo {self.nombre} y digo {msj}")
        
    def __str__(self) -> str:
        return f"Hola, me llamo {self.nombre} mi boleta es {self.boleta} y tengo {self.edad} años."

pavel = Alumno('Pavel', edad=19, boleta='72635476723654')
pavel.habla("Hola")
print(pavel)