from modelos.servicio_cabello import ServicioCabello
from modelos.servicio_unas import ServicioUnas
from modelos.excepciones import PrecioInvalidoError
from modelos.servicio import Servicio
from modelos.catalogo_servicios import CatalogoServicios

servicio = Servicio("Corte de cabello", 15.00)

try:
    servicio.precio = -10
except PrecioInvalidoError as error:
    print("Error:", error)

print(servicio.mostrar_detalle())

# Creando objetos de las clases hijas
servicio1 = ServicioCabello("Corte de cabello", 15, "Rizado")
servicio2 = ServicioUnas("Manicura", 12, "Semipermanente")

# Lista de servicios
servicios = [servicio1, servicio2]


# POLIMORFISMO:
# Invocamos el mismo método en objetos de diferentes clases.
# Cada objeto ejecuta su propia implementación.
for servicio in servicios:
    print(servicio.mostrar_detalle())
    print(servicio.mostrar_detalle(False))

catalogo = CatalogoServicios()

catalogo.agregar_servicio(
    ServicioCabello("Corte de cabello", 15, "Rizado")
)

catalogo.agregar_servicio(
    ServicioUnas("Manicura", 12, "Semipermanente")
)

print("CATÁLOGO DE SERVICIOS")
catalogo.mostrar_servicios()

 

