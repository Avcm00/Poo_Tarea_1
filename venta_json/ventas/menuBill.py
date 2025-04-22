from typing import List, Dict, Any, Optional, Union, Tuple, TypeVar, Callable
import datetime
import time
import os
from functools import reduce

from venta_json.utils.components import Menu, Valida # type: ignore
from venta_json.utils.utilities import (
    borrarPantalla, gotoxy,
    reset_color, red_color, green_color,
    yellow_color, blue_color, purple_color, cyan_color
)
from venta_json.utils.clsJson import JsonFile
from venta_json.clientes.company import Company
from venta_json.clientes.customer import RegularClient
from venta_json.ventas.sales import Sale
from venta_json.productos.product import Product
from venta_json.interfaces.iCrud import ICrud

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    @staticmethod
    def create() -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Registro de Cliente" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("Cédula:")
        dni: str = validar.solo_numeros("Error: Solo números", 13, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/clients.json')
        client: Optional[List[Dict[str, Any]]] = json_file.find("dni", dni)

        if client:
            gotoxy(5, 7)
            print(red_color + "¡Cliente ya existe!" + reset_color)
            time.sleep(2)
            return

        gotoxy(5, 6)
        print("Nombre:")
        nombre: str = input("  " * 7)

        gotoxy(5, 7)
        print("Apellido:")
        apellido: str = input("  " * 7)

        gotoxy(5, 8)
        print("¿Tiene tarjeta? (s/n):")
        tiene_tarjeta: str = input("  " * 7).lower()

        new_client: Dict[str, Any] = {
            "dni": dni,
            "nombre": nombre,
            "apellido": apellido,
            "card": tiene_tarjeta
        }

        clients: List[Dict[str, Any]] = json_file.read()
        clients.append(new_client)
        json_file.save(clients)

        gotoxy(5, 10)
        print(green_color + "Cliente guardado exitosamente" + reset_color)
        time.sleep(2)

    @staticmethod
    def update() -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Actualización de Cliente" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("Cédula del cliente a modificar:")
        dni: str = validar.solo_numeros("Error: Solo números", 35, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/clients.json')
        clients: List[Dict[str, Any]] = json_file.read()
        client_index: int = -1

        for i, client in enumerate(clients):
            if client["dni"] == dni:
                client_index = i
                break

        if client_index == -1:
            gotoxy(5, 7)
            print(red_color + "¡Cliente no existe!" + reset_color)
            time.sleep(2)
            return

        cliente_actual = clients[client_index]

        gotoxy(5, 6)
        print(f"Nombre actual: {cliente_actual['nombre']}")
        gotoxy(5, 7)
        print("Nuevo nombre (deje vacío para mantener):")
        nombre: str = input("  " * 7)
        if nombre.strip():
            cliente_actual['nombre'] = nombre

        gotoxy(5, 8)
        print(f"Apellido actual: {cliente_actual['apellido']}")
        gotoxy(5, 9)
        print("Nuevo apellido (deje vacío para mantener):")
        apellido: str = input("  " * 7)
        if apellido.strip():
            cliente_actual['apellido'] = apellido

        gotoxy(5, 10)
        print(f"Tiene tarjeta: {'Sí' if cliente_actual['card'] else 'No'}")
        gotoxy(5, 11)
        print("¿Cambiar estado de tarjeta? (s/n):")
        cambiar_tarjeta: str = input("  " * 7).lower()
        if cambiar_tarjeta == 's':
            cliente_actual['card'] = not cliente_actual['card']

        json_file.save(clients)

        gotoxy(5, 13)
        print(green_color + "Cliente actualizado exitosamente" + reset_color)
        time.sleep(2)

    @staticmethod
    def delete() -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Eliminación de Cliente" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("Cédula del cliente a eliminar:")
        dni: str = validar.solo_numeros("Error: Solo números", 35, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/clients.json')
        clients: List[Dict[str, Any]] = json_file.read()
        client_index: int = -1

        for i, client in enumerate(clients):
            if client["dni"] == dni:
                client_index = i
                break

        if client_index == -1:
            gotoxy(5, 7)
            print(red_color + "¡Cliente no existe!" + reset_color)
            time.sleep(2)
            return

        cliente_a_eliminar = clients[client_index]
        gotoxy(5, 7)
        print(f"Cliente: {cliente_a_eliminar['nombre']} {cliente_a_eliminar['apellido']}")
        gotoxy(5, 8)
        print(yellow_color + "¿Está seguro de eliminar este cliente? (s/n):" + reset_color)
        confirmar: str = input("  " * 7).lower()

        if confirmar == 's':
            clients.pop(client_index)
            json_file.save(clients)
            gotoxy(5, 10)
            print(green_color + "Cliente eliminado exitosamente" + reset_color)
        else:
            gotoxy(5, 10)
            print(cyan_color + "Operación cancelada" + reset_color)

        time.sleep(2)

    @staticmethod
    def consult() -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Consulta de Clientes" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        gotoxy(5, 5)
        print("1. Consultar cliente específico")
        gotoxy(5, 6)
        print("2. Listar todos los clientes")
        gotoxy(5, 7)
        print("Seleccione una opción:")
        opcion: str = input("  " * 7)

        json_file: JsonFile = JsonFile(path + '/archivos/clients.json')
        clients: List[Dict[str, Any]] = json_file.read()

        if opcion == "1":
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2, 1)
            print(green_color + "*" * 90 + reset_color)
            gotoxy(30, 2)
            print(blue_color + "Consulta de Cliente Específico" + reset_color)
            gotoxy(2, 3)
            print(green_color + "*" * 90 + reset_color)

            validar: Valida = Valida()
            gotoxy(5, 5)
            print("Cédula del cliente a consultar:")
            dni: str = validar.solo_numeros("Error: Solo números", 35, 5)

            client_found = False
            for client in clients:
                if client["dni"] == dni:
                    gotoxy(5, 7)
                    print(purple_color + "Datos del Cliente:" + reset_color)
                    gotoxy(5, 8)
                    print(f"Cédula: {client['dni']}")
                    gotoxy(5, 9)
                    print(f"Nombre: {client['nombre']}")
                    gotoxy(5, 10)
                    print(f"Apellido: {client['apellido']}")
                    gotoxy(5, 11)
                    print(f"Tiene tarjeta: {'Sí' if client['card'] else 'No'}")
                    client_found = True
                    break

            if not client_found:
                gotoxy(5, 7)
                print(red_color + "Cliente no encontrado" + reset_color)

        elif opcion == "2":
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2, 1)
            print(green_color + "*" * 90 + reset_color)
            gotoxy(30, 2)
            print(blue_color + "Listado de Clientes" + reset_color)
            gotoxy(2, 3)
            print(green_color + "*" * 90 + reset_color)

            if not clients:
                gotoxy(5, 5)
                print(yellow_color + "No hay clientes registrados" + reset_color)
            else:
                gotoxy(5, 5)
                print(purple_color + "Cédula".ljust(15) + "Nombre".ljust(15) + "Apellido".ljust(15) + "Tarjeta" + reset_color)
                gotoxy(5, 6)
                print("-" * 55)

                for i, client in enumerate(clients):
                    gotoxy(5, 7 + i)
                    tiene_tarjeta = "Sí" if client.get("card", False) else "No"
                    print(f"{client['dni']}".ljust(15) + f"{client['nombre']}".ljust(15) + f"{client['apellido']}".ljust(15) + tiene_tarjeta)

        gotoxy(5, 20)
        input(cyan_color + "Presione una tecla para continuar..." + reset_color)


class CrudProducts(ICrud):
    def create(self) -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Registro de Producto" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("ID:")
        id_producto: str = validar.solo_numeros("Error: Solo números", 9, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/products.json')
        product: Optional[List[Dict[str, Any]]] = json_file.find("id", int(id_producto))

        if product:
            gotoxy(5, 7)
            print(red_color + "¡Producto ya existe!" + reset_color)
            time.sleep(2)
            return

        gotoxy(5, 6)
        print("Descripción:")
        descripcion: str = input("  " * 7).strip()

        gotoxy(5, 7)
        print("Precio:")
        # La corrección está aquí, ahora solo pasamos los argumentos necesarios
        # Basándonos en la llamada a solo_numeros(), probablemente solo_decimales() 
        # también necesita mensaje_error y columna, fila - o solo mensaje_error y posición
        precio: float = float(validar.solo_decimales("Error: Ingrese un valor decimal", 12))

        gotoxy(5, 8)
        print("Stock:")
        stock: int = int(validar.solo_numeros("Error: Solo números", 12, 8))

        new_product: Dict[str, Any] = {
            "id": int(id_producto),
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }

        products: List[Dict[str, Any]] = json_file.read()
        products.append(new_product)
        json_file.save(products)

        gotoxy(5, 10)
        print(green_color + "Producto guardado exitosamente" + reset_color)
        time.sleep(2)

    def update(self) -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Actualización de Producto" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("ID del producto a modificar:")
        id_producto: str = validar.solo_numeros("Error: Solo números", 32, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/products.json')
        products: List[Dict[str, Any]] = json_file.read()
        product_index: int = -1

        for i, product in enumerate(products):
            if product["id"] == int(id_producto):
                product_index = i
                break

        if product_index == -1:
            gotoxy(5, 7)
            print(red_color + "¡Producto no existe!" + reset_color)
            time.sleep(2)
            return

        producto_actual = products[product_index]

        gotoxy(5, 6)
        print(f"Descripción actual: {producto_actual['descripcion']}")
        gotoxy(5, 7)
        print("Nueva descripción (deje vacío para mantener):")
        descripcion: str = input("  " * 7)
        if descripcion.strip():
            producto_actual['descripcion'] = descripcion

        gotoxy(5, 8)
        print(f"Precio actual: {producto_actual['precio']}")
        gotoxy(5, 9)
        print("Nuevo precio (deje vacío para mantener):")
        precio: str = input("  " * 7)
        if precio.strip():
            producto_actual['precio'] = float(precio)

        gotoxy(5, 10)
        print(f"Stock actual: {producto_actual['stock']}")
        gotoxy(5, 11)
        print("Nuevo stock (deje vacío para mantener):")
        stock: str = input("  " * 7)
        if stock.strip():
            producto_actual['stock'] = int(stock)

        json_file.save(products)

        gotoxy(5, 13)
        print(green_color + "Producto actualizado exitosamente" + reset_color)
        time.sleep(2)

    def delete(self) -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Eliminación de Producto" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        validar: Valida = Valida()
        gotoxy(5, 5)
        print("ID del producto a eliminar:")
        id_producto: str = validar.solo_numeros("Error: Solo números", 30, 5)

        json_file: JsonFile = JsonFile(path + '/archivos/products.json')
        products: List[Dict[str, Any]] = json_file.read()
        product_index: int = -1

        for i, product in enumerate(products):
            if product["id"] == int(id_producto):
                product_index = i
                break

        if product_index == -1:
            gotoxy(5, 7)
            print(red_color + "¡Producto no existe!" + reset_color)
            time.sleep(2)
            return

        producto_a_eliminar = products[product_index]
        gotoxy(5, 7)
        print(f"Producto: {producto_a_eliminar['descripcion']}")
        gotoxy(5, 8)
        print(yellow_color + "¿Está seguro de eliminar este producto? (s/n):" + reset_color)
        confirmar: str = input("  " * 7).lower()

        if confirmar == 's':
            products.pop(product_index)
            json_file.save(products)
            gotoxy(5, 10)
            print(green_color + "Producto eliminado exitosamente" + reset_color)
        else:
            gotoxy(5, 10)
            print(cyan_color + "Operación cancelada" + reset_color)

        time.sleep(2)

    def consult(self) -> None:
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1)
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2)
        print(blue_color + "Consulta de Productos" + reset_color)
        gotoxy(2, 3)
        print(green_color + "*" * 90 + reset_color)

        gotoxy(5, 5)
        print("1. Consultar producto específico")
        gotoxy(5, 6)
        print("2. Listar todos los productos")
        gotoxy(5, 7)
        print("Seleccione una opción:")
        opcion: str = input("  " * 7)

        json_file: JsonFile = JsonFile(path + '/archivos/products.json')
        products: List[Dict[str, Any]] = json_file.read()

        if opcion == "1":
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2, 1)
            print(green_color + "*" * 90 + reset_color)
            gotoxy(30, 2)
            print(blue_color + "Consulta de Producto Específico" + reset_color)
            gotoxy(2, 3)
            print(green_color + "*" * 90 + reset_color)

            validar: Valida = Valida()
            gotoxy(5, 5)
            print("ID del producto a consultar:")
            id_producto: str = validar.solo_numeros("Error: Solo números", 32, 5)

            product_found = False
            for product in products:
                if product["id"] == int(id_producto):
                    gotoxy(5, 7)
                    print(purple_color + "Datos del Producto:" + reset_color)
                    gotoxy(5, 8)
                    print(f"ID: {product['id']}")
                    gotoxy(5, 9)
                    print(f"Descripción: {product['descripcion']}")
                    gotoxy(5, 10)
                    print(f"Precio: {product['precio']}")
                    gotoxy(5, 11)
                    print(f"Stock: {product['stock']}")
                    product_found = True
                    break

            if not product_found:
                gotoxy(5, 7)
                print(red_color + "Producto no encontrado" + reset_color)

        elif opcion == "2":
            borrarPantalla()
            print('\033c', end='')
            gotoxy(2, 1)
            print(green_color + "*" * 90 + reset_color)
            gotoxy(30, 2)
            print(blue_color + "Listado de Productos" + reset_color)
            gotoxy(2, 3)
            print(green_color + "*" * 90 + reset_color)

            if not products:
                gotoxy(5, 5)
                print(yellow_color + "No hay productos registrados" + reset_color)
            else:
                gotoxy(5, 5)
                print(purple_color + "ID".ljust(10) + "Descripción".ljust(30) + "Precio".ljust(15) + "Stock" + reset_color)
                gotoxy(5, 6)
                print("-" * 65)

                for i, product in enumerate(products):
                    gotoxy(5, 7 + i)
                    print(f"{product['id']}".ljust(10) + f"{product['descripcion']}".ljust(30) + f"{product['precio']}".ljust(15) + f"{product['stock']}")

        gotoxy(5, 20)
        input(cyan_color + "Presione una tecla para continuar..." + reset_color)


class CrudSales(ICrud):
    def create(self) -> None:
        # cabecera de la venta
        validar: Valida = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1);
        print(green_color + "*" * 90 + reset_color)
        gotoxy(30, 2);
        print(blue_color + "Registro de Venta")
        gotoxy(17, 3);
        print(blue_color + Company.get_business_name())
        gotoxy(5, 4);
        print(f"Factura#:F0999999 {' ' * 3} Fecha:{datetime.datetime.now()}")
        gotoxy(66, 4);
        print("Subtotal:")
        gotoxy(66, 5);
        print("Decuento:")
        gotoxy(66, 6);
        print("Iva     :")
        gotoxy(66, 7);
        print("Total   :")
        gotoxy(15, 6);
        print("Cedula:")

        dni: str = validar.solo_numeros("Error: Solo numeros", 23, 6)
        json_file: JsonFile = JsonFile(path + '/archivos/clients.json')
        client: Optional[List[Dict[str, Any]]] = json_file.find("dni", dni)

        if not client:
            gotoxy(35, 6);
            print("Cliente no existe")
            return

        client_data: Dict[str, Any] = client[0]
        cli: RegularClient = RegularClient(client_data["nombre"], client_data["apellido"], client_data["dni"],
                                           card=True)
        sale: Sale = Sale(cli)

        gotoxy(35, 6);
        print(cli.fullName())
        gotoxy(2, 8);
        print(green_color + "*" * 90 + reset_color)
        gotoxy(5, 9);
        print(purple_color + "Linea")
        gotoxy(12, 9);
        print("Id_Articulo")
        gotoxy(24, 9);
        print("Descripcion")
        gotoxy(38, 9);
        print("Precio")
        gotoxy(48, 9);
        print("Cantidad")
        gotoxy(58, 9);
        print("Subtotal")
        gotoxy(70, 9);
        print("n->Terminar Venta)" + reset_color)

        # detalle de la venta
        follow: str = "s"
        line: int = 1

        while follow.lower() == "s":
            gotoxy(7, 9 + line);
            print(line)
            gotoxy(15, 9 + line)
            id: int = int(validar.solo_numeros("Error: Solo numeros", 15, 9 + line))

            json_file = JsonFile(path + '/archivos/products.json')
            prods: Optional[List[Dict[str, Any]]] = json_file.find("id", id)

            if not prods:
                gotoxy(24, 9 + line);
                print("Producto no existe")
                time.sleep(1)
                gotoxy(24, 9 + line);
                print(" " * 20)
            else:
                prod_data: Dict[str, Any] = prods[0]
                product: Product = Product(prod_data["id"], prod_data["descripcion"], prod_data["precio"],
                                           prod_data["stock"])

                gotoxy(24, 9 + line);
                print(product.descrip)
                gotoxy(38, 9 + line);
                print(product.preci)
                gotoxy(49, 9 + line);
                qyt: int = int(validar.solo_numeros("Error:Solo numeros", 49, 9 + line))
                gotoxy(59, 9 + line);
                print(product.preci * qyt)

                sale.add_detail(product, qyt)
                gotoxy(76, 4);
                print(round(sale.subtotal, 2))
                gotoxy(76, 5);
                print(round(sale.discount, 2))
                gotoxy(76, 6);
                print(round(sale.iva, 2))
                gotoxy(76, 7);
                print(round(sale.total, 2))

                gotoxy(74, 9 + line);
                follow = input() or "s"
                gotoxy(76, 9 + line);
                print(green_color + "✔" + reset_color)
                line += 1

        gotoxy(15, 9 + line);
        print(red_color + "Esta seguro de grabar la venta(s/n):")
        gotoxy(54, 9 + line);
        procesar: str = input().lower()

        if procesar == "s":
            gotoxy(15, 10 + line);
            print("😊 Venta Grabada satisfactoriamente 😊" + reset_color)
            # print(sale.getJson())
            json_file = JsonFile(path + '/archivos/invoices.json')
            invoices: List[Dict[str, Any]] = json_file.read()
            ult_invoices: int = invoices[-1]["factura"] + 1

            data: Dict[str, Any] = sale.getJson()
            data["factura"] = ult_invoices
            invoices.append(data)

            json_file = JsonFile(path + '/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20, 10 + line);
            print("🤣 Venta Cancelada 🤣" + reset_color)

        time.sleep(2)

    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete() -> None:
        pass

    def consult(self) -> None:
        print('\033c', end='')
        gotoxy(2, 1);
        print(green_color + "█" * 90)
        gotoxy(2, 2);
        print("██" + " " * 34 + "Consulta de Venta" + " " * 35 + "██")
        gotoxy(2, 4);
        invoice: str = input("Ingrese Factura: ")

        if invoice.isdigit():
            invoice_num: int = int(invoice)
            json_file: JsonFile = JsonFile(path + '/archivos/invoices.json')
            invoices: List[Dict[str, Any]] = json_file.find("factura", invoice_num)
            print(f"Impresion de la Factura#{invoice_num}")
            print(invoices)
        else:
            json_file: JsonFile = JsonFile(path + '/archivos/invoices.json')
            invoices: List[Dict[str, Any]] = json_file.read()
            print("Consulta de Facturas")

            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")

            suma: float = reduce(lambda total, invoice: round(total + invoice["total"], 2),
                                 invoices, 0)
            totales_map: List[float] = list(map(lambda invoice: invoice["total"], invoices))
            total_client: List[Dict[str, Any]] = list(
                filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice: float = max(totales_map)
            min_invoice: float = min(totales_map)
            tot_invoices: float = sum(totales_map)

            print("filter cliente: ", total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{tot_invoices}")
            print(f"              reduce Facturas:{suma}")

        x: str = input("presione una tecla para continuar...")


# Menu Proceso Principal
opc: str = ''
while opc != '4':
    borrarPantalla()
    menu_main: Menu = Menu("Menu Facturacion", ["1) Clientes", "2) Productos", "3) Ventas", "4) Salir"], 20, 10)
    opc = menu_main.menu()

    if opc == "1":
        opc1: str = ''
        while opc1 != '5':
            borrarPantalla()
            clients: CrudClients = CrudClients()
            menu_clients: Menu = Menu("Menu Cientes",
                                      ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20,
                                      10)
            opc1 = menu_clients.menu()

            if opc1 == "1":
                clients.create()
            elif opc1 == "2":
                clients.update()
            elif opc1 == "3":
                clients.delete()
            elif opc1 == "4":
                clients.consult()

            print("Regresando al menu Clientes...")
            # time.sleep(2)

    elif opc == "2":
        opc2: str = ''
        while opc2 != '5':
            borrarPantalla()
            products: CrudProducts = CrudProducts()
            menu_products: Menu = Menu("Menu Productos",
                                       ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20,
                                       10)
            opc2 = menu_products.menu()

            if opc2 == "1":
                products.create()
            elif opc2 == "2":
                products.update()
            elif opc2 == "3":
                products.delete()
            elif opc2 == "4":
                products.consult()

    elif opc == "3":
        opc3: str = ''
        while opc3 != '5':
            borrarPantalla()
            sales: CrudSales = CrudSales()
            menu_sales: Menu = Menu("Menu Ventas",
                                    ["1) Registro Venta", "2) Consultar", "3) Modificar", "4) Eliminar", "5) Salir"],
                                    20, 10)
            opc3 = menu_sales.menu()

            if opc3 == "1":
                sales.create()
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                sales.update()
            elif opc3 == "4":
                sales.delete()


    print("Regresando al menu Principal...")
    # time.sleep(2)

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()