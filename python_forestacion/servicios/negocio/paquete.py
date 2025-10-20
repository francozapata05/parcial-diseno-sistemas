"""
Clase generica para empaquetar cultivos.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')

class Paquete(Generic[T]):
    """Caja generica para empaquetar un tipo de cultivo."""
    _id_counter = 0

    def __init__(self, tipo_cultivo: type):
        Paquete._id_counter += 1
        self._id_paquete = Paquete._id_counter
        self._tipo_cultivo = tipo_cultivo
        self._contenido: List[T] = []

    def agregar_cultivo(self, cultivo: T) -> None:
        if not isinstance(cultivo, self._tipo_cultivo):
            raise TypeError(f"Solo se pueden agregar cultivos de tipo {self._tipo_cultivo.__name__}")
        self._contenido.append(cultivo)

    def get_contenido(self) -> List[T]:
        return self._contenido.copy()

    def mostrar_contenido_caja(self) -> None:
        print("Contenido de la caja:")
        print(f"  Tipo: {self._tipo_cultivo.__name__}")
        print(f"  Cantidad: {len(self._contenido)}")
        print(f"  ID Paquete: {self._id_paquete}")
