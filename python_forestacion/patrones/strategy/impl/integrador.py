"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ================================================================================

"""
Estrategia de absorcion de agua constante.
"""

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Absorcion de una cantidad constante de agua."""
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        return self._cantidad


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ================================================================================

"""
Estrategia de absorcion de agua estacional.
"""

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Absorcion diferenciada por estacion (verano/invierno)."""
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


