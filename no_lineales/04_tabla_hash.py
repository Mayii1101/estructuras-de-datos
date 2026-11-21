"""
========================================
ESTRUCTURA NO LINEAL: TABLA HASH (Hash Table / Diccionario)
========================================
Una Tabla Hash (o HashMap) almacena pares CLAVE → VALOR.
Usa una función HASH para calcular el índice donde guardar cada valor,
lo que permite búsquedas, inserciones y eliminaciones en O(1) promedio.

Conceptos clave:
  - Función hash : transforma la clave en un índice
  - Colisión     : cuando dos claves generan el mismo índice
  - Encadenamiento: resolver colisiones con listas en cada celda

Python incluye el tipo 'dict' que ES una tabla hash internamente.
Aquí se muestra primero la implementación manual, luego el uso de dict.
"""

# ======= IMPLEMENTACIÓN MANUAL DE TABLA HASH =======
class TablaHash:
    """
    Tabla Hash manual con encadenamiento para resolver colisiones.
    Usa listas (cadenas) en cada celda para manejar múltiples
    claves que producen el mismo índice.
    """

    def __init__(self, capacidad=10):
        self.capacidad = capacidad    # Número de "cubetas" (buckets)
        # Crear la tabla: lista de listas vacías
        self.tabla = [[] for _ in range(capacidad)]
        self.tamaño = 0               # Contador de elementos

    def _hash(self, clave):
        """
        Función hash: convierte la clave en un índice válido.
        hash() de Python + módulo para que el índice quepa en la tabla.
        """
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        """Inserta o actualiza un par clave-valor en la tabla."""
        indice = self._hash(clave)   # Calcular posición en la tabla
        cubeta = self.tabla[indice]  # Obtener la lista en esa posición

        # Buscar si la clave ya existe en la cubeta (actualizar)
        for i, (k, v) in enumerate(cubeta):
            if k == clave:
                cubeta[i] = (clave, valor)   # Actualizar valor existente
                print(f"  [UPDATE] '{clave}' actualizado → '{valor}'")
                return

        # Si no existe, agregar el nuevo par
        cubeta.append((clave, valor))
        self.tamaño += 1
        print(f"  [INSERT] '{clave}': '{valor}' en índice {indice}")

    def obtener(self, clave):
        """Busca y retorna el valor asociado a la clave."""
        indice = self._hash(clave)
        cubeta = self.tabla[indice]

        for k, v in cubeta:
            if k == clave:
                return v   # ¡Encontrado!

        return None   # No existe esa clave

    def eliminar(self, clave):
        """Elimina el par clave-valor de la tabla."""
        indice = self._hash(clave)
        cubeta = self.tabla[indice]

        for i, (k, v) in enumerate(cubeta):
            if k == clave:
                del cubeta[i]    # Eliminar de la lista
                self.tamaño -= 1
                print(f"  [DELETE] '{clave}' eliminado.")
                return

        print(f"  [ERROR] Clave '{clave}' no encontrada.")

    def __str__(self):
        """Muestra la tabla hash con sus cubetas."""
        lineas = ["Tabla Hash:"]
        for i, cubeta in enumerate(self.tabla):
            if cubeta:   # Solo mostrar celdas no vacías
                lineas.append(f"  [{i:2d}] → {cubeta}")
        return "\n".join(lineas)


# ======= DEMOSTRACIÓN TABLA HASH MANUAL =======
print("=" * 55)
print("     DEMOSTRACIÓN DE TABLA HASH (Manual)")
print("=" * 55)

th = TablaHash(capacidad=7)

print("\n--- Insertando estudiantes ---")
th.insertar("E001", "Ana García")
th.insertar("E002", "Carlos López")
th.insertar("E003", "María Torres")
th.insertar("E004", "Juan Pérez")
th.insertar("E002", "Carlos López Actualizado")  # Actualizar clave existente

print("\n" + str(th))

print("\n--- Búsquedas ---")
for clave in ["E001", "E003", "E999"]:
    resultado = th.obtener(clave)
    print(f"  Buscar '{clave}': {resultado if resultado else 'No encontrado'}")

print("\n--- Eliminar ---")
th.eliminar("E002")
th.eliminar("E999")

print(f"\nElementos restantes: {th.tamaño}")


# ======= DICCIONARIO DE PYTHON (dict interno = tabla hash) =======
print("\n" + "=" * 55)
print("   DICCIONARIO de Python (Tabla Hash nativa)")
print("=" * 55)

# El dict de Python es altamente optimizado internamente
inventario = {}

print("\n--- Gestión de inventario ---")
inventario["Manzanas"] = 50
inventario["Peras"]    = 30
inventario["Uvas"]     = 75
inventario["Mangos"]   = 20

print("Inventario inicial:", inventario)

# Acceso directo O(1)
print(f"\nManzanas disponibles: {inventario['Manzanas']}")

# Actualizar valor
inventario["Manzanas"] += 10
print(f"Manzanas después de restock: {inventario['Manzanas']}")

# Recorrer el diccionario
print("\nInventario completo:")
for producto, cantidad in inventario.items():
    print(f"  {producto:<12} → {cantidad} unidades")

# Verificar existencia de clave
print(f"\n¿Hay 'Peras'? {'Sí' if 'Peras' in inventario else 'No'}")
print(f"¿Hay 'Kiwis'? {'Sí' if 'Kiwis' in inventario else 'No'}")

