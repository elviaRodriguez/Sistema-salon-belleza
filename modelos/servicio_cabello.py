from modelos.servicio import Servicio

class ServicioCabello(Servicio):

    def __init__(self, nombre, precio, tipo_cabello):
        super().__init__(nombre, precio)
        self.tipo_cabello = tipo_cabello

    def mostrar_detalle(self, incluir_precio=True):
        return (
            f"{super().mostrar_detalle(incluir_precio)}, "
            f"Tipo de cabello: {self.tipo_cabello}"
        )

    
