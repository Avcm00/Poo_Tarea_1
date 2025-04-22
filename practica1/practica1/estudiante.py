from typing import Dict, List
from datetime import date
from clases import Persona

"""
HERENCIA:
- Estudiante(subclase) hereda de Persona (clase Base)
- Reutiliza atributos y métodos de la clase Persona
- Extiende la funcionalidad agregando atributos y métodos propios de un estudiante
"""
class Estudiante(Persona):
    # Atributo estático para contar estudiantes
    total_estudiantes: int = 0
    
    def __init__(
        self,
        nombre: str,
        apellido: str,
        edad: int,
        email: str,
        cedula: str,
        matricula: str,
        carrera: str,
        fecha_ingreso: date,
        asignaturas: Dict[str, float] | None = None
    ) -> None:
        # Llamada al constructor de la clase padre
        super().__init__(nombre, apellido, edad, email, cedula)
        
        # Atributo privado
        self.__matricula: str = matricula
        # Atributos públicos
        self.carrera: str = carrera
        self.fecha_ingreso: date = fecha_ingreso
        self.asignaturas: Dict[str, float] = asignaturas or {}
        # Incrementar contador de estudiantes
        Estudiante.total_estudiantes += 1

    @property
    def matricula(self) -> str:
        return self.__matricula
    
    
    def __calcular_promedio(self) -> float:
        """
        Método privado para calcular el promedio de notas
        """
        return sum(self.asignaturas.values()) / len(self.asignaturas)
    
    
    def promedio_general(self) -> float:
        if not self.asignaturas:
            return 0.0
        return self.__calcular_promedio()
    
    def agregar_asignatura(self, nombre: str, nota: float) -> None:
        if 0 <= nota <= 10:
            self.asignaturas[nombre] = nota
    
    @staticmethod
    def obtener_periodo_academico(fecha: date) -> str:
        """
        Método estático para determinar el período académico según la fecha
        """
        mes = fecha.month
        año = fecha.year
        if 1 <= mes <= 6:
            return f"Primer Semestre {año}"
        else:
            return f"Segundo Semestre {año}"
    
    """
    POLIMORFISMO:capacidad de un objeto para tomar diferentes formas en diferentes contextos.
    - Método mostrar_datos sobreescrito
    - Se utiliza super() para llamar al método de la clase padre
    - Se extiende la funcionalidad agregando información específica de un estudiante
    """
    def mostrar_datos(self) -> str:
        datos_base = super().mostrar_datos()
        return (
            f"{datos_base}\n"
            f"Matrícula: {self.__matricula}\n"
            f"Carrera: {self.carrera}\n"
            f"Fecha Ingreso: {self.fecha_ingreso.strftime('%d/%m/%Y')}\n"
            f"Promedio General: {self.promedio_general():.2f}\n"
            f"Asignaturas: {', '.join(self.asignaturas.keys())}"
        )

if __name__ == "__main__":
    # Crear estudiante
    fecha_ingreso = date(2024, 1, 15)
    estudiante1 = Estudiante(
        "Ana", "García", 20, 
        "ana@unemi.edu.ec", "0987654321",
        "EST-2024-001", "Ingeniería en Sistemas",
        fecha_ingreso
    )
    
    # Agregar asignaturas y notas
    estudiante1.agregar_asignatura("Programación", 10)
    estudiante1.agregar_asignatura("Base de Datos", 8)
    
    # Mostrar información
    print(estudiante1.mostrar_datos())
    
    # Uso del método estático
    periodo = Estudiante.obtener_periodo_academico(fecha_ingreso)
    print(f"\nPeríodo Académico: {periodo}")
    print(f"Total de estudiantes matriculados: {Estudiante.total_estudiantes}")

    objeto: str = "[+]"