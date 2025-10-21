"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

"""
Servicio base para arboles.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol

class ArbolService(CultivoService):
    """Servicio abstracto para operaciones de arboles."""
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        super().mostrar_datos(cultivo)
        print(f"Altura: {cultivo.get_altura()} m")


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

"""
Servicio base para todos los cultivos.
"""

from abc import ABC
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio abstracto para operaciones de cultivo."""
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            date.today(), 0, 0, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

"""
Registro de servicios de cultivo (Singleton y Registry).
"""

from threading import Lock
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls() # Llama al constructor
        return cls._instance

    def _inicializar_servicios(self):
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def absorber_agua(self, cultivo: Cultivo) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo):
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo):
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo):
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo):
        return self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo):
        return self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo):
        return self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo):
        return self._zanahoria_service.mostrar_datos(cultivo)


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

"""
Servicio para Lechuga.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """Servicio para Lechuga."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.is_invernadero()}")


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================

"""
Servicio para Olivo.
"""

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """Servicio para Olivo."""

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Olivo') -> int:
        agua_absorvida = super().absorver_agua(cultivo)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_OLIVO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().value}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================

"""
Servicio para Zanahoria.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """Servicio para Zanahoria."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")


