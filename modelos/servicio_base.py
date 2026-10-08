from abc import ABC, abstractmethod

class ServicioBase(ABC):

    @abstractmethod
    def mostrar_detalle(self, incluir_precio=True):
        pass