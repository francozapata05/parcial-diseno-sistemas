"""
Ejemplo de uso del sistema de gestion forestal.
"""

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
