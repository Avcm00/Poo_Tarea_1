from typing import List, Optional, Union
import time
from venta_json.utils.utilities import borrarPantalla, gotoxy


class Menu:
    def __init__(self, titulo: str = "", opciones: List[str] = [], col: int = 6, fil: int = 1) -> None:
        self.titulo: str = titulo
        self.opciones: List[str] = opciones
        self.col: int = col
        self.fil: int = fil

    def menu(self) -> str:
        gotoxy(self.col, self.fil);
        print(self.titulo)
        self.col -= 5
        for opcion in self.opciones:
            self.fil += 1
            gotoxy(self.col, self.fil);
            print(opcion)
        gotoxy(self.col + 5, self.fil + 2)
        opc: str = input(f"Elija opcion[1...{len(self.opciones)}]: ")
        return opc


class Valida:
    def solo_numeros(self, mensajeError: str, col: int, fil: int) -> str:
        while True:
            gotoxy(col, fil)
            valor: str = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col, fil);
                print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil);
                print(" " * 20)
        return valor

    def solo_letras(self, mensaje: str, mensajeError: str) -> str:
        while True:
            valor: str = str(input("          ------>   |"))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self, mensaje: str, mensajeError: str) -> float:
        while True:
            valor_str: str = str(input("          ------>   |  "))
            try:
                valor: float = float(valor_str)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    @staticmethod
    def cedula() -> None:
        pass


if __name__ == '__main__':
    # instanciar el menu
    opciones_menu: List[str] = ["1. Entero", "2. Letra", "3. Decimal"]
    menu: Menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida: str = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida: Valida = Valida()
    if (opciones_menu == 1):  # Esto parece un error, debería ser opcion_elegida
        numero_validado: str = valida.solo_numeros("Mensaje de error", 10, 10)
        print("Número validado:", numero_validado)

    numero_validado: str = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)

    letra_validada: str = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)

    decimal_validado: float = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)