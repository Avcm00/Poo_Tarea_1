from abc import ABC, abstractmethod
from typing import Any, Dict

class InterfaceArchivo(ABC):
    def __init__(self, ruta_archivo: str) -> None:
        self.ruta_archivo: str = ruta_archivo
    
    @abstractmethod
    def guardar_json(self, datos: Dict[str, Any]) -> bool:
        """
        Método abstracto para guardar datos en formato JSON
        Args:
            datos: Diccionario con los datos a guardar
        Returns:
            bool: True si se guardó correctamente, False en caso contrario
        """
        pass
    
    @abstractmethod
    def leer_json(self) -> Dict[str, Any]:
        """
        Método abstracto para leer datos desde un archivo JSON
        Returns:
            Dict: Diccionario con los datos leídos del archivo
        """
        pass
    
    @abstractmethod
    def validar_archivo(self) -> bool:
        """
        Método abstracto para validar si el archivo existe y es válido
        Returns:
            bool: True si el archivo es válido, False en caso contrario
        """
        pass