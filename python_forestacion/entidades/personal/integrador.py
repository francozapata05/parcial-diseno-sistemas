"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal
Fecha: 2025-10-21 20:39:38
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\apto_medico.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\herramienta.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\tarea.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: C:\Users\Franco\Desktop\DS1\Python\parcial-diseno-sistemas\python_forestacion\entidades\personal\trabajador.py
# ================================================================================

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


