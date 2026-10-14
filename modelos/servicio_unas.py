
from modelos.servicio import Servicio


class ServicioUnas(Servicio):
    """
    Representa un servicio de uñas del salón de belleza.

    Hereda los atributos nombre y precio de la clase Servicio.
    Incorpora el atributo tipo_esmalte para identificar
    el esmalte utilizado en el servicio.

    Sobrescribe mostrar_detalle() para incluir información
    específica del servicio de uñas.
    """

    def __init__(self, nombre, precio, tipo_esmalte="Tradicional"):
        # Inicializa los atributos heredados nombre y precio.
        super().__init__(nombre, precio)

        # Inicializa el atributo propio de la clase.
        self.tipo_esmalte = tipo_esmalte

    # POLIMORFISMO:
    # Sobrescribe el método heredado para agregar
    # información específica sobre el tipo de esmalte.
    def mostrar_detalle(self, incluir_precio=True):
        return (
            f"{super().mostrar_detalle(incluir_precio)}, "
            f"Tipo de esmalte: {self.tipo_esmalte}"
        )
