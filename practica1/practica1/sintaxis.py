from typing import List, Tuple, Dict, Set, Optional, Any

class Ejercicios:
    def __init__(self) -> None:
        print("Empiezo a ejecutar los ejercicios")
     
    
    def variables(self) -> None:
        # Tipos de datos simples
        entero: int = 19
        flotante: float = 3.14
        cadena: str = "Hello World"
        booleano: bool = True
        nulo: None = None
        # Tipos de datos complejos
        # Lista: Colección ordenada y modificable de elementos que pueden ser de diferentes tipos
        lista: List[Any] = [1, 2, 3, "python", True]
        
        # Tupla: Colección ordenada e inmutable de elementos que pueden ser de diferentes tipos
        tupla: Tuple[int, str, float] = (1, "hello", 3.14)
        
        # Diccionario: Colección de pares clave-valor, donde cada elemento tiene una clave única
        diccionario: Dict[str, Any] = {
            "nombre": "Juan",
            "edad": 25,
            "activo": True
        }
        
        # Conjunto: Colección desordenada de elementos únicos (no permite duplicados)
        conjunto: Set[int] = {1, 2, 3, 4, 5}
        
        # Mostrando las variables
        print("Tipos de Datos Simples:")
        print(f"Integer: {entero}")
        print(f"Float: {flotante}")
        print(f"String: {cadena}")
        print(f"String (primer caracter): {cadena[0]}")
        print(f"String (rango 0-5): {cadena[0:5]}")
        print(f"Boolean: {booleano}")
        print(f"None: {nulo}")
        
        print("\nTipos de Datos Complejos:")
        print(f"List completa: {lista}")
        print(f"List (elemento 2): {lista[2]}")
        print(f"List (rango 1-3): {lista[1:4]}")
        
        print(f"Tuple completa: {tupla}")
        print(f"Tuple (primer elemento): {tupla[0]}")
        print(f"Tuple (últimos dos elementos): {tupla[1:]}")
        
        print(f"Dictionary completo: {diccionario}")
        print(f"Dictionary (valor de 'nombre'): {diccionario['nombre']}")
        print(f"Dictionary (todas las claves): {list(diccionario.keys())}")
        
        print(f"Set completo: {conjunto}")
        print(f"Set (convertido a lista y primer elemento): {list(conjunto)[0]}")
    
    def operadores(self) -> None:
        # Operadores Aritméticos
        print("Operadores Aritméticos:")
        a: int = 20
        b: int = 4
        print(f"Suma: {a + b}")                  # 24
        print(f"Resta: {a - b}")                 # 16
        print(f"Multiplicación: {a * b}")        # 80
        print(f"División: {a / b}")              # 5.0
        print(f"División entera: {a // b}")      # 5
        print(f"Módulo: {a % b}")               # 0
        print(f"Exponente: {a ** b}")           # 160000

        # Operadores de Comparación
        print("\nOperadores de Comparación:")
        print(f"Igual a: {a == b}")             # False
        print(f"Diferente de: {a != b}")        # True
        print(f"Mayor que: {a > b}")            # True
        print(f"Menor que: {a < b}")            # False
        print(f"Mayor o igual: {a >= b}")       # True
        print(f"Menor o igual: {a <= b}")       # False

        # Operadores Lógicos
        print("\nOperadores Lógicos:")
        x: bool = True
        y: bool = False
        print(f"AND: {x and y}")                # False
        print(f"OR: {x or y}")                  # True
        print(f"NOT: {not x}")                  # False

        # Operadores de Asignación
        print("\nOperadores de Asignación:")
        c: int = 10
        c += 5  # c = c + 5
        print(f"Suma y asignación: {c}")        # 15
        c -= 3  # c = c - 3
        print(f"Resta y asignación: {c}")       # 12
        c *= 2  # c = c * 2
        print(f"Multiplicación y asignación: {c}")  # 24

        # Operadores de Identidad
        print("\nOperadores de Identidad:")
        lista1: List[int] = [1, 2, 3]
        lista2: List[int] = [1, 2, 3]
        lista3: List[int] = lista1
        print(f"is: {lista1 is lista3}")        # True
        # Retorna True porque aunque lista1 y lista2 tienen los mismos valores, 
        # son objetos diferentes en memoria
        print(f"is not: {lista1 is not lista2}")  # True

        # Operadores de Pertenencia
        print("\nOperadores de Pertenencia:")
        numeros: List[int] = [1, 2, 3, 4, 5]
        print(f"in: {3 in numeros}")            # True
        print(f"not in: {6 not in numeros}")    # True

    def entrada_salida(self) -> None:
        # Diferentes formas de salida (output)
        nombre = "Ana"
        edad = 25
        altura = 1.753
        
        # Print básico
        print("Print básico:")
        print("Hola Mundo")
        
        # Print con múltiples argumentos
        print("Nombre:", nombre, "Edad:", edad)
        
        # Print con format()
        print("Mi nombre es {} y tengo {} años".format(nombre, edad))
        
        # Print con f-strings (recomendado)
        print(f"Mi nombre es {nombre} y mido {altura:.2f} metros")
        
        # Print con control de separadores y fin de línea
        print("Python", "Java", "C++", sep=" -> ", end="!\n")
        
        # Diferentes formas de entrada (input)
        print("\nDiferentes tipos de entrada:")
        
        # Input básico (string)
        nombre_input = input("Ingrese su nombre: ")
        # Input numérico (convertido a int)
        edad_input = int(input("Ingrese su edad: "))
        # Input numérico (convertido a float)
        altura_input = float(input("Ingrese su altura en metros: "))
        
        # Mostrar los datos ingresados
        print("\nDatos ingresados:")
        print(f"Nombre: {nombre_input}")
        print(f"Edad: {edad_input}")
        print(f"Altura: {altura_input:.2f} metros")

    def condicionales(self) -> None:
        # If simple - Condicional básico
        edad: int = 18
        if edad >= 18:
            print("Es mayor de edad")
            
        # If-else - Condicional con alternativa
        numero: int = 15
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
            
        # If-elif-else - Condicional múltiple
        nota: float = 85.5
        if nota >= 90:
            print("Calificación: A")
        elif nota >= 80:
            print("Calificación: B")
        elif nota >= 70:
            print("Calificación: C")
        else:
            print("Calificación: D")
            
        # Operador ternario - Condicional en una línea
        edad: int = 20
        mensaje: str = "Mayor de edad" if edad >= 18 else "Menor de edad"
        print(mensaje)
        
        # Condicionales anidados - Condiciones dentro de condiciones
        usuario: str = "admin"
        password: str = "123"
        if usuario == "admin":
            if password == "123":
                print("Acceso concedido")
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario incorrecto")
            
        # Condicionales con operadores lógicos
        edad: int = 25
        tiene_licencia: bool = True
        if edad >= 18 and tiene_licencia:
            print("Puede conducir")
            
        # Condicional con operador de pertenencia 'in'
        frutas: List[str] = ["manzana", "pera", "uva"]
        if "manzana" in frutas:
            print("Hay manzanas disponibles")
            
        # Condicional con operador de identidad 'is'
        valor: Optional[str] = None
        if valor is None:
            print("La variable es None")
            
        # Match case - Estructura de coincidencia (Python 3.10+)
        dia: str = "lunes"
        match dia:
            case "lunes":
                print("Inicio de semana")
            case "viernes":
                print("Fin de semana laboral")
            case _:
                print("Otro día")

    def bucles(self) -> None:
        # Bucle while - Repetición mientras se cumpla una condición
        print("Bucle while básico:")
        contador: int = 1
        while contador <= 3:
            print(f"Contador: {contador}")
            contador += 1

        # While con else - Se ejecuta cuando la condición es falsa
        print("\nWhile con else:")
        numero: int = 1
        while numero < 3:
            print(f"Número: {numero}")
            numero += 1
        else:
            print("Fin del bucle while")

        # For con range - Iteración sobre un rango de números
        print("\nFor con range:")
        for i in range(3): # (0,1,2)
            print(f"Iteración: {i}")

        # For con range y paso - Iteración con saltos
        print("\nFor con range y paso:")
        for i in range(0, 10, 2):  # (0,2,4,6,8) de 2 en 2
            print(f"Número par: {i}")

        # For con lista - Iteración sobre elementos de una lista
        print("\nFor con lista:")
        frutas: List[str] = ["manzana", "pera", "uva"]
                          #    0          1       2
        for fruta in frutas:
            print(f"Fruta: {fruta}")

        # For con enumerate - Iteración con índice
        print("\nFor con enumerate:")
        for indice, fruta in enumerate(frutas):
         #if indice%2!==0:
            print(f"Índice {indice}: {fruta}")

        # For con diccionario
        print("\nFor con diccionario:")
        persona: Dict[str, Any] = {"nombre": "Juan", "edad": 25}

        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

        # For con break - Interrumpe el bucle
        print("\nFor con break:")
        for i in range(5):
            if i == 3:
                break
            print(f"Número: {i}")

        # For con continue - Salta a la siguiente iteración
        print("\nFor con continue:")
        for i in range(5):
            if i == 2:
                continue
            print(f"Número: {i}")

        # Comprensión de listas - Forma concisa de crear listas
        print("\nComprensión de listas:")
        cuadrados: List[int] = [x**2 for x in range(4)]
        #cuadrados2: List[int] = [] 
        #for x in range(4):
        #    cuadrados.append(x**2)[0,1,4,9]
      

        print(f"Cuadrados: {cuadrados}")

        # Comprensión de diccionarios
        print("\nComprensión de diccionarios:")
        cubos: Dict[int, int] = {x: x**3 for x in range(4)}
        print(f"Cubos: {cubos}")

    def funciones(self) -> None:
        # Función básica sin parámetros
        def saludar():
            print("¡Hola mundo!")
        
        # Función con parámetros
        def sumar(a: int, b: int) -> int:
            return a + b
        
        # Función con parámetros por defecto
        def presentarse(nombre: str, edad: int = 25) -> str:
            return f"Me llamo {nombre} y tengo {edad} años"
        
        # Función con argumentos variables (*args)
        def sumar_varios(*numeros: int) -> int:
            return sum(numeros)
        
        # Función con argumentos de palabra clave variables (**kwargs)
        def mostrar_datos(**datos: Any) -> None:
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
        
        # Función lambda (función anónima)
        cuadrado = lambda x: x**2
        #def cuadrado(x):
        #    return x**2
        
        # Función con tipo de retorno múltiple
        def dividir(a: float, b: float) -> Tuple[float, float]:
            cociente = a / b
            resto = a % b
            return cociente, resto
        
        # Función con documentación (docstring)
        def factorial(n: int) -> int:
            """Calcula el factorial de un número.
            Args:
                n: Número entero positivo
            Returns:
                Factorial de n
            """
            if n == 0:
                return 1
            return n * factorial(n - 1)
        
        # Probando las funciones
        print("Función básica:")
        saludar()
        
        print("\nFunción con parámetros:")
        print(f"Suma: {sumar(5, 3)}")
        
        print("\nFunción con parámetros por defecto:")
        print(presentarse("Ana"))
        print(presentarse("Juan", 30))
        
        print("\nFunción con argumentos variables:")
        print(f"Suma varios: {sumar_varios(1, 2, 3, 4)}")
        
        print("\nFunción con kwargs:")
        mostrar_datos(nombre="Ana", edad=25, ciudad="Quito")
        
        print("\nFunción lambda:")
        print(f"Cuadrado de 4: {cuadrado(4)}")
        
        print("\nFunción con retorno múltiple:")
        coc, res = dividir(10, 3)
        print(f"División 10/3: Cociente = {coc:.2f}, Resto = {res}")
        
        print("\nFunción con docstring:")
        print(f"Factorial de 5: {factorial(5)}")
        print("Documentación:", factorial.__doc__)

    def operaciones_listas(self) -> None:
        # Crear listas de ejemplo
        lista1: List[int] = [1, 2, 3, 4, 5]
        lista2: List[int] = [6, 7, 8, 9, 10]
        numeros: List[int] = [10, 5, 8, 1, 9, 3]
        
        # Operaciones básicas
        print("Operaciones con listas:")
        print(f"Lista 1: {lista1}")
        print(f"Lista 2: {lista2}")
        
        # Concatenación de listas
        concatenada: List[int] = lista1 + lista2
        print(f"\nConcatenación: {concatenada}")
        
        # Suma de elementos
        suma: int = sum(lista1)
        print(f"Suma de lista1: {suma}")
        
        # Máximo y mínimo
        maximo: int = max(numeros)
        minimo: int = min(numeros)
        print(f"Máximo de números: {maximo}")
        print(f"Mínimo de números: {minimo}")
        
        # Ordenamiento
        numeros_ordenados: List[int] = sorted(numeros)
        print(f"Lista ordenada: {numeros_ordenados}")
        numeros.sort(reverse=True)
        print(f"Lista ordenada descendente: {numeros}")
        
        # Invertir lista
        lista1.reverse()
        print(f"Lista1 invertida: {lista1}")
        
        # Contar ocurrencias
        lista_repetidos: List[int] = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        print(f"Número de veces que aparece 3: {lista_repetidos.count(3)}")
        
        # Copiar lista
        copia_superficial: List[int] = lista1.copy()
        print(f"Copia de lista1: {copia_superficial}")
        
        # Extender lista
        lista1.extend([6, 7, 8])
        print(f"Lista1 extendida: {lista1}")
        
        # Insertar en posición específica
        lista2.insert(2, 100)
        print(f"Lista2 con nuevo elemento: {lista2}")
        
        # Eliminar último elemento
        ultimo: int = lista2.pop()
        print(f"Último elemento eliminado: {ultimo}")
        print(f"Lista2 después de pop: {lista2}")
        
        # Eliminar por valor
        lista2.remove(100)
        print(f"Lista2 después de remove(100): {lista2}")
        
        # Limpiar lista
        lista2.clear()
        print(f"Lista2 después de clear: {lista2}")

    def operaciones_tuplas(self) -> None:
        # Creación de tuplas de diferentes formas
        tupla1: Tuple[int, ...] = (1, 2, 3, 4, 5)  # Tupla de enteros
        tupla2: Tuple[Any, ...] = (6, "python", True, 3.14)  # Tupla con diferentes tipos de datos
        numeros: Tuple[int, ...] = (10, 5, 8, 1, 9, 3, 5, 5)  # Tupla con números repetidos
        
        # Mostramos las tuplas originales
        print("Operaciones con tuplas:")
        print(f"Tupla1: {tupla1}")  # Tupla de enteros
        print(f"Tupla2: {tupla2}")  # Tupla mixta
        
        # Concatenación: Une dos tuplas en una nueva
        concatenada: Tuple[Any, ...] = tupla1 + tupla2
        print(f"\nConcatenación de tupla1 y tupla2: {concatenada}")
        
        # Multiplicación: Repite los elementos de la tupla
        repetida: Tuple[int, ...] = tupla1 * 2
        print(f"Tupla1 repetida dos veces: {repetida}")
        
        # Acceso a elementos
        print(f"Primer elemento de tupla1: {tupla1[0]}")  # Índice positivo
        print(f"Último elemento de tupla1: {tupla1[-1]}")  # Índice negativo
        
        # Slicing: Obtener subtuplas
        print(f"Elementos del 1 al 3: {tupla1[1:4]}")  # Excluye el índice final
        print(f"Primeros tres elementos: {tupla1[:3]}")  # Desde el inicio
        print(f"Últimos tres elementos: {tupla1[-3:]}")  # Hasta el final
        
        # Funciones integradas para tuplas
        print(f"\nLongitud de tupla2: {len(tupla2)}")  # Número de elementos
        print(f"Valor máximo en tupla1: {max(tupla1)}")  # Elemento mayor
        print(f"Valor mínimo en tupla1: {min(tupla1)}")  # Elemento menor
        
        # Métodos de tuplas
        print(f"Número de veces que aparece 5: {numeros.count(5)}")  # Contar ocurrencias
        print(f"Posición del primer 5: {numeros.index(5)}")  # Encontrar índice
        
        # Verificación de pertenencia
        print(f"¿Existe el 3 en tupla1?: {3 in tupla1}")  # Operador in
        print(f"¿Existe el 7 en tupla1?: {7 not in tupla1}")  # Operador not in
        
        # Conversión entre tipos
        lista_temporal: List[int] = list(tupla1)  # Tupla a lista
        lista_temporal.append(6)  # Modificamos la lista
        nueva_tupla: Tuple[int, ...] = tuple(lista_temporal)  # Lista a tupla
        print(f"Tupla convertida a lista y de vuelta a tupla: {nueva_tupla}")
        
        # Desempaquetado de tuplas
        a, b, c, *resto = tupla2  # El asterisco recoge los elementos restantes
        print("\nDesempaquetado de tupla2:")
        print(f"a: {a}, b: {b}, c: {c}, resto: {resto}")
        
        # Tuplas anidadas (tuplas dentro de tuplas)
        tupla_anidada: Tuple[Any, ...] = (1, (2, 3), (4, 5, 6))
                                      #   0     1         2
                                      #   0   0   1   0  1   2
        print(f"\nTupla anidada: {tupla_anidada}")
        print(f"Segundo elemento de la segunda tupla interna: {tupla_anidada[1][1]}")
  
    def operaciones_diccionarios(self) -> None:
        # Crear diccionarios de ejemplo
        persona: Dict[str, Any] = {
            "nombre": "Juan",
            "edad": 25,
            "ciudad": "Guayaquil",
            "hobbies": ["música", "deportes", "lectura"]
        }
        
        calificaciones: Dict[str, float] = {
            "matemáticas": 90.5,
            "historia": 85.0,
            "ciencias": 92.0
        }
        
        # Acceso a elementos
        print("Operaciones con diccionarios:")
        print(f"Diccionario persona: {persona}")
        print(f"Nombre: {persona['nombre']}")
        print(f"Hobby principal: {persona['hobbies'][0]}")
        
        # Método get (acceso seguro)
        print(f"\nTeléfono: {persona.get('telefono', 'No disponible')}")
        
        # Modificar valores
        persona["edad"] = 26
        persona["telefono"] = "0991234567"
        print(f"Diccionario actualizado: {persona}")
        
        # Agregar nuevos elementos
        calificaciones["inglés"] = 88.5
        print(f"\nCalificaciones actualizadas: {calificaciones}")
        
        # Eliminar elementos
        del persona["telefono"]
        eliminado = calificaciones.pop("historia")
        print(f"Calificación eliminada: {eliminado}")
        
        # Métodos principales
        print("\nMétodos de diccionarios:")
        print(f"Claves: {list(persona.keys())}")
        print(f"Valores: {list(persona.values())}")
        print(f"Items: {list(persona.items())}")
        
        # Verificar existencia de claves
        print(f"\n¿Existe 'nombre'?: {'nombre' in persona}")
        print(f"¿Existe 'apellido'?: {'apellido' in persona}")
        
        # Combinar diccionarios
        info_adicional: Dict[str, Any] = {
            "apellido": "Pérez",
            "profesion": "Ingeniero"
        }
        persona.update(info_adicional)
        print(f"\nDiccionario combinado: {persona}")
        
        # Diccionario por comprensión
        numeros: Dict[int, int] = {x: x**2 for x in range(5)}
        print(f"\nCuadrados: {numeros}")
        
        # Copiar diccionarios
        copia_superficial: Dict[str, Any] = persona.copy()
        print(f"\nCopia del diccionario: {copia_superficial}")
        
        # Limpiar diccionario
        copia_superficial.clear()
        print(f"Diccionario después de clear(): {copia_superficial}")
        
        # Diccionarios anidados
        universidad: Dict[str, Dict[str, Any]] = {
            "estudiante": {
                "nombre": "María",
                "edad": 20,
                "carrera": "Sistemas"
            },
            "profesor": {
                "nombre": "Carlos",
                "edad": 45,
                "materia": "Programación"
            }
        }
        print(f"\nDiccionario anidado:")
        print(f"Estudiante: {universidad['estudiante']}")
        print(f"Profesor de: {universidad['profesor']['materia']}")

    def operaciones_conjuntos(self) -> None:
        # Crear conjuntos de ejemplo
        conjunto1: Set[int] = {1, 2, 3, 4, 5}
        conjunto2: Set[int] = {4, 5, 6, 7, 8}
        numeros: Set[int] = {1, 2, 2, 3, 3, 3}  # Los duplicados se eliminan automáticamente
        
        # Operaciones básicas
        print("Operaciones con conjuntos:")
        print(f"Conjunto1: {conjunto1}")
        print(f"Conjunto2: {conjunto2}")
        print(f"Números (sin duplicados): {numeros}")
        
        # Operaciones de conjuntos
        print("\nOperaciones de conjuntos:")
        print(f"Unión: {conjunto1 | conjunto2}")
        print(f"Intersección: {conjunto1 & conjunto2}")
        print(f"Diferencia: {conjunto1 - conjunto2}")
        print(f"Diferencia simétrica: {conjunto1 ^ conjunto2}")
        
        # Métodos de conjuntos
        # Agregar elementos
        conjunto1.add(6)
        print(f"\nConjunto1 después de add(6): {conjunto1}")
        
        # Agregar múltiples elementos
        conjunto1.update([7, 8, 9])
        print(f"Conjunto1 después de update([7, 8, 9]): {conjunto1}")
        
        # Eliminar elementos
        conjunto1.remove(9)  # Lanza error si no existe
        print(f"Conjunto1 después de remove(9): {conjunto1}")
        
        conjunto1.discard(10)  # No lanza error si no existe
        print(f"Conjunto1 después de discard(10): {conjunto1}")
        
        # Eliminar y retornar un elemento aleatorio
        elemento = conjunto1.pop()
        print(f"Elemento eliminado con pop(): {elemento}")
        print(f"Conjunto1 después de pop(): {conjunto1}")
        
        # Verificar subconjuntos y superconjuntos
        A: Set[int] = {1, 2, 3}
        B: Set[int] = {1, 2, 3, 4, 5}
        print(f"\nA es subconjunto de B: {A.issubset(B)}")
        print(f"B es superconjunto de A: {B.issuperset(A)}")
        
        # Verificar conjuntos disjuntos
        C: Set[int] = {7, 8, 9}
        print(f"A y C son disjuntos: {A.isdisjoint(C)}")
        
        # Copiar conjuntos
        copia: Set[int] = conjunto1.copy()
        print(f"\nCopia de conjunto1: {copia}")
        
        # Limpiar conjunto
        copia.clear()
        print(f"Conjunto después de clear(): {copia}")
        
        # Conjunto por comprensión
        pares: Set[int] = {x for x in range(10) if x % 2 == 0}
        print(f"\nConjunto de números pares: {pares}")
        
        # Conjuntos inmutables (frozenset)
        inmutable: frozenset = frozenset([1, 2, 3])
        print(f"\nConjunto inmutable: {inmutable}")
        
        # Verificar pertenencia
        print(f"\n¿2 está en conjunto1?: {2 in conjunto1}")
        print(f"¿10 no está en conjunto1?: {10 not in conjunto1}")

    def excepciones(self) -> None:
        print("Manejo de excepciones en Python:")
        
        # Try-except básico: Maneja errores de conversión de tipos
        # ValueError ocurre cuando no se puede convertir un string a número
        try:
            numero: int = int("abc")  # Intenta convertir una cadena no numérica
        except ValueError as e:
            print(f"Error de conversión: {e}")  # Captura y muestra el mensaje de error
            
        # Múltiples excepciones: Maneja diferentes tipos de errores en un mismo bloque
        try:
            lista: List[int] = [1, 2, 3]
            print(lista[10])  # IndexError: índice fuera del rango de la lista
            resultado = 10 / 0  # ZeroDivisionError: división entre cero
        except IndexError as e:
            print(f"Error de índice: {e}")  # Se ejecuta si ocurre error de índice
        except ZeroDivisionError as e:
            print(f"Error de división: {e}")  # Se ejecuta si ocurre división por cero
            
        # Try-except-else: El bloque else se ejecuta si no ocurre ninguna excepción
        try:
            numero = int("123")  # Conversión exitosa
        except ValueError:
            print("No es un número válido")
        else:
            print(f"Conversión exitosa: {numero}")  # Se ejecuta si no hay errores
            
        # Try-except-finally: Finally siempre se ejecuta, haya o no excepciones
        archivo = None
        try:
            archivo = open("archivo_no_existe.txt", "r")  # Intenta abrir un archivo
            contenido = archivo.read()
        except FileNotFoundError as e:
            print(f"Error de archivo: {e}")  # Se ejecuta si el archivo no existe
        finally:
            if archivo:
                archivo.close()  # Cierra el archivo si está abierto
                print("Archivo cerrado")  # Siempre se ejecuta
                
        # Raise: Lanzar excepciones manualmente
        def verificar_edad(edad: int) -> None:
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")  # Lanza excepción personalizada
            print(f"Edad válida: {edad}")
            
        try:
            verificar_edad(-5)  # Intenta verificar una edad inválida
        except ValueError as e:
            print(f"Error de validación: {e}")  # Captura la excepción lanzada
            
        # Excepciones personalizadas: Crear nuestras propias clases de excepciones
        class MiError(Exception):
            def __init__(self, mensaje: str) -> None:
                self.mensaje = mensaje
                super().__init__(self.mensaje)
            
        try:

            raise MiError("Este es un error personalizado")  # Lanza excepción personalizada
        except MiError as e:
            print(f"Error personalizado: {e}")  # Captura la excepción personalizada
            
        # Assert: Verifica condiciones y lanza AssertionError si no se cumplen
        try:
            x: int = -10
            assert x > 0, "El número debe ser positivo"  # Verifica condición
        except AssertionError as e:
            print(f"Error de aserción: {e}")  # Captura el error de aserción
            
        # Try con tipos específicos: Maneja errores de tipos de datos
        #capturar cualquier excepción: Maneja cualquier tipo de error
        try:
            1/0  # División por cero
        except Exception as e:
            # Muestra el tipo de excepción y el mensaje
            print(f"Error general: {type(e).__name__} - {e}")


    def decoradores(self) -> None:
        print("Ejemplos de Decoradores en Python:")
        
        # Los decoradores son funciones que modifican el comportamiento de otras funciones
        # Se utilizan con el símbolo @ seguido del nombre del decorador
        # Son útiles para añadir funcionalidad sin modificar la función original
        
        # Este decorador verifica si el denominador es cero antes de realizar la división
        def validar_division(funcion_original):
            def funcion_decorada(a: float, b: float) -> float:
                # Aquí podemos añadir código antes de ejecutar la función
                if b == 0:
                    print("¡Error! No se puede dividir por cero")
                    return 0
                # Llamamos a la función original
                resultado = funcion_original(a, b)
                # Aquí podemos añadir código después de ejecutar la función
                print(f"La división de {a} entre {b} es: {resultado}")
                return resultado
            return funcion_decorada
        
        # Aplicamos el decorador a la función dividir
        @validar_division
        def dividir(a: float, b: float) -> float:
            return a / b
        
        # Probando la función decorada
        print("\nProbando división con decorador:")
        dividir(10, 2)  # División normal
        dividir(10, 0)  # Intento de división por cero
    # extraer valores - destructuracion de datos
    def unpacking(self) -> None:
        print("Ejemplos de Unpacking en Python:")
        
        # 1. Unpacking básico con listas
        print("\nUnpacking básico:")
        numeros = [1, 2]
        a, b = numeros  # Desempaqueta la lista en variables individuales
        print(f"a: {a}, b: {b}")
        
        # 2. Unpacking extendido usando *
        print("\nUnpacking extendido:")
        lista = [1, 2, 3, 4, 5]
        primero, *resto, ultimo = lista  # * captura elementos del medio
        print(f"Primero: {primero}")
        print(f"Resto: {resto}")
        print(f"Último: {ultimo}")
        
        # 3. Unpacking en diccionarios con **
        print("\nUnpacking de diccionarios:")
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        dict_combinado = {**dict1, **dict2}  # Combina diccionarios
        print(f"Diccionario combinado: {dict_combinado}")
        
        # 4. Unpacking en funciones
        def suma(a: int, b: int, c: int) -> int:
            return a + b + c
        
        numeros = [1, 2, 3]
        resultado = suma(*numeros)  # Desempaqueta la lista como argumentos
        print(f"\nResultado de suma usando unpacking: {resultado}")
        
        # 5. Unpacking en bucles
        print("\nUnpacking en bucle:")
        coordenadas = [(1, 2), (3, 4), (5, 6)]
        for x, y in coordenadas:  # Desempaqueta cada tupla
            print(f"x: {x}, y: {y}")

    def funciones_orden_superior(self) -> None:
            from functools import reduce
            print("Ejemplos de Funciones de Orden Superior:")
            
            # Lista base para los ejemplos
            numeros: List[int] = [1, 2, 3, 4, 5]
            print(f"Lista original: {numeros}")
            
            # Map: transforma cada elemento según una función
            x= map(lambda x: x**2, numeros)
            print(f"Cuadrados usando map: {x}")
            cuadrados = list(map(lambda x: x**2, numeros))
            print(f"\nCuadrados usando map: {cuadrados}")
            
            # Ejemplo adicional de map con múltiples listas
            lista1 = [1, 2, 3]
            lista2 = [10, 20, 30]
            suma_listas = list(map(lambda x, y: x + y, lista1, lista2))
            print(f"Suma de elementos: {suma_listas}")
            
            # Filter: filtra elementos según una condición
            pares = list(filter(lambda x: x % 2 == 0, numeros))
            print(f"\nNúmeros pares usando filter: {pares}")
            mayores_tres = list(filter(lambda x: x > 3, numeros))
            print(f"Números mayores que 3: {mayores_tres}")
            
            # Reduce: reduce una secuencia a un solo valor
            suma = reduce(lambda x, y: x + y, numeros,10)
            print(f"\nSuma total usando reduce: {suma}")
            
            # Ejemplo adicional de reduce
            producto = reduce(lambda x, y: x * y, numeros)
            print(f"Producto total: {producto}")
    
    def archivos(self) -> None:
        import json
        print("Ejemplos de manejo de archivos:")
        
        # ====== MANEJO DE ARCHIVOS DE TEXTO ======
        print("\nManejo de archivo de texto:")
        try:
            # Abrimos el archivo en modo escritura ('w')
            # Si el archivo no existe, lo crea
            # Si existe, lo sobrescribe
            with open("d:/daniel/unemi/Primer Semestre 2025/POO/POO/practica1/ejemplo.txt", "w") as archivo:
                # Escribimos líneas individuales
                archivo.write("Primera línea de texto\n")  # \n para salto de línea
                archivo.write("Segunda línea de texto\n")
                
                # Escribimos múltiples líneas a la vez
                archivo.writelines(["Tercera línea\n", "Cuarta línea\n"])
            
            # Abrimos el archivo en modo lectura ('r')
            # El bloque 'with' asegura que el archivo se cierre correctamente
            with open("d:/daniel/unemi/Primer Semestre 2025/POO/POO/practica1/ejemplo.txt", "r") as archivo:
                # Leemos todo el contenido del archivo de una vez
                contenido = archivo.read()
                print("Contenido completo:")
                print(contenido)
                
        except FileNotFoundError as e:
            # Manejamos el error si el archivo no se encuentra
            print(f"Error con archivo de texto: {e}")
            
        # ====== MANEJO DE ARCHIVOS JSON ======
        print("\nManejo de archivo JSON:")
        # Creamos un diccionario con datos estructurados
        datos = {
            "estudiantes": [
                {
                    "nombre": "Juan",
                    "edad": 20,
                    "cursos": ["Python", "Java", "SQL"]
                },
                {
                    "nombre": "María",
                    "edad": 22,
                    "cursos": ["JavaScript", "HTML", "CSS"]
                }
            ]
        }
        
        try:
            # json.dump() - Serializa (convierte) un objeto Python a formato JSON y lo guarda en un archivo
            # Útil para guardar diccionarios, listas y otros objetos Python en formato JSON
            # indent=4 da formato legible con sangría de 4 espacios
            with open("d:/daniel/unemi/Primer Semestre 2025/POO/POO/practica1/datos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
            
            # json.load() - Lee un archivo JSON y lo deserializa (convierte) a un objeto Python
            # Convierte el JSON a diccionarios y listas de Python que podemos manipular
            with open("d:/daniel/unemi/Primer Semestre 2025/POO/POO/practica1/datos.json", "r") as archivo:
                datos_leidos = json.load(archivo)
                
            # Accedemos y mostramos los datos estructurados
            print("Datos leídos del JSON:")
            for estudiante in datos_leidos["estudiantes"]:
                print(f"\nNombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")
                print(f"Cursos: {', '.join(estudiante['cursos'])}")
                
        except FileNotFoundError as e:
            # Manejamos el error si hay problemas con el archivo
            print(f"Error con archivo JSON: {e}")

# Instancia la clase y se crea un objeto llamado ejer1
ejer1 = Ejercicios()
#ejer1.variables()
#ejer1.operadores()
#ejer1.entrada_salida()
#ejer1.condicionales()
#ejer1.bucles()
#ejer1.funciones()
#ejer1.operaciones_listas()
#ejer1.operaciones_tuplas()
#ejer1.operaciones_diccionarios()
#ejer1.operaciones_conjuntos()
#ejer1.excepciones()
#ejer1.decoradores()
#ejer1.unpacking()
#ejer1.funciones_orden_superior()
#ejer1.archivos()
















