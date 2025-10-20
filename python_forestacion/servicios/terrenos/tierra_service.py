"""
Servicio para Tierra.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

class TierraService:
    """Servicio para operaciones relacionadas con Tierra."""
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        # Acoplamiento aqui, pero aceptable para este caso
        setattr(tierra, '_plantacion', plantacion)
        return tierra

    def get_plantacion(self, tierra: Tierra) -> Plantacion:
        return getattr(tierra, '_plantacion')
