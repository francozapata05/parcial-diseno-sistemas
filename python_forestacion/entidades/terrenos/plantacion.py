"""
Entidad Plantacion.
"""

from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """Representa una plantacion agricola."""
    def __init__(self, nombre: str, superficie: float, agua: int):
        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List[Cultivo] = []
        self._trabajadores: List[Trabajador] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_total(self) -> float:
        return self._superficie

    def get_superficie_ocupada(self) -> float:
        return sum(c.get_superficie() for c in self._cultivos)

    def get_superficie_disponible(self) -> float:
        return self.get_superficie_total() - self.get_superficie_ocupada()

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()  # Defensive copy

    def add_cultivo(self, cultivo: Cultivo) -> None:
        self._cultivos.append(cultivo)

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()  # Defensive copy

    def set_trabajadores(self, trabajadores: List[Trabajador]) -> None:
        self._trabajadores = trabajadores
