import json
from modelos.excepciones import PrecioInvalidoError
from pathlib import Path
from modelos.servicio_cabello import ServicioCabello

class PersistenciaServicios:
    """
    Permite guardar y recuperar servicios de cabello
    mediante archivos JSON.
    Maneja errores de lectura, escritura y datos inválidos.
    """

    def __init__(self, archivo="servicios.json"):
        self.archivo = Path(archivo)

    def guardar_servicio(self, servicio):
        # Convierte los atributos del objeto en un diccionario.
        datos = {
            "nombre": servicio.nombre,
            "precio": servicio.precio,
            "tipo_cabello": servicio.tipo_cabello
        }

        try:
            with self.archivo.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            print("Servicio guardado correctamente.")

        except OSError as error:
            print(f"Error al guardar el archivo: {error}")

    def cargar_servicio(self):
        try:
            # Lee la información almacenada en JSON.
            with self.archivo.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            # Valida la estructura básica de los datos.
            if not isinstance(datos, dict):
                raise ValueError("El contenido debe ser un objeto JSON.")

            # Reconstruye el objeto usando su constructor.
            servicio = ServicioCabello(
                datos["nombre"],
                datos["precio"],
                datos["tipo_cabello"]
            )

            print("Servicio recuperado correctamente.")
            return servicio

        except FileNotFoundError:
            print("Error: No se encontró el archivo de servicios.")

        except (json.JSONDecodeError, UnicodeError):
            print("Error: El archivo contiene datos corruptos.")

        except (KeyError, TypeError, ValueError, PrecioInvalidoError) as error:
            print(f"Error: Los datos del servicio no son válidos: {error}")

        except OSError as error:
            print(f"Error al leer el archivo: {error}")

        return None
