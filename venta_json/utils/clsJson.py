import json
import os
from typing import List, Dict, Any, Optional, Union


class JsonFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def save(self, data: List[Dict[str, Any]]) -> None:
        # Crear el directorio si no existe
        directory = os.path.dirname(self.filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(self.filename, 'w') as file:
            json.dump(data, file)  # dump:graba datos a un archivo json
            file.write('\n')
    def read(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filename, 'r') as file:
                data: List[Dict[str, Any]] = json.load(file)  # load:carga datos desde un archivo json
        except FileNotFoundError:
            data = []
        return data

    def find(self, atributo: str, buscado: Union[str, int]) -> List[Dict[str, Any]]:
        try:
            with open(self.filename, 'r') as file:
                datas: List[Dict[str, Any]] = json.load(file)
                data = [item for item in datas if item[atributo] == buscado]
        except FileNotFoundError:
            data = []
        return data