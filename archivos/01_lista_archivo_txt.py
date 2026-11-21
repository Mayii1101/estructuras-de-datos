"""
========================================
ARCHIVOS: Guardar y Leer una Lista en Archivo de Texto
========================================
Demostración de cómo persistir (guardar) una estructura de datos
(Lista) en un archivo .txt y cómo leerla de vuelta.

Operaciones:
  - Escribir la lista en un archivo (una línea por elemento)
  - Leer el archivo y reconstruir la lista
  - Agregar elementos al archivo sin borrar los existentes (modo 'a')
"""

import os    # Para verificar si el archivo existe

# Ruta del archivo que vamos a usar para guardar datos
ARCHIVO_LISTA = "archivos/lista_guardada.txt"

# ======= FUNCIÓN: Guardar lista en archivo =======
def guardar_lista(lista, archivo=ARCHIVO_LISTA):
    """
    Escribe cada elemento de la lista como una línea en el archivo.
    Modo 'w' (write): crea el archivo o lo sobreescribe si ya existe.
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        for elemento in lista:
            f.write(str(elemento) + '\n')   # Cada elemento en una nueva línea
    print(f"  [GUARDADO] {len(lista)} elementos escritos en '{archivo}'.")


# ======= FUNCIÓN: Leer lista desde archivo =======
def leer_lista(archivo=ARCHIVO_LISTA):
    """
    Lee el archivo línea por línea y reconstruye la lista.
    Modo 'r' (read): solo lectura, el archivo debe existir.
    """
    if not os.path.exists(archivo):
        print(f"  [ERROR] El archivo '{archivo}' no existe.")
        return []

    lista = []
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            elemento = linea.strip()   # strip() elimina el '\n' al final
            if elemento:               # Ignorar líneas vacías
                lista.append(elemento)

    print(f"  [LEÍDO]   {len(lista)} elementos cargados desde '{archivo}'.")
    return lista


# ======= FUNCIÓN: Agregar elemento al final del archivo =======
def agregar_a_lista(elemento, archivo=ARCHIVO_LISTA):
    """
    Agrega un elemento al final del archivo SIN borrar el contenido.
    Modo 'a' (append): abre para agregar al final.
    """
    with open(archivo, 'a', encoding='utf-8') as f:
        f.write(str(elemento) + '\n')
    print(f"  [APPEND]  '{elemento}' agregado al archivo.")


# ======= FUNCIÓN: Buscar en el archivo =======
def buscar_en_archivo(valor, archivo=ARCHIVO_LISTA):
    """Busca si un valor existe dentro del archivo."""
    lista = leer_lista(archivo)
    return valor in lista


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("   ARCHIVOS: Lista persistida en archivo .txt")
print("=" * 55)

# Crear la carpeta archivos si no existe
os.makedirs("archivos", exist_ok=True)

# Datos iniciales
frutas = ["Manzana", "Pera", "Uva", "Mango", "Banano"]

print("\n--- Guardando lista en archivo ---")
guardar_lista(frutas)

print("\n--- Leyendo lista desde archivo ---")
lista_recuperada = leer_lista()
print("Lista recuperada:", lista_recuperada)

print("\n--- Agregando nuevos elementos ---")
agregar_a_lista("Fresa")
agregar_a_lista("Melón")

print("\n--- Lista actualizada (después de agregar) ---")
lista_actualizada = leer_lista()
print("Lista completa:", lista_actualizada)

print("\n--- Buscar elementos ---")
for fruta in ["Uva", "Papaya", "Fresa"]:
    existe = buscar_en_archivo(fruta)
    icono = "✓" if existe else "✗"
    print(f"  {icono} '{fruta}': {'Encontrada' if existe else 'No encontrada'}")

print("\n--- Ver contenido del archivo (línea por línea) ---")
print(f"Contenido de '{ARCHIVO_LISTA}':")
with open(ARCHIVO_LISTA, 'r', encoding='utf-8') as f:
    for num, linea in enumerate(f, 1):
        print(f"  Línea {num}: {linea}", end='')

