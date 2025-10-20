"""
Entidad Herramienta.
"""

class Herramienta:
    """Herramienta de trabajo con certificacion."""
    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def has_certificado_hys(self) -> bool:
        return self._certificado_hys
