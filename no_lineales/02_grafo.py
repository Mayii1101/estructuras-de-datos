"""
========================================
ESTRUCTURA NO LINEAL: GRAFO (Graph)
========================================
Un Grafo es una estructura formada por:
  - VÉRTICES (nodos): los elementos del grafo
  - ARISTAS (edges) : las conexiones entre vértices

Tipos de grafos:
  - Dirigido   : las aristas tienen dirección (A → B)
  - No dirigido: las aristas son bidireccionales (A ↔ B)
  - Ponderado  : las aristas tienen un peso/costo
  - Cíclico    : existe al menos un ciclo
  - Acíclico   : no tiene ciclos

Representaciones comunes:
  - Lista de adyacencia  : diccionario {nodo: [vecinos]}
  - Matriz de adyacencia : tabla n×n de True/False

Este ejemplo implementa un Grafo No Dirigido con lista de adyacencia.
"""

from collections import deque   # Para el recorrido BFS

class Grafo:
    """
    Grafo No Dirigido implementado con lista de adyacencia.
    Perfecto para representar redes, mapas, relaciones sociales.
    """

    def __init__(self):
        # Diccionario: cada clave es un vértice, su valor es una lista de vecinos
        self._adyacencia = {}

    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo (si no existe ya)."""
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = []   # Lista de vecinos vacía
            print(f"  [VÉRTICE] '{vertice}' agregado al grafo.")
        else:
            print(f"  [INFO] '{vertice}' ya existe.")

    def agregar_arista(self, v1, v2):
        """
        Conecta dos vértices con una arista.
        Como el grafo no es dirigido, se agrega en ambas direcciones.
        """
        # Asegurarse de que ambos vértices existen
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)

        # Agregar la conexión bidireccional
        if v2 not in self._adyacencia[v1]:
            self._adyacencia[v1].append(v2)   # v1 conoce a v2
        if v1 not in self._adyacencia[v2]:
            self._adyacencia[v2].append(v1)   # v2 conoce a v1

        print(f"  [ARISTA]  '{v1}' ↔ '{v2}' conectados.")

    def vecinos(self, vertice):
        """Retorna la lista de vértices conectados a uno dado."""
        return self._adyacencia.get(vertice, [])

    def bfs(self, inicio):
        """
        BFS - Breadth First Search (Búsqueda en Anchura).
        Recorre el grafo por niveles: primero los vecinos más cercanos.
        Usa una Cola para procesar nodos en orden de llegada.
        """
        visitados = set()       # Conjunto de nodos ya visitados
        cola = deque([inicio])  # Cola inicializada con el nodo de inicio
        orden_visita = []

        visitados.add(inicio)

        while cola:
            vertice = cola.popleft()   # Tomar el primero de la cola
            orden_visita.append(vertice)

            # Visitar cada vecino que no haya sido visitado aún
            for vecino in self._adyacencia[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)   # Agregar a la cola para visitar después

        return orden_visita

    def dfs(self, inicio):
        """
        DFS - Depth First Search (Búsqueda en Profundidad).
        Recorre el grafo profundizando por cada rama antes de retroceder.
        Usa una Pila (stack) para ir profundizando.
        """
        visitados = set()
        pila = [inicio]       # Pila inicializada con el nodo de inicio
        orden_visita = []

        while pila:
            vertice = pila.pop()   # Tomar el último de la pila (LIFO)
            if vertice not in visitados:
                visitados.add(vertice)
                orden_visita.append(vertice)
                # Agregar vecinos no visitados a la pila
                for vecino in reversed(self._adyacencia[vertice]):
                    if vecino not in visitados:
                        pila.append(vecino)

        return orden_visita

    def hay_camino(self, origen, destino):
        """Verifica si existe un camino entre dos vértices usando BFS."""
        return destino in self.bfs(origen)

    def __str__(self):
        """Muestra la lista de adyacencia completa."""
        lineas = ["Lista de Adyacencia:"]
        for vertice, vecinos in self._adyacencia.items():
            lineas.append(f"  {vertice} → {vecinos}")
        return "\n".join(lineas)


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("          DEMOSTRACIÓN DE GRAFO")
print("=" * 55)

# Simulamos una red de ciudades conectadas por carreteras
grafo = Grafo()

print("\n--- Construyendo mapa de ciudades ---")
grafo.agregar_arista("Bogotá", "Medellín")
grafo.agregar_arista("Bogotá", "Cali")
grafo.agregar_arista("Bogotá", "Bucaramanga")
grafo.agregar_arista("Medellín", "Pereira")
grafo.agregar_arista("Cali", "Pereira")
grafo.agregar_arista("Pereira", "Manizales")
grafo.agregar_arista("Bucaramanga", "Cúcuta")

print("\n" + str(grafo))

print(f"\nVecinos de 'Bogotá': {grafo.vecinos('Bogotá')}")
print(f"Vecinos de 'Pereira': {grafo.vecinos('Pereira')}")

print(f"\nRecorrido BFS desde 'Bogotá': {grafo.bfs('Bogotá')}")
print(f"Recorrido DFS desde 'Bogotá': {grafo.dfs('Bogotá')}")

print("\n--- Verificar caminos ---")
pares = [("Bogotá", "Manizales"), ("Bogotá", "Cúcuta"), ("Manizales", "Cúcuta")]
for origen, destino in pares:
    existe = grafo.hay_camino(origen, destino)
    print(f"  {'✓' if existe else '✗'} ¿Hay camino de {origen} a {destino}? {'Sí' if existe else 'No'}")

