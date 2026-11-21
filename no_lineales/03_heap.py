"""
========================================
ESTRUCTURA NO LINEAL: MONTÍCULO (Heap)
========================================
Un Montículo (Heap) es un árbol binario especial que cumple la
"Propiedad de Montículo":

  - Min-Heap: el padre SIEMPRE es MENOR que sus hijos
              → la raíz es el elemento mínimo
  - Max-Heap: el padre SIEMPRE es MAYOR que sus hijos
              → la raíz es el elemento máximo

Los heaps se usan en:
  - Colas de prioridad (priority queues)
  - Algoritmo Heapsort
  - Algoritmos de grafos (Dijkstra, Prim)

Python incluye el módulo 'heapq' que implementa un Min-Heap.
"""

import heapq   # Módulo estándar de Python para heaps

# ======= MIN-HEAP con heapq =======
print("=" * 50)
print("       MIN-HEAP (usando módulo heapq)")
print("=" * 50)

min_heap = []   # En Python, el heap se representa como una lista

# heappush inserta un elemento manteniendo la propiedad de heap
print("\n--- Insertando elementos ---")
elementos = [15, 3, 10, 1, 7, 20, 5]
for e in elementos:
    heapq.heappush(min_heap, e)
    print(f"  heappush({e}) → Heap: {min_heap}")

# La raíz siempre es el mínimo en un Min-Heap
print(f"\nEl mínimo siempre está en [0]: {min_heap[0]}")

# heappop extrae y retorna el elemento mínimo (la raíz)
print("\n--- Extrayendo elementos (siempre el mínimo) ---")
while min_heap:
    minimo = heapq.heappop(min_heap)   # Extrae la raíz (mínimo)
    print(f"  heappop() → {minimo}  |  Heap restante: {min_heap}")


# ======= MAX-HEAP (truco: negar los valores) =======
print("\n" + "=" * 50)
print("       MAX-HEAP (valores negados)")
print("=" * 50)
print("Truco: Python solo tiene Min-Heap, pero si negamos")
print("los valores, el 'mínimo negado' = el máximo original.\n")

max_heap = []

print("--- Insertando elementos (negados internamente) ---")
for e in elementos:
    heapq.heappush(max_heap, -e)   # Insertar negado
    print(f"  heappush({e}) → guardado como {-e} | Heap: {max_heap}")

print(f"\nEl máximo (valor original) está en [0]: {-max_heap[0]}")

print("\n--- Extrayendo máximos ---")
while max_heap:
    maximo = -heapq.heappop(max_heap)   # Negar al extraer para recuperar el original
    print(f"  heappop() → {maximo}  |  Max-Heap restante: {[-x for x in max_heap]}")


# ======= COLA DE PRIORIDAD con heap =======
print("\n" + "=" * 50)
print("   APLICACIÓN: Cola de Prioridad (Priority Queue)")
print("=" * 50)
print("Cada tarea tiene un número de prioridad.")
print("La de MENOR número es la más urgente.\n")

cola_prioridad = []

# Cada elemento es una tupla (prioridad, nombre_tarea)
# heapq compara primero por prioridad
tareas = [
    (3, "Revisar correos"),
    (1, "Atender emergencia"),
    (5, "Reunión de equipo"),
    (2, "Responder ticket urgente"),
    (4, "Actualizar documentación"),
]

print("--- Agregando tareas ---")
for prioridad, tarea in tareas:
    heapq.heappush(cola_prioridad, (prioridad, tarea))
    print(f"  Tarea '{tarea}' con prioridad {prioridad} añadida.")

print("\n--- Ejecutando tareas (de mayor a menor prioridad) ---")
while cola_prioridad:
    prioridad, tarea = heapq.heappop(cola_prioridad)
    print(f"  [P{prioridad}] Ejecutando: '{tarea}'")

