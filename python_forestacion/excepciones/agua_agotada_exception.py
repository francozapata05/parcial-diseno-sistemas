"""
Excepcion para cuando el agua esta agotada.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    USER_AGUA_AGOTADA,
    TECH_AGUA_AGOTADA
)

class AguaAgotadaException(ForestacionException):
    """Lanzada cuando no hay suficiente agua para regar."""
    def __init__(self, agua_requerida: int, agua_disponible: int):
        super().__init__(
            USER_AGUA_AGOTADA,
            f"{TECH_AGUA_AGOTADA} Requerida: {agua_requerida}, Disponible: {agua_disponible}"
        )
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

    def get_agua_requerida(self) -> int:
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        return self._agua_disponible
