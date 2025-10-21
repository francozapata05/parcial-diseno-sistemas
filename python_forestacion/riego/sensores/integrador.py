"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\humedad_reader_task.py
# ================================================================================

"""
Sensor de humedad en tiempo real.
"""

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Lee la humedad ambiental y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_humedad(self) -> float:
        return round(random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX), 2)

    def run(self):
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def detener(self) -> None:
        self._detenido.set()


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\temperatura_reader_task.py
# ================================================================================

"""
Sensor de temperatura en tiempo real.
"""

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Lee la temperatura ambiental y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        self._detenido.set()


