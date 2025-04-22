import json
import os
from typing import Any, Dict
from clase_abstract_json import InterfaceArchivo

class ManejadorJSON(InterfaceArchivo):
    # Constructor que inicializa la ruta del archivo
    def __init__(self, ruta_archivo: str) -> None:
        super().__init__(ruta_archivo)

    # Método para guardar datos en formato JSON
    def guardar_json(self, datos: Dict[str, Any]) -> bool:
        try:
            # Abre el archivo en modo escritura con codificación UTF-8
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                # Convierte y guarda el diccionario a formato JSON con formato legible
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            # Manejo de errores durante el guardado
            print(f"Error al guardar el archivo: {e}")
            return False

    # Método para leer datos desde un archivo JSON
    def leer_json(self) -> Dict[str, Any]:
        try:
            # Verifica si el archivo existe antes de leerlo
            if self.validar_archivo():
                # Abre el archivo en modo lectura con codificación UTF-8
                with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                    # Carga y retorna el contenido JSON como diccionario
                    return json.load(archivo)
            return {}
        except Exception as e:
            # Manejo de errores durante la lectura
            print(f"Error al leer el archivo: {e}")
            return {}

    # Método para validar la existencia del archivo
    def validar_archivo(self) -> bool:
        # Verifica si el archivo existe en la ruta especificada
        return os.path.exists(self.ruta_archivo)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia del manejador especificando la ruta del archivo JSON
    manejador = ManejadorJSON("d:/daniel/unemi/Primer Semestre 2025/POO/POO/practica1/datos.json")
    
    # Crear estructura de datos de ejemplo con información de estudiantes
    datos_guardar = {
        "estudiantes": [
            {
                "nombre": "Ana García",
                "edad": 20,
                "carrera": "Ingeniería"
            },
            {
                "nombre": "Daniel Vera",
                "edad": 50,
                "carrera": "Software"
            }
        ]
    }
    
    # Guardar los datos en el archivo JSON y verificar si se guardó correctamente
    if manejador.guardar_json(datos_guardar):
        print("Datos guardados correctamente")
    
    # Leer el contenido del archivo JSON
    datos_leidos = manejador.leer_json()
    
    # Mostrar los datos leídos con formato JSON indentado
    # ensure_ascii=False permite mostrar caracteres especiales y acentos correctamente
    print("\nDatos leídos:")
    print(json.dumps(datos_leidos, indent=2, ensure_ascii=False))