"""
Servicio para gestionar multiples fincas.
"""

from typing import Dict, Type
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete

class FincasService:
    """Servicio para operaciones de alto nivel en multiples fincas."""
    def __init__(self):
        self._fincas: Dict[int, RegistroForestal] = {}

    def add_finca(self, registro: RegistroForestal) -> None:
        self._fincas[registro.get_id_padron()] = registro

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        if id_padron not in self._fincas:
            raise ValueError(f"Finca con padron {id_padron} no encontrada.")
        return self._fincas[id_padron]

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        self.buscar_finca(id_padron)
        print(f"Fumigando plantacion con: {plaguicida}")
        # En un sistema real, se iteraria sobre los cultivos y se aplicaria el efecto

    def cosechar_yempaquetar(self, tipo_cultivo: Type[Cultivo]) -> Paquete:
        paquete = Paquete(tipo_cultivo)
        cultivos_cosechados = []

        for finca in self._fincas.values():
            plantacion = finca.get_plantacion()
            cultivos_en_plantacion = plantacion.get_cultivos()
            
            for cultivo in cultivos_en_plantacion:
                if isinstance(cultivo, tipo_cultivo):
                    cultivos_cosechados.append(cultivo)
            
            # Remover cultivos cosechados de la plantacion
            cultivos_restantes = [c for c in cultivos_en_plantacion if c not in cultivos_cosechados]
            setattr(plantacion, '_cultivos', cultivos_restantes)

        for cultivo in cultivos_cosechados:
            paquete.agregar_cultivo(cultivo)

        print(f"COSECHANDO {len(cultivos_cosechados)} unidades de {tipo_cultivo}")
        return paquete
