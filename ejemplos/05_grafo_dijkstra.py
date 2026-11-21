"""
========================================
EJEMPLO: Grafo para Encontrar el Camino Más Corto
========================================
Implementamos el Algoritmo de Dijkstra para encontrar
la ruta más corta entre ciudades en un mapa de carreteras.

El algoritmo de Dijkstra:
  1. Asigna distancia = 0 al nodo inicial, infinito a los demás
  2. Usa una Cola de Prioridad (Min-Heap) para explorar siempre
     el nodo más cercano sin visitar
  3. Actualiza distancias si encuentra una ruta más corta
  4. Termina cuando llega al destino o cuando explora todo el grafo

Complejidad: O((V + E) log V) donde V=vértices, E=aristas
"""

import heapq   # Para la cola de prioridad

class GrafoPonderado:
    """
    Grafo Dirigido y Ponderado (con costos en las aristas).
    Usado para representar redes de transporte con distancias.
    """

    def __init__(self):
        # Diccionario de listas de adyacencia con pesos:
        # { nodo: [(vecino, costo), ...] }
        self._grafo = {}

    def agregar_ciudad(self, ciudad):
        """Agrega una ciudad (vértice) al grafo."""
        if ciudad not in self._grafo:
            self._grafo[ciudad] = []

    def agregar_ruta(self, origen, destino, distancia_km):
        """
        Agrega una ruta (arista) entre dos ciudades con su distancia.
        Bidireccional (se puede ir y volver por la misma ruta).
        """
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)
        # Agregar en ambas direcciones (grafo no dirigido)
        self._grafo[origen].append((destino, distancia_km))
        self._grafo[destino].append((origen, distancia_km))
        print(f"  [RUTA] {origen} ↔ {destino}: {distancia_km} km")

    def dijkstra(self, inicio, fin):
        """
        Implementación del Algoritmo de Dijkstra.
        Retorna la distancia mínima y el camino para llegar de inicio a fin.
        """
        # Inicializar todas las distancias como infinito
        distancias = {ciudad: float('inf') for ciudad in self._grafo}
        distancias[inicio] = 0   # La distancia al inicio es 0

        # Diccionario para reconstruir el camino
        anteriores = {ciudad: None for ciudad in self._grafo}

        # Cola de prioridad: (distancia_acumulada, ciudad)
        cola_prioridad = [(0, inicio)]

        # Conjunto de ciudades ya procesadas
        visitados = set()

        print(f"\n--- Ejecutando Dijkstra: {inicio} → {fin} ---")

        while cola_prioridad:
            # Extraer la ciudad con menor distancia acumulada
            dist_actual, ciudad_actual = heapq.heappop(cola_prioridad)

            if ciudad_actual in visitados:
                continue   # Ya fue procesada, saltarla

            visitados.add(ciudad_actual)
            print(f"  Visitando '{ciudad_actual}' (distancia: {dist_actual} km)")

            # Si llegamos al destino, ya tenemos la ruta más corta
            if ciudad_actual == fin:
                break

            # Explorar los vecinos (rutas que salen de esta ciudad)
            for vecino, peso in self._grafo.get(ciudad_actual, []):
                if vecino not in visitados:
                    # Calcular la nueva distancia pasando por ciudad_actual
                    nueva_distancia = dist_actual + peso

                    if nueva_distancia < distancias[vecino]:
                        # Encontramos una ruta más corta al vecino
                        distancias[vecino] = nueva_distancia
                        anteriores[vecino] = ciudad_actual   # Guardar de dónde venimos
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                        print(f"    → Actualizar '{vecino}': {nueva_distancia} km (vía {ciudad_actual})")

        # Reconstruir el camino más corto
        camino = []
        ciudad = fin
        while ciudad is not None:
            camino.insert(0, ciudad)   # Insertar al inicio para orden correcto
            ciudad = anteriores[ciudad]

        return distancias[fin], camino

    def mostrar_grafo(self):
        """Muestra todas las rutas del grafo."""
        print("\nMapa de rutas:")
        for ciudad, rutas in self._grafo.items():
            for destino, km in rutas:
                if ciudad < destino:   # Evitar mostrar duplicados (bidireccional)
                    print(f"  {ciudad} ↔ {destino}: {km} km")


# ======= DEMOSTRACIÓN =======
print("=" * 60)
print("  EJEMPLO: Ruta más Corta con Algoritmo de Dijkstra")
print("=" * 60)

mapa = GrafoPonderado()

print("\n--- Construyendo mapa de Colombia ---")
mapa.agregar_ruta("Bogotá",     "Medellín",     415)
mapa.agregar_ruta("Bogotá",     "Cali",         470)
mapa.agregar_ruta("Bogotá",     "Bucaramanga",  390)
mapa.agregar_ruta("Medellín",   "Pereira",      190)
mapa.agregar_ruta("Cali",       "Pereira",      210)
mapa.agregar_ruta("Pereira",    "Manizales",     55)
mapa.agregar_ruta("Bucaramanga","Cúcuta",       195)
mapa.agregar_ruta("Medellín",   "Cartagena",    630)
mapa.agregar_ruta("Bogotá",     "Villavicencio",  86)

mapa.mostrar_grafo()

# Buscar caminos más cortos
consultas = [
    ("Bogotá",     "Manizales"),
    ("Bogotá",     "Cúcuta"),
    ("Cartagena",  "Manizales"),
]

print("\n" + "=" * 60)
for origen, destino in consultas:
    distancia, camino = mapa.dijkstra(origen, destino)
    ruta_str = " → ".join(camino)
    print(f"\n✓ Ruta más corta: {origen} → {destino}")
    print(f"  Camino  : {ruta_str}")
    print(f"  Distancia: {distancia} km")
    print("-" * 60)

