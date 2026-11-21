"""
========================================
ARCHIVOS: Guardar y Leer un Diccionario/Tabla Hash en JSON
========================================
JSON (JavaScript Object Notation) es el formato más usado para
guardar y transmitir datos estructurados (pares clave-valor).

Python incluye el módulo 'json' que convierte entre:
  - Diccionarios Python  ↔  Archivos .json
  - Listas Python        ↔  Arrays JSON

Ventajas del JSON:
  - Legible por humanos
  - Compatible con prácticamente todos los lenguajes
  - Soporta tipos: string, número, booleano, lista, objeto, null
"""

import json   # Módulo estándar para trabajar con JSON
import os     # Para operaciones del sistema de archivos

ARCHIVO_JSON = "archivos/estudiantes.json"

# ======= FUNCIÓN: Guardar diccionario en JSON =======
def guardar_json(datos, archivo=ARCHIVO_JSON):
    """
    Serializa un diccionario/lista de Python a un archivo JSON.
    indent=4 formatea el archivo para que sea legible.
    ensure_ascii=False permite caracteres especiales (tildes, ñ).
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"  [GUARDADO] Datos escritos en '{archivo}' (JSON).")


# ======= FUNCIÓN: Leer JSON y convertir a Python =======
def leer_json(archivo=ARCHIVO_JSON):
    """
    Deserializa un archivo JSON a un diccionario/lista de Python.
    """
    if not os.path.exists(archivo):
        print(f"  [ERROR] El archivo '{archivo}' no existe.")
        return {}

    with open(archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)   # Convierte JSON → Python dict/list

    print(f"  [LEÍDO]   '{archivo}' cargado correctamente.")
    return datos


# ======= FUNCIÓN: Agregar o actualizar un estudiante =======
def actualizar_estudiante(codigo, nombre, notas, archivo=ARCHIVO_JSON):
    """Carga el archivo, agrega/actualiza un estudiante y guarda."""
    base_datos = leer_json(archivo) if os.path.exists(archivo) else {}

    # Calcular promedio de notas
    promedio = sum(notas) / len(notas) if notas else 0

    base_datos[codigo] = {
        "nombre"  : nombre,
        "notas"   : notas,
        "promedio": round(promedio, 2),
        "estado"  : "APROBADO" if promedio >= 3.0 else "REPROBADO"
    }

    guardar_json(base_datos, archivo)
    print(f"  [UPDATE]  Estudiante '{nombre}' ({codigo}) actualizado.")


# ======= FUNCIÓN: Eliminar estudiante =======
def eliminar_estudiante(codigo, archivo=ARCHIVO_JSON):
    """Elimina un estudiante del JSON por su código."""
    base_datos = leer_json(archivo)
    if codigo in base_datos:
        nombre = base_datos[codigo]["nombre"]
        del base_datos[codigo]
        guardar_json(base_datos, archivo)
        print(f"  [DELETE]  '{nombre}' ({codigo}) eliminado.")
    else:
        print(f"  [ERROR]   Código '{codigo}' no encontrado.")


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("    ARCHIVOS: Base de Datos en JSON")
print("=" * 55)

os.makedirs("archivos", exist_ok=True)

print("\n--- Registrando estudiantes ---")
actualizar_estudiante("E001", "Ana García",   [4.5, 3.8, 4.2, 3.9])
actualizar_estudiante("E002", "Carlos López", [2.8, 3.1, 2.5, 2.9])
actualizar_estudiante("E003", "María Torres", [4.8, 4.9, 5.0, 4.7])
actualizar_estudiante("E004", "Juan Pérez",   [1.5, 2.0, 1.8, 2.2])
actualizar_estudiante("E005", "Sofía Ruiz",   [3.5, 4.0, 3.8, 3.7])

print("\n--- Leyendo la base de datos ---")
db = leer_json()

print("\n📋 REPORTE DE ESTUDIANTES:")
print(f"{'─'*60}")
print(f"{'Código':<8} {'Nombre':<20} {'Promedio':<10} {'Estado'}")
print(f"{'─'*60}")
for codigo, info in db.items():
    estado_icono = "✓" if info['estado'] == 'APROBADO' else "✗"
    print(f"{codigo:<8} {info['nombre']:<20} {info['promedio']:<10} {estado_icono} {info['estado']}")
print(f"{'─'*60}")

# Estadísticas
promedios = [info['promedio'] for info in db.values()]
print(f"\nEstadísticas del grupo:")
print(f"  Promedio del grupo : {sum(promedios)/len(promedios):.2f}")
print(f"  Nota más alta      : {max(promedios)}")
print(f"  Nota más baja      : {min(promedios)}")
aprobados = sum(1 for info in db.values() if info['estado'] == 'APROBADO')
print(f"  Aprobados          : {aprobados}/{len(db)}")

print("\n--- Eliminar un estudiante ---")
eliminar_estudiante("E004")

print("\n--- Ver el JSON guardado ---")
print(f"Contenido de '{ARCHIVO_JSON}':")
with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
    print(f.read())

