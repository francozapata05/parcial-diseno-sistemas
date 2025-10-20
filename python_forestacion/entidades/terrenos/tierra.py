"""
Entidad Tierra.
"""

class Tierra:
    """Representa un terreno catastral."""
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio
