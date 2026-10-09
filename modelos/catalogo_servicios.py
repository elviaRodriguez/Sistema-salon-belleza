from modelos.servicio import Servicio

class CatalogoServicios:

    def __init__(self):
        # AGRUPACIÓN DE CLASES:
        # Almacenamos diferentes objetos de tipo Servicio
        # dentro de una misma colección.
        self.servicios = []

    def agregar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise TypeError(
                "Solo se pueden agregar objetos de tipo Servicio."
            )
        self.servicios.append(servicio)

    def mostrar_servicios(self):
        for servicio in self.servicios:
            print(servicio.mostrar_detalle())

            