
from modelos.servicio import Servicio
from modelos.servicio_cabello import ServicioCabello
from modelos.servicio_unas import ServicioUnas
from modelos.servicio_facial import ServicioFacial
from modelos.excepciones import PrecioInvalidoError
from modelos.catalogo_servicios import CatalogoServicios
from modelos.servicio_base import ServicioBase
from servicios.persistencia_servicios import PersistenciaServicios
from modelos.categoria_servicios import CategoriaServicio
from modelos.servicios_composicion import ServicioComposicion


# ==================================================
# 1. VALIDACIÓN DE EXCEPCIONES PERSONALIZADAS
# ==================================================
print("\n=== VALIDACIÓN DE PRECIOS ===")

servicio = Servicio("Corte de cabello", 15.00)

try:
    servicio.precio = -10
except PrecioInvalidoError as error:
    print("Error:", error)

print(servicio.mostrar_detalle())


# ==================================================
# 2. HERENCIA Y POLIMORFISMO
# ==================================================
print("\n=== HERENCIA Y POLIMORFISMO ===")

# Crear objetos de las clases hijas.
servicio_cabello = ServicioCabello(
    "Tratamiento capilar", 25, "Rizado"
)

servicio_unas = ServicioUnas(
    "Manicura semipermanente", 20, "Semipermanente"
)

servicio_facial = ServicioFacial(
    "Tratamiento facial", 35, "Hidratación profunda"
)

# POLIMORFISMO:
# Todos los objetos heredan de Servicio.
# Cada clase hija sobrescribe mostrar_detalle()
# para mostrar información específica.
servicios = [
    servicio_cabello,
    servicio_unas,
    servicio_facial
]

for servicio in servicios:
    print(servicio.mostrar_detalle())


# ==================================================
# 3. SOBRECARGA SIMULADA - ACTIVIDAD 2
# ==================================================
print("\n=== SOBRECARGA SIMULADA ===")

# SOBRECARGA:
# En Java podemos definir métodos con el mismo nombre,
# pero con diferentes parámetros.
#
# Python no implementa directamente esa sobrecarga.
# Por eso utilizamos el argumento por defecto
# incluir_precio=True en mostrar_detalle().
#
# Esto permite llamar al mismo método con o sin
# argumentos adicionales.

servicio = Servicio("Lavado de cabello", 10)

print(servicio.mostrar_detalle())
print(servicio.mostrar_detalle(False))


# ==================================================
# 4. SOBRESCRITURA - ACTIVIDAD 3, EJERCICIO 2
# ==================================================
print("\n=== SOBRESCRITURA DE MÉTODOS ===")

# SOBRESCRITURA:
# Ocurre cuando una clase hija redefine un método
# heredado para adaptar su comportamiento.
#
# ServicioFacial sobrescribe mostrar_detalle()
# de la clase Servicio para agregar información
# específica sobre el tratamiento facial.
#
# DIFERENCIA:
# La sobrecarga simulada permite diferentes formas
# de invocar un método mediante argumentos opcionales.
# La sobrescritura permite que una subclase proporcione
# su propia implementación de un método heredado.

print(servicio_facial.mostrar_detalle())


# ==================================================
# 5. AGRUPACIÓN DE OBJETOS - CATÁLOGO
# ==================================================
print("\n=== CATÁLOGO DE SERVICIOS ===")

catalogo = CatalogoServicios()

# Agregar los servicios al catálogo.
for servicio in servicios:
    catalogo.agregar_servicio(servicio)

# Mostrar todos los servicios registrados.
catalogo.mostrar_servicios()

print("\n=== EJERCICIO 3: CONTRATO ABSTRACTO ===")

# Creamos objetos de diferentes clases que
# implementan el contrato de ServicioBase.
servicios_contrato = [
    ServicioCabello("Corte de cabello", 15, "Liso"),
    ServicioUnas("Manicura", 12, "Tradicional"),
    ServicioFacial("Limpieza facial", 25, "Profunda")
]

for servicio in servicios_contrato:
    print(
        isinstance(servicio, ServicioBase),
        servicio.mostrar_detalle()
    )


# EJERCICIO 4: EXCEPCIÓN PERSONALIZADA
# ==================================================

print("\n=== VALIDACIÓN DE PRECIO ===")

servicio = Servicio("Corte de cabello", 15.00)

try:
    # Intentamos asignar un precio inválido.
    servicio.precio = -10

except PrecioInvalidoError as error:
    # Capturamos la excepción y mostramos un mensaje.
    print(f"Error al actualizar el precio: {error}")

# Comprobamos que se conserva el precio original.
print(servicio.mostrar_detalle())


import threading
import time

# EJERCICIO 5: USO DE HILOS
# Simulamos el procesamiento concurrente
# de dos servicios del salón de belleza.

def procesar_servicio(servicio):
    print(f"Iniciando: {servicio.nombre}")

    # Simula una tarea que requiere tiempo de espera.
    time.sleep(2)

    print(f"Finalizado: {servicio.mostrar_detalle()}")


print("\n=== PROCESAMIENTO CON HILOS ===")

# Utilizamos los objetos creados anteriormente.
hilo1 = threading.Thread(
    target=procesar_servicio,
    args=(servicio_cabello,)
)

hilo2 = threading.Thread(
    target=procesar_servicio,
    args=(servicio_unas,)
)

# Iniciamos ambos hilos.
hilo1.start()
hilo2.start()

# Esperamos que ambos terminen.
hilo1.join()
hilo2.join()

print("Todos los servicios fueron procesados.")


# ==================================================
# EJERCICIO 6: ENTRADA Y SALIDA CON ARCHIVOS JSON
# ==================================================

print("\n=== PERSISTENCIA DE SERVICIOS ===")

# Crear un objeto de ServicioCabello.
servicio_guardar = ServicioCabello(
    "Tratamiento capilar", 25, "Rizado"
)

# Crear el administrador de archivos.
persistencia = PersistenciaServicios()

# Guardar el objeto en un archivo JSON.
persistencia.guardar_servicio(servicio_guardar)

# Leer el archivo y reconstruir el objeto.
servicio_recuperado = persistencia.cargar_servicio()

if servicio_recuperado is not None:
    print(servicio_recuperado.mostrar_detalle())
    print("Tipo de objeto:", type(servicio_recuperado).__name__)


# EJERCICIO 7: COMPOSICIÓN EN LUGAR DE HERENCIA
# ==================================================

print("\n=== COMPOSICIÓN DE SERVICIOS ===")

# Creamos las categorías.
categoria_cabello = CategoriaServicio(
    "Cabello", "Servicios de cuidado capilar"
)

categoria_unas = CategoriaServicio(
    "Uñas", "Servicios de manicura"
)

categoria_facial = CategoriaServicio(
    "Facial", "Tratamientos para el rostro"
)

# Creamos servicios utilizando la clase general.
servicio1 = Servicio("Corte de cabello", 15)
servicio2 = Servicio("Manicura", 20)
servicio3 = Servicio("Limpieza facial", 25)

# Asociamos cada servicio con su categoría.
servicios = [
    ServicioComposicion(servicio1, categoria_cabello),
    ServicioComposicion(servicio2, categoria_unas),
    ServicioComposicion(servicio3, categoria_facial)
]

for servicio in servicios:
    print(servicio.mostrar_detalle())

# Ejercicio 8
#Polimorfismo
print("--------Ejercicio 8-----------")
servicios = [
    ServicioCabello("Tratamiento capilar", 25, "Rizado"),
    ServicioUnas("Manicura", 20, "Semipermanente"),
    ServicioFacial("Limpieza facial", 30, "Profunda")
]

for servicio in servicios:
    print(servicio.mostrar_detalle())

