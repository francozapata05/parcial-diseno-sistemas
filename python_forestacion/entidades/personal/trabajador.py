"""
Entidad Trabajador.
"""

from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """Representa un trabajador agricola."""
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico: Optional[AptoMedico] = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas.copy()  # Defensive copy

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico) -> None:
        self._apto_medico = apto
