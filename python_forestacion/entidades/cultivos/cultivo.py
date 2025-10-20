"""
Interfaz base para todos los cultivos.
"""

from abc import ABC

class Cultivo(ABC):
    """Clase abstracta que representa un cultivo."""
    _id_counter = 0

    def __init__(self, agua: int, superficie: float):
        Cultivo._id_counter += 1
        self._id = Cultivo._id_counter
        self._agua = agua
        self._superficie = superficie

    def get_id(self) -> int:
        return self._id

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie
