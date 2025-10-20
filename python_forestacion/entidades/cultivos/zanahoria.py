"""
Entidad Zanahoria.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)

class Zanahoria(Hortaliza):
    """Entidad Zanahoria - solo datos."""

    def __init__(self, es_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby

    def is_baby_carrot(self) -> bool:
        return self._es_baby

    def set_es_baby(self, es_baby: bool) -> None:
        self._es_baby = es_baby
