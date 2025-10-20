"""
Servicio para RegistroForestal.
"""

import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.persistencia_exception import PersistenciaException, TipoOperacion
from python_forestacion.excepciones.mensajes_exception import (
    USER_PERSISTENCIA_ESCRITURA,
    TECH_PERSISTENCIA_ESCRITURA,
    USER_PERSISTENCIA_LECTURA,
    TECH_PERSISTENCIA_LECTURA,
    USER_PERSISTENCIA_NO_ENCONTRADO,
    TECH_PERSISTENCIA_NO_ENCONTRADO
)
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

class RegistroForestalService:
    """Servicio para persistencia y visualizacion de RegistroForestal."""
    def __init__(self):
        self._cultivo_service_registry = CultivoServiceRegistry.get_instance()

    def mostrar_datos(self, registro: RegistroForestal) -> None:
        print("REGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie: {registro.get_tierra().get_superficie()}")
        print(f"Cantidad de cultivos plantados: {len(registro.get_plantacion().get_cultivos())}")
        print("Listado de Cultivos plantados")
        print("____________________________")
        for cultivo in registro.get_plantacion().get_cultivos():
            self._cultivo_service_registry.mostrar_datos(cultivo)
            print()

    def persistir(self, registro: RegistroForestal) -> None:
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}{EXTENSION_DATA}")

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente en {nombre_archivo}")
        except IOError as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_ESCRITURA,
                f"{TECH_PERSISTENCIA_ESCRITURA}: {e}",
                nombre_archivo,
                TipoOperacion.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")

        if not os.path.exists(nombre_archivo):
            raise PersistenciaException(
                USER_PERSISTENCIA_NO_ENCONTRADO,
                TECH_PERSISTENCIA_NO_ENCONTRADO,
                nombre_archivo,
                TipoOperacion.LECTURA
            )

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
                print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
                return registro
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_LECTURA,
                f"{TECH_PERSISTENCIA_LECTURA}: {e}",
                nombre_archivo,
                TipoOperacion.LECTURA
            )
