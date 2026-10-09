from abc import ABC, abstractmethod
# ABSTRACCIÓN:
# Definimos una clase abstracta que establece el método
# que deben implementar los servicios del salón de belleza.

class ServicioBase(ABC):

    @abstractmethod
    def mostrar_detalle(self, incluir_precio=True):
        pass