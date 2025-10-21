"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\fincas_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\paquete.py
# ================================================================================

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


