from typing import Tuple, Optional
import os
import datetime
import time

# Variables globales: Colores en formato ANSI escape code
reset_color: str = "\033[0m"
red_color: str = "\033[91m"
green_color: str = "\033[92m"
yellow_color: str = "\033[93m"
blue_color: str = "\033[94m"
purple_color: str = "\033[95m"
cyan_color: str = "\033[96m"

# funciones de usuario

def gotoxy(x: int, y: int) -> None:
    print("%c[%d;%df" % (0x1B, y, x), end="")

def borrarPantalla() -> None:
    os.system("cls")

def mensaje(msg: str, f: int, c: int) -> None:
    pass

path, _ = os.path.split(os.path.abspath(__file__))
print("ruta: ", path)