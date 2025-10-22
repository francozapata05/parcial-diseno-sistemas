"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion
Fecha de generacion: 2025-10-21 20:39:38
Total de archivos integrados: 67
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: ..
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades\terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones\factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones\observer\eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones\singleton
#   38. __init__.py
#
# DIRECTORIO: patrones\strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego\control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego\sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios\cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios\negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios\personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios\terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#


################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 1/67: main.py
# Directorio: .
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\main.py
# ==============================================================================


import time
from datetime import date
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

def main():
    """Punto de entrada principal del sistema."""
    print("=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)

    # Singleton
    print("\n" + "-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)
    plantacion_service = PlantacionService()
    registro_service = RegistroForestalService()
    trabajador_service = TrabajadorService()
    fincas_service = FincasService()
    print("[OK] Todos los servicios comparten la misma instancia del Registry")

    # Creacion de tierra y plantacion
    print("\n1. Creando tierra con plantacion...")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    plantacion = tierra_service.get_plantacion(terreno)
    print(f"[OK] Plantacion '{plantacion.get_nombre()}' creada con {plantacion.get_superficie_total()} m²")

    # Registro Forestal
    print("\n2. Creando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print("[OK] Registro forestal creado.")

    # Factory
    print("\n" + "-" * 70)
    print("  PATRON FACTORY: Plantando cultivos")
    print("-" * 70)
    try:
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 5)
        plantacion_service.plantar(plantacion, "Zanahoria", 5)
        print("[OK] Cultivos plantados exitosamente.")
    except ForestacionException as e:
        print(f"[ERROR] {e.get_user_message()}")

    # Strategy
    print("\n" + "-" * 70)
    print("  PATRON STRATEGY: Regando plantacion")
    print("-" * 70)
    try:
        plantacion_service.regar(plantacion)
        print("[OK] Riego completado.")
    except ForestacionException as e:
        print(f"[ERROR] {e.get_user_message()}")

    # Observer
    print("\n" + "-" * 70)
    print("  PATRON OBSERVER: Sistema de riego automatico")
    print("-" * 70)
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    tarea_control = ControlRiegoTask(tarea_temp, tarea_hum, plantacion, plantacion_service)

    print("[INFO] Iniciando sensores y control de riego...")
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    time.sleep(10)

    print("[INFO] Deteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)
    print("[OK] Sistema de riego detenido.")

    # Gestion de Personal
    print("\n3. Gestion de Personal...")
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]
    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    plantacion.set_trabajadores([trabajador])
    print(f"[OK] Trabajador '{trabajador.get_nombre()}' asignado a la plantacion.")

    trabajador_service.asignar_apto_medico(
        trabajador,
        True,
        date.today(),
        "Estado de salud: excelente"
    )
    print("[OK] Apto medico asignado.")

    herramienta = Herramienta(1, "Pala", True)
    trabajador_service.trabajar(trabajador, date.today(), herramienta)

    # Operaciones de Negocio
    print("\n4. Operaciones de Negocio...")
    fincas_service.add_finca(registro)
    print("[OK] Finca agregada al servicio de fincas.")

    fincas_service.fumigar(1, "insecto organico")

    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()

    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()

    # Persistencia
    print("\n5. Persistencia de Datos...")
    try:
        registro_service.persistir(registro)
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        registro_service.mostrar_datos(registro_leido)
    except ForestacionException as e:
        print(f"[ERROR] {e.get_user_message()}")

    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70)

if __name__ == "__main__":
    main()



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 2/67: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/67: constantes.py
# Directorio: .
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\constantes.py
# ==============================================================================

"""
Modulo de constantes del sistema.
"""

# Agua
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
INTERVALO_CONTROL_RIEGO = 2.5  # segundos
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50  # °C
SENSOR_HUMEDAD_MIN = 0  # %
SENSOR_HUMEDAD_MAX = 100  # %

# Cultivos
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
ALTURA_INICIAL_ARBOL = 1.0  # metros
CRECIMIENTO_PINO = 0.10
SUPERFICIE_OLIVO = 3.0
AGUA_INICIAL_OLIVO = 5
CRECIMIENTO_OLIVO = 0.01
SUPERFICIE_LECHUGA = 0.10
AGUA_INICIAL_LECHUGA = 1
SUPERFICIE_ZANAHORIA = 0.15
AGUA_INICIAL_ZANAHORIA = 0
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
MES_INICIO_VERANO = 3
MES_FIN_VERANO = 8

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# Threads
THREAD_JOIN_TIMEOUT = 2.0  # segundos



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/67: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/67: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/67: arbol.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

"""
Clase base para cultivos de tipo arbol.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """Clase abstracta para arboles."""
    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        self._altura = altura


# ==============================================================================
# ARCHIVO 7/67: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

"""
Interfaz base para todos los cultivos.
"""

from abc import ABC

class Cultivo(ABC):
    """Clase abstracta que representa un cultivo."""
    _id_counter = 0

    def __init__(self, agua: int, superficie: float):
        Cultivo._id_counter += 1
        self._id = Cultivo._id_counter
        self._agua = agua
        self._superficie = superficie

    def get_id(self) -> int:
        return self._id

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero.")
        self._superficie = superficie


# ==============================================================================
# ARCHIVO 8/67: hortaliza.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

"""
Clase base para cultivos de tipo hortaliza.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase abstracta para hortalizas."""
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def is_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero


# ==============================================================================
# ARCHIVO 9/67: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

"""
Entidad Lechuga.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)

class Lechuga(Hortaliza):
    """Entidad Lechuga - solo datos."""

    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad


# ==============================================================================
# ARCHIVO 10/67: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

"""
Entidad Olivo.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO
)

class Olivo(Arbol):
    """Entidad Olivo - solo datos."""

    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=0.5  # Altura inicial mas baja
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        self._tipo_aceituna = tipo_aceituna


# ==============================================================================
# ARCHIVO 11/67: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

"""
Entidad Pino.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL
)

class Pino(Arbol):
    """Entidad Pino - solo datos."""

    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad


# ==============================================================================
# ARCHIVO 12/67: tipo_aceituna.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

"""
Enum para los tipos de aceituna.
"""

from enum import Enum

class TipoAceituna(Enum):
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"


# ==============================================================================
# ARCHIVO 13/67: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

"""
Entidad Zanahoria.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)

class Zanahoria(Hortaliza):
    """Entidad Zanahoria - solo datos."""

    def __init__(self, es_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby

    def is_baby_carrot(self) -> bool:
        return self._es_baby

    def set_es_baby(self, es_baby: bool) -> None:
        self._es_baby = es_baby



################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 14/67: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/67: apto_medico.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

"""
Entidad AptoMedico.
"""

from datetime import date

class AptoMedico:
    """Certificacion medica de un trabajador."""
    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones


# ==============================================================================
# ARCHIVO 16/67: herramienta.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 17/67: tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

"""
Entidad Tarea.
"""

from datetime import date

class Tarea:
    """Tarea asignada a un trabajador."""
    def __init__(self, id_tarea: int, fecha_programada: date, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._completada = False

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def is_completada(self) -> bool:
        return self._completada

    def marcar_completada(self) -> None:
        self._completada = True


# ==============================================================================
# ARCHIVO 18/67: trabajador.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

"""
Entidad Trabajador.
"""

from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    """Representa un trabajador agricola."""
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico: Optional[AptoMedico] = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas.copy()  # Defensive copy

    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self._apto_medico

    def set_apto_medico(self, apto: AptoMedico) -> None:
        self._apto_medico = apto



################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/67: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/67: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

"""
Entidad Plantacion.
"""

from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """Representa una plantacion agricola."""
    def __init__(self, nombre: str, superficie: float, agua: int):
        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List[Cultivo] = []
        self._trabajadores: List[Trabajador] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_total(self) -> float:
        return self._superficie

    def get_superficie_ocupada(self) -> float:
        return sum(c.get_superficie() for c in self._cultivos)

    def get_superficie_disponible(self) -> float:
        return self.get_superficie_total() - self.get_superficie_ocupada()

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa.")
        self._agua_disponible = agua

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()  # Defensive copy

    def add_cultivo(self, cultivo: Cultivo) -> None:
        self._cultivos.append(cultivo)

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()  # Defensive copy

    def set_trabajadores(self, trabajadores: List[Trabajador]) -> None:
        self._trabajadores = trabajadores


# ==============================================================================
# ARCHIVO 21/67: registro_forestal.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

"""
Entidad RegistroForestal.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Vincula tierra, plantacion, propietario y avaluo."""
    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo


# ==============================================================================
# ARCHIVO 22/67: tierra.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/67: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/67: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

"""
Excepcion para cuando el agua esta agotada.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    USER_AGUA_AGOTADA,
    TECH_AGUA_AGOTADA
)

class AguaAgotadaException(ForestacionException):
    """Lanzada cuando no hay suficiente agua para regar."""
    def __init__(self, agua_requerida: int, agua_disponible: int):
        super().__init__(
            USER_AGUA_AGOTADA,
            f"{TECH_AGUA_AGOTADA} Requerida: {agua_requerida}, Disponible: {agua_disponible}"
        )
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

    def get_agua_requerida(self) -> int:
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        return self._agua_disponible


# ==============================================================================
# ARCHIVO 25/67: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

"""
Excepcion base para el sistema de forestacion.
"""

class ForestacionException(Exception):
    """Clase base para excepciones del sistema."""
    def __init__(self, user_message: str, technical_message: str):
        super().__init__(f"{user_message} ({technical_message})")
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_technical_message(self) -> str:
        return self._technical_message

    def get_full_message(self) -> str:
        return str(self)


# ==============================================================================
# ARCHIVO 26/67: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

"""
Centralizacion de mensajes de error para excepciones.
"""

# Superficie
USER_SUPERFICIE_INSUFICIENTE = "La superficie de la plantacion es insuficiente."
TECH_SUPERFICIE_INSUFICIENTE = "Superficie requerida excede la disponible."

# Agua
USER_AGUA_AGOTADA = "El agua de la plantacion esta agotada."
TECH_AGUA_AGOTADA = "No hay suficiente agua para completar la operacion."

# Persistencia
USER_PERSISTENCIA_ESCRITURA = "Error al guardar el registro."
TECH_PERSISTENCIA_ESCRITURA = "Fallo la operacion de escritura en disco."
USER_PERSISTENCIA_LECTURA = "Error al leer el registro."
TECH_PERSISTENCIA_LECTURA = "Fallo la operacion de lectura de disco."
USER_PERSISTENCIA_NO_ENCONTRADO = "El registro solicitado no existe."
TECH_PERSISTENCIA_NO_ENCONTRADO = "El archivo no fue encontrado en el directorio de datos."


# ==============================================================================
# ARCHIVO 27/67: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

"""
Excepcion para errores de persistencia.
"""

from enum import Enum
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class TipoOperacion(Enum):
    LECTURA = "lectura"
    ESCRITURA = "escritura"

class PersistenciaException(ForestacionException):
    """Lanzada cuando ocurren errores de I/O en persistencia."""
    def __init__(self, user_message: str, technical_message: str, nombre_archivo: str, tipo_operacion: TipoOperacion):
        super().__init__(user_message, f"{technical_message} en archivo: {nombre_archivo}")
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion


# ==============================================================================
# ARCHIVO 28/67: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

"""
Excepcion para cuando la superficie es insuficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    USER_SUPERFICIE_INSUFICIENTE,
    TECH_SUPERFICIE_INSUFICIENTE
)

class SuperficieInsuficienteException(ForestacionException):
    """Lanzada cuando no hay suficiente superficie para plantar."""
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        super().__init__(
            USER_SUPERFICIE_INSUFICIENTE,
            f"{TECH_SUPERFICIE_INSUFICIENTE} Requerida: {superficie_requerida}, Disponible: {superficie_disponible}"
        )
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/67: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 30/67: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/67: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

"""
Factory para la creacion de cultivos.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """Fabrica de cultivos que encapsula la logica de creacion."""
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> Olivo:
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        return Zanahoria(es_baby=False)



################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 32/67: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/67: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\observable.py
# ==============================================================================

"""
Clase Observable generica para el patron Observer.
"""

from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento, self)


# ==============================================================================
# ARCHIVO 34/67: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\observer.py
# ==============================================================================

"""
Interfaz Observer generica para el patron Observer.
"""

from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.patrones.observer.observable import Observable
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para que un objeto sea notificable de cambios."""
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        """
        Recibe una actualizacion de un objeto observable.

        Args:
            evento: El evento que se ha producido.
        """
        pass



################################################################################
# DIRECTORIO: patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/67: __init__.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/67: evento_plantacion.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 37/67: evento_sensor.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ==============================================================================

"""
Evento de sensor para el patron Observer.
"""

from datetime import datetime

class EventoSensor:
    """Representa un evento de un sensor."""
    def __init__(self, valor: float, unidad: str):
        self._valor = valor
        self._unidad = unidad
        self._timestamp = datetime.now()

    def get_valor(self) -> float:
        return self._valor

    def get_unidad(self) -> str:
        return self._unidad

    def get_timestamp(self) -> datetime:
        return self._timestamp



################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/67: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/67: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/67: absorcion_agua_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ==============================================================================

"""
Interfaz para la estrategia de absorcion de agua.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz para definir algoritmos de absorcion de agua."""
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        pass



################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 41/67: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/67: absorcion_constante_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

"""
Estrategia de absorcion de agua constante.
"""

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Absorcion de una cantidad constante de agua."""
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        return self._cantidad


# ==============================================================================
# ARCHIVO 43/67: absorcion_seasonal_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

"""
Estrategia de absorcion de agua estacional.
"""

from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    MES_INICIO_VERANO,
    MES_FIN_VERANO,
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Absorcion diferenciada por estacion (verano/invierno)."""
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/67: __init__.py
# Directorio: riego
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego\control
################################################################################

# ==============================================================================
# ARCHIVO 45/67: __init__.py
# Directorio: riego\control
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/67: control_riego_task.py
# Directorio: riego\control
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/67: __init__.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/67: humedad_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 49/67: temperatura_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/67: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/67: __init__.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/67: arbol_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

"""
Servicio base para arboles.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol

class ArbolService(CultivoService):
    """Servicio abstracto para operaciones de arboles."""
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        super().mostrar_datos(cultivo)
        print(f"Altura: {cultivo.get_altura()} m")


# ==============================================================================
# ARCHIVO 53/67: cultivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

"""
Servicio base para todos los cultivos.
"""

from abc import ABC
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio abstracto para operaciones de cultivo."""
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            date.today(), 0, 0, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")


# ==============================================================================
# ARCHIVO 54/67: cultivo_service_registry.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

"""
Registro de servicios de cultivo (Singleton y Registry).
"""

from threading import Lock
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls() # Llama al constructor
        return cls._instance

    def _inicializar_servicios(self):
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def absorber_agua(self, cultivo: Cultivo) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: Cultivo) -> None:
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo):
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo):
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo):
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo):
        return self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo):
        return self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo):
        return self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo):
        return self._zanahoria_service.mostrar_datos(cultivo)


# ==============================================================================
# ARCHIVO 55/67: lechuga_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

"""
Servicio para Lechuga.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """Servicio para Lechuga."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {cultivo.is_invernadero()}")


# ==============================================================================
# ARCHIVO 56/67: olivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

"""
Servicio para Olivo.
"""

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """Servicio para Olivo."""

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Olivo') -> int:
        agua_absorvida = super().absorver_agua(cultivo)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_OLIVO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        super().mostrar_datos(cultivo)
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna().value}")


# ==============================================================================
# ARCHIVO 57/67: pino_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

"""
Servicio para Pino.
"""

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino

class PinoService(ArbolService):
    """Servicio para Pino."""

    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, cultivo: 'Pino') -> int:
        agua_absorvida = super().absorver_agua(cultivo)
        cultivo.set_altura(cultivo.get_altura() + CRECIMIENTO_PINO)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")


# ==============================================================================
# ARCHIVO 58/67: zanahoria_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

"""
Servicio para Zanahoria.
"""

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """Servicio para Zanahoria."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        super().mostrar_datos(cultivo)
        print(f"Es baby carrot: {cultivo.is_baby_carrot()}")



################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/67: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 60/67: fincas_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 61/67: paquete.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\negocio\paquete.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 62/67: __init__.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/67: trabajador_service.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

"""
Servicio para Trabajador.
"""

from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.entidades.personal.herramienta import Herramienta

class TrabajadorService:
    """Servicio para operaciones de Trabajador."""
    def asignar_apto_medico(
        self,
        trabajador: Trabajador,
        apto: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)

    def trabajar(self, trabajador: Trabajador, fecha: date, util: Herramienta) -> bool:
        apto_medico = trabajador.get_apto_medico()
        if not apto_medico or not apto_medico.esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no puede trabajar. Apto medico no valido.")
            return False

        tareas_del_dia = [t for t in trabajador.get_tareas() if t.get_fecha_programada() == fecha and not t.is_completada()]
        
        # Ordenar por ID descendente
        tareas_del_dia.sort(key=self._obtener_id_tarea, reverse=True)

        for tarea in tareas_del_dia:
            print(f"El trabajador {trabajador.get_nombre()} realizo la tarea {tarea.get_id_tarea()} {tarea.get_descripcion()} con herramienta: {util.get_nombre()}")
            tarea.marcar_completada()
        
        return True

    @staticmethod
    def _obtener_id_tarea(tarea):
        return tarea.get_id_tarea()



################################################################################
# DIRECTORIO: servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/67: __init__.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/67: plantacion_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 66/67: registro_forestal_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 67/67: tierra_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67
# Generado: 2025-10-21 20:39:38
################################################################################
