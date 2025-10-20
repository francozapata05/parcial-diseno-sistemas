"""
Servicio para Plantacion.
"""

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_MINIMA

class PlantacionService:
    """Servicio para operaciones de Plantacion."""
    def __init__(self):
        self._cultivo_service_registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> None:
        superficie_requerida = 0
        # No se puede instanciar directamente, pero para calcular superficie es ok
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        if plantacion.get_superficie_disponible() < superficie_requerida:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                plantacion.get_superficie_disponible()
            )

        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.add_cultivo(nuevo_cultivo)

    def regar(self, plantacion: Plantacion) -> None:
        if plantacion.get_agua_disponible() < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, plantacion.get_agua_disponible())

        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_MINIMA)

        for cultivo in plantacion.get_cultivos():
            self._cultivo_service_registry.absorber_agua(cultivo)

    def cosechar(self, plantacion: Plantacion) -> None:
        # Logica de cosecha aqui
        pass

    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        print(f"Fumigando plantacion con: {plaguicida}")
