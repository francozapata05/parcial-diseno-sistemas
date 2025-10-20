"""
Controlador de riego automatico.
"""

import threading
import time
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controla el riego basado en sensores de temperatura y humedad."""
    def __init__(
        self,
        sensor_temperatura: TemperaturaReaderTask,
        sensor_humedad: HumedadReaderTask,
        plantacion: Plantacion,
        plantacion_service: PlantacionService
    ):
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._ultima_temperatura: float = 20.0
        self._ultima_humedad: float = 60.0
        self._detenido = threading.Event()

        # Suscribirse a los sensores
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float, sender) -> None:
        # Este metodo es llamado por los sensores
        # Se podria diferenciar por tipo de evento si fuera necesario
        if isinstance(sender, TemperaturaReaderTask):
            self._ultima_temperatura = evento
        elif isinstance(sender, HumedadReaderTask):
            self._ultima_humedad = evento

    def run(self):
        while not self._detenido.is_set():
            self._evaluar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)

    def _evaluar_y_regar(self):
        temp = self._ultima_temperatura
        hum = self._ultima_humedad

        print(f"[CONTROL RIEGO] Temp: {temp}°C, Hum: {hum}%")

        if (TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO) and (hum < HUMEDAD_MAX_RIEGO):
            try:
                print("[CONTROL RIEGO] Condiciones optimas. Regando...")
                self._plantacion_service.regar(self._plantacion)
                print("[CONTROL RIEGO] Riego completado.")
            except AguaAgotadaException as e:
                print(f"[CONTROL RIEGO] No se pudo regar: {e.get_user_message()}")
        else:
            print("[CONTROL RIEGO] Condiciones no optimas. No se riega.")

    def detener(self) -> None:
        self._detenido.set()
