"""
Servicio para Pino.
"""

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """Servicio para Pino."""

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Pino') -> int:
        agua_absorvida = super().absorver_agua(cultivo)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_PINO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
