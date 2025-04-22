from typing import List, Dict, Any, Optional
from datetime import date
import os
from venta_json.utils.calculos import Icalculo
from venta_json.productos.product import Product  # Suponiendo que existe esta clase

# Colores en formato ANSI escape code
reset_color: str = "\033[0m"
red_color: str = "\033[91m"
green_color: str = "\033[92m"
yellow_color: str = "\033[93m"
blue_color: str = "\033[94m"
purple_color: str = "\033[95m"
cyan_color: str = "\033[96m"


class SaleDetail:
    _line: int = 0

    def __init__(self, product: 'Product', quantity: int) -> None:
        SaleDetail._line += 1
        self.__id: int = SaleDetail._line
        self.product: 'Product' = product
        self.preci: float = product.preci
        self.quantity: int = quantity

    @property
    def id(self) -> int:
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__id

    def __repr__(self) -> str:
        # Método especial para representar la clase Cliente como una cadena
        return f'{self.id} {self.product.descrip} {self.preci} {self.quantity}'


class Sale(Icalculo):
    next: int = 0
    FACTOR_IVA: float = 0.12

    def __init__(self, client: Any) -> None:
        Sale.next += 1
        self.__invoice: int = Sale.next
        self.date: date = date.today()
        self.client: Any = client
        self.subtotal: float = 0
        self.percentage_discount: float = client.discount
        self.discount: float = 0
        self.iva: float = 0
        self.total: float = 0
        self.sale_detail: List[SaleDetail] = []

    @property
    def invoice(self) -> int:
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__invoice

    def __repr__(self) -> str:
        # Método especial para representar la clase Cliente como una cadena
        return f'Factura# {self.invoice} {self.date} {self.client.fullName()} {self.total}'

    def cal_iva(self, iva: float = 0.12, valor: float = 0) -> float:
        return round(valor * iva, 2)

    def cal_discount(self, valor: float = 0, discount: float = 0) -> float:
        return valor * discount

    def add_detail(self, prod: 'Product', qty: int) -> None:
        # composicion entre detventa y venta
        detail: SaleDetail = SaleDetail(prod, qty)
        self.subtotal += round(detail.preci * detail.quantity, 2)
        # self.discount = self.subtotal*self.percentage_discount
        self.discount = self.cal_discount(self.subtotal, self.percentage_discount)
        # self.iva = round((self.subtotal-self.discount)*Sale.FACTOR_IVA,2)
        self.iva = self.cal_iva(Sale.FACTOR_IVA, self.subtotal - self.discount)
        self.total = round(self.subtotal + self.iva - self.discount, 2)
        self.sale_detail.append(detail)

    def print_invoice(self, company: Any) -> None:
        os.system('cls')
        print('\033c', end='')
        print(green_color + "*" * 70 + reset_color)
        print(blue_color + f"Empresa: {company.business_name} Ruc: {company.ruc}", end='')
        print(" Factura#:{:7}Fecha:{}".format(self.invoice, self.date))
        self.client.show()
        print(green_color + "*" * 70 + reset_color)
        print(purple_color + "Linea Articulo Precio Cantidad Subtotal")
        for det in self.sale_detail:
            print(
                blue_color + f"{det.id:5} {det.product.descrip:6} {det.preci:7} {det.quantity:2} {det.preci * det.quantity:14}")
        print(green_color + "*" * 70 + reset_color)
        print(purple_color + " " * 23, "Subtotal:  ", str(self.subtotal))
        print(" " * 23, "Descuento: ", str(self.discount))
        print(" " * 23, "Iva:       ", str(self.iva))
        print(" " * 23, "Total:     ", str(self.total) + reset_color)

    def getJson(self) -> Dict[str, Any]:
        # Método especial para representar la clase venta como diccionario
        invoice: Dict[str, Any] = {
            "factura": self.invoice,
            "Fecha": self.date.strftime("%Y-%m-%d"),
            "cliente": self.client.fullName(),
            "subtotal": self.subtotal,
            "descuento": self.discount,
            "iva": self.iva,
            "total": self.total,
            "detalle": []
        }
        for det in self.sale_detail:
            invoice["detalle"].append({
                "poducto": det.product.descrip,
                "precio": det.preci,
                "cantidad": det.quantity
            })
        return invoice
# cli = Client()
# sale1 = Sale()