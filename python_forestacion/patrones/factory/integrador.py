"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\factory
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\factory\cultivo_factory.py
# ================================================================================

"""
Factory para la creacion de cultivos.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """Fabrica de cultivos que encapsula la logica de creacion."""
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Olivo:
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        return Zanahoria(es_baby=False)


