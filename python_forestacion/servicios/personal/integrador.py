"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\personal
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\servicios\personal\trabajador_service.py
# ================================================================================

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


