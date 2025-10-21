"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

"""
Servicio para Plantacion.
"""

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import AGUA_MINIMA

class PlantacionService:
    """Servicio para operaciones de Plantacion."""
    def __init__(self):
        self._cultivo_service_registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> None:
        superficie_requerida = 0
        # No se puede instanciar directamente, pero para calcular superficie es ok
        cultivo_temporal = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_temporal.get_superficie() * cantidad

        if plantacion.get_superficie_disponible() < superficie_requerida:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                plantacion.get_superficie_disponible()
            )

        for _ in range(cantidad):
            nuevo_cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.add_cultivo(nuevo_cultivo)

    def regar(self, plantacion: Plantacion) -> None:
        if plantacion.get_agua_disponible() < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, plantacion.get_agua_disponible())

        plantacion.set_agua_disponible(plantacion.get_agua_disponible() - AGUA_MINIMA)

        for cultivo in plantacion.get_cultivos():
            self._cultivo_service_registry.absorber_agua(cultivo)

    def cosechar(self, plantacion: Plantacion) -> None:
        # Logica de cosecha aqui
        pass

    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        print(f"Fumigando plantacion con: {plaguicida}")


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

"""
Servicio para Tierra.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

class TierraService:
    """Servicio para operaciones relacionadas con Tierra."""
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        # Acoplamiento aqui, pero aceptable para este caso
        setattr(tierra, '_plantacion', plantacion)
        return tierra

    def get_plantacion(self, tierra: Tierra) -> Plantacion:
        return getattr(tierra, '_plantacion')


