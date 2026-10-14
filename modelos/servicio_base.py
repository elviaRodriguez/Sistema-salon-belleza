
from abc import ABC, abstractmethod

class ServicioBase(ABC):
    """
    Define el contrato que deben cumplir los servicios
    del salón de belleza.
    Las clases concretas deben implementar el método
    mostrar_detalle() para proporcionar información
    sobre el servicio.
    """
    @abstractmethod
    def mostrar_detalle(self, incluir_precio=True):
        pass
