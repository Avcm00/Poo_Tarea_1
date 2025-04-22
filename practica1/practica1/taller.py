"""1. Clase Producto
•Crear una única clase Producto con atributos como
código, nombre, precio, stock, categoría y atributos adicionales
como tipo, fecha_vencimiento (opcional) y garantía (opcional).
Crear atributos públicos, protegidos y privados con sus respectivos properties.
Además, métodos de usuario según las especificaciones"""
import time
class Producto:

    def __init__(self, codigo,nombre,precio,stock,categoria,fecha) -> None:
        productos_registrados = {}
        if codigo in productos_registrados:
            raise CodigoDuplicado(f"Ya existe un producto con este codigo{codigo}")

        #atributos
        self.nombre = nombre,
        self.codigo = codigo,
        self.__precio = 0,
        self.__garantia = False,
        self.__stock = 0,
        self.__fecha = "0000, 00, 00",
        self._categoria = categoria
        self._tipo = None


        self.precio = precio,
        self.stock = stock
        self.fecha = fecha

        Producto.productos_registrados[codigo] = self

        print(f"Producto creado: {self.codigo}, {self.nombre}")

"""2. Uso de unpacking
• Implementar la carga de productos desde tuplas de datos utilizando unpacking.
• Utilizar unpacking para extraer información de ventas y reportes."""
#   productos
datos_productos = [
        ("FOOD001", "Cereal Integral", 4.99, 50, "Alimentos", "No perecedero", "2025, 12, 31", None),
        ("FOOD002", "Leche Deslactosada", 2.49, 30, "Alimentos", "Lácteos", "2023, 5, 15", None),
        ("CLOTH001", "Camiseta Algodón", 19.99, 40, "Ropa", "Camisetas", None, 1),
        ("CLOTH002", "Pantalón Vaquero", 39.99, 20, "Ropa", "Pantalones", None, 3),
        ("TECH003", "Audífonos Bluetooth", 59.99, 15, "Electrónica", "Audio", None, 6)
]
#funcion cargar productos de tuplas
def cargar_produto_tuplas (*datos):
    datos_cargados = []

    for dato in datos:
        producto = list(dato)
        datos_cargados.append(producto)

    return datos_cargados



"""
3. Utilización de map y sum
• Usar map para aplicar descuentos a múltiples productos.
• Implementar sum para calcular el valor total del inventario."""

def aplicar_descuento_multiple ():
    x = 0
    return x


def valor_total_inventario ():
    return True

"""4. Excepciones personalizadas
• Crear excepciones específicas para manejar errores de operaciones con productos."""
class ProductoError(Exception):
    pass

class StockInsuficiente(ProductoError):
    def __init__(self, mensaje = "Stock insuficiente para realizar esta operacion"):
        super().__init__(mensaje)
class PrecioInvalido(ProductoError):
    def __init__(self, mensaje = "aqui va algo"):
        super().__init__(mensaje)
class CodigoDuplicado(ProductoError):
    def __init__(self, mensaje = "El Codigo ya se encuentra registrado en otro producto"):
        super().__init__(mensaje)

"""5. Decoradores
• Implementar decoradores para registrar operaciones y medir tiempos de ejecución."""

#decoradores

def validar_operacion(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except (ValueError,TypeError) as e:
            print(f"Error de validacion en {func.__name__}: {str(e)}")
            raise ProductoError(f"Error de validacion {str(e)}")
    return wrapper

def medir_ejecucion(func):
    def wrapper(*args,**kwargs):
        tiempo_inicio = time.time()
        resultado = func(*args,**kwargs)
        tiempo_fin = time.time()
        print(f"El tiempo de ejecucion de {func.__name__} : {tiempo_inicio - tiempo_fin:.4f}")
        return  resultado
    return wrapper

"""6. Colecciones
• Usar diferentes colecciones (listas, diccionarios, tuplas) para gestionar los datos."""

