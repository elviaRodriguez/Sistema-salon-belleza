
from modelos.servicio import Servicio


class ServicioCabello(Servicio):
    """
    Representa un servicio de cabello del salón de belleza.

    Hereda los atributos nombre y precio de la clase Servicio.
    Incorpora el atributo tipo_cabello para identificar
    el tipo de cabello al que está dirigido el servicio.

    Sobrescribe mostrar_detalle() para incluir información
    específica del servicio de cabello.
    """

    def __init__(self, nombre, precio, tipo_cabello="General"):
        # Inicializa los atributos heredados nombre y precio.
        super().__init__(nombre, precio)

        # Inicializa el atributo propio de la clase.
        self.tipo_cabello = tipo_cabello

    # POLIMORFISMO:
    # Sobrescribe el método heredado para agregar
    # información específica sobre el tipo de cabello.
    def mostrar_detalle(self, incluir_precio=True):
        return (
            f"{super().mostrar_detalle(incluir_precio)}, "
            f"Tipo de cabello: {self.tipo_cabello}"
        )
