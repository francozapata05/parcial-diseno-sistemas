"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

"""
Excepcion base para el sistema de forestacion.
"""

class ForestacionException(Exception):
    """Clase base para excepciones del sistema."""
    def __init__(self, user_message: str, technical_message: str):
        super().__init__(f"{user_message} ({technical_message})")
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_technical_message(self) -> str:
        return self._technical_message

    def get_full_message(self) -> str:
        return str(self)


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

"""
Centralizacion de mensajes de error para excepciones.
"""

# Superficie
USER_SUPERFICIE_INSUFICIENTE = "La superficie de la plantacion es insuficiente."
TECH_SUPERFICIE_INSUFICIENTE = "Superficie requerida excede la disponible."

# Agua
USER_AGUA_AGOTADA = "El agua de la plantacion esta agotada."
TECH_AGUA_AGOTADA = "No hay suficiente agua para completar la operacion."

# Persistencia
USER_PERSISTENCIA_ESCRITURA = "Error al guardar el registro."
TECH_PERSISTENCIA_ESCRITURA = "Fallo la operacion de escritura en disco."
USER_PERSISTENCIA_LECTURA = "Error al leer el registro."
TECH_PERSISTENCIA_LECTURA = "Fallo la operacion de lectura de disco."
USER_PERSISTENCIA_NO_ENCONTRADO = "El registro solicitado no existe."
TECH_PERSISTENCIA_NO_ENCONTRADO = "El archivo no fue encontrado en el directorio de datos."


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

"""
Excepcion para errores de persistencia.
"""

from enum import Enum
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class TipoOperacion(Enum):
    LECTURA = "lectura"
    ESCRITURA = "escritura"

class PersistenciaException(ForestacionException):
    """Lanzada cuando ocurren errores de I/O en persistencia."""
    def __init__(self, user_message: str, technical_message: str, nombre_archivo: str, tipo_operacion: TipoOperacion):
        super().__init__(user_message, f"{technical_message} en archivo: {nombre_archivo}")
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

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


