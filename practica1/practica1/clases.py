from abc import ABC, abstractmethod
"""  Este ejemplo implementa:
Clases y objetos
Abstracción
Encapsulamiento
Herencia
Polimorfismo
CLASE:
- Persona es una plantilla/molde que define las características y comportamientos
- Define la estructura de datos (atributos) y métodos que tendrán los objetos
- Actúa como un tipo de dato personalizado
OBJETO: instancia de la clase
ABSTRACCIÓN:
- Modela una persona del mundo real con sus atributos esenciales (nombre, apellido, edad, etc)
- Expone métodos que representan el comportamiento relevante (mostrar_datos, nombre_completo)
- Oculta la complejidad interna y muestra una interfaz simple de usar
- Properties (cedula, nombre_completo) que controlan el acceso a los datos
- Métodos que gestionan la manipulación de los atributos de forma segura
"""
class Persona:
    # __init__ Constructor de la clase se ejecuta cuando se crea una instancia de la clase 
    # sirve para inicializar los atributos de la clase
    def __init__(
        self,
        nombre: str,
        apellido: str,
        edad: int,
        email: str,
        cedula: str= "9999999999" # atributos de instancia
      
    ) -> None:
        self._nombre: str = nombre  # (-) Atributos protegidos (encapsulamiento nivel bajo)
        self._apellido: str = apellido
        self.edad: int = edad # Atributo publico sin guion bajo
        self.__cedula: str = cedula  # (__) Atributo privado (encapsulamiento fuerte)
        self._email: str = email
    
    # Property so metodos para acceso controlado al atributo privado
    @property
    def cedula(self) -> str:
       return self.__cedula
    # Setter que permite modificar el atributo privado de forma controlada
    @cedula.setter
    def cedula(self, cedula: str) -> None:
       if len(cedula) != 10:
           self.__cedula= "9999999999"
       else:
           self.__cedula= cedula

    # Property para el nombre completo 
    @property
    def nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"
    # @abstractmethod
    def mostrar_datos(self) -> str:
        email_info: str = f"Email: {self._email}" if self._email else "Email: No proporcionado"
        return (
            f"Datos de la Persona:\n"
            f"Nombre Completo: {self.nombre_completo}\n"
            f"Edad: {self.edad}\n"
            f"Cédula: {self.__cedula}\n"
            f"{email_info}"
        )

# Ejemplo de uso
if __name__ == "__main__":
    """OBJETO:
- persona1 y persona2 son instancias/objetos creados a partir de la clase Persona
- Cada objeto tiene sus propios datos pero comparte la estructura definida en la clase
- Los objetos pueden acceder a los métodos definidos en su clase """
    persona1 = Persona("Juan","Pérez", 25, "juan@email.com","0123456789" )
    persona2 = Persona("María", "López", 30, "ml@gmail.com")
    
    # Mostrar los datos
    print(persona1.mostrar_datos())
    print("\n" + persona2.mostrar_datos())
    
    # Ejemplo de uso de property
    print(f"\nCédula de persona1: {persona1.cedula}")
    persona1.cedula = "4444444444"
    print(f"Nueva cédula de persona1: {persona1.cedula}")
  

 
 
 
 
 