from modelos.servicio_cabello import ServicioCabello
from modelos.servicio_unas import ServicioUnas

# Creando objetos de las clases hijas
servicio1 = ServicioCabello("Corte de cabello", 15, "Rizado")
servicio2 = ServicioUnas("Manicura", 12, "Semipermanente")

# Lista de servicios
servicios = [servicio1, servicio2]

# Aplicar polimorfismo
for servicio in servicios:
    print(servicio.mostrar_detalle())
    print(servicio.mostrar_detalle(False))

 

