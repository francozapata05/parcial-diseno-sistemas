"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

"""
Clase base para cultivos de tipo arbol.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """Clase abstracta para arboles."""
    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        self._altura = altura


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

"""
Clase base para cultivos de tipo hortaliza.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase abstracta para hortalizas."""
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def is_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

"""
Entidad Lechuga.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)

class Lechuga(Hortaliza):
    """Entidad Lechuga - solo datos."""

    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

"""
Entidad Olivo.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO
)

class Olivo(Arbol):
    """Entidad Olivo - solo datos."""

    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=0.5  # Altura inicial mas baja
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        self._tipo_aceituna = tipo_aceituna


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

"""
Entidad Pino.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL
)

class Pino(Arbol):
    """Entidad Pino - solo datos."""

    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

"""
Enum para los tipos de aceituna.
"""

from enum import Enum

class TipoAceituna(Enum):
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

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


