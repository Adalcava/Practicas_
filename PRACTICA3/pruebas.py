from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

class MiClaseConcreta(MiClaseAbstracta):
    def metodo_abstracto(self):
        print("Implementación del método abstracto")

print(issubclass(MiClaseAbstracta, ABC))  # True
print(issubclass(MiClaseConcreta, ABC))   # True