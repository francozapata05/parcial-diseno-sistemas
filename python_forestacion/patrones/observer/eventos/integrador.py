"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ================================================================================

"""
Evento de plantacion para el patron Observer.
"""

from datetime import datetime

class EventoPlantacion:
    """Representa un evento en una plantacion."""
    def __init__(self, descripcion: str):
        self._descripcion = descripcion
        self._timestamp = datetime.now()

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_timestamp(self) -> datetime:
        return self._timestamp


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ================================================================================

"""
Evento de sensor para el patron Observer.
"""

from datetime import datetime

class EventoSensor:
    """Representa un evento de un sensor."""
    def __init__(self, valor: float, unidad: str):
        self._valor = valor
        self._unidad = unidad
        self._timestamp = datetime.now()

    def get_valor(self) -> float:
        return self._valor

    def get_unidad(self) -> str:
        return self._unidad

    def get_timestamp(self) -> datetime:
        return self._timestamp


