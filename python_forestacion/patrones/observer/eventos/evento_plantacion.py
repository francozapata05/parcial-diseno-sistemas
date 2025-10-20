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
