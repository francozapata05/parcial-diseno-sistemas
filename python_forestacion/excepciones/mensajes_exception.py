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
