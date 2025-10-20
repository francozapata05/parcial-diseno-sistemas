"""
Excepcion para cuando la superficie es insuficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    USER_SUPERFICIE_INSUFICIENTE,
    TECH_SUPERFICIE_INSUFICIENTE
)

class SuperficieInsuficienteException(ForestacionException):
    """Lanzada cuando no hay suficiente superficie para plantar."""
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        super().__init__(
            USER_SUPERFICIE_INSUFICIENTE,
            f"{TECH_SUPERFICIE_INSUFICIENTE} Requerida: {superficie_requerida}, Disponible: {superficie_disponible}"
        )
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible
