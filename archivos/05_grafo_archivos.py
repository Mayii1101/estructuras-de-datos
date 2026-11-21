"""
========================================
ARCHIVOS: Grafo guardado en formato DOT y análisis estadístico
========================================
Este archivo muestra cómo:
1. Guardar un Grafo en formato de texto (.dot) — formato estándar
   para representar grafos, compatible con la herramienta Graphviz.
2. Leer el grafo desde el archivo y reconstruirlo.
3. Generar un reporte de análisis estadístico del grafo en .txt.

Formato DOT:
  graph MiGrafo {
      A -- B [label="5"];
      B -- C [label="3"];
  }

También se demuestra cómo guardar la MATRIZ DE ADYACENCIA en CSV.
"""

import os    # Operaciones del sistema de archivos
import csv   # Para guardar la matriz de adyacencia

ARCHIVO_DOT    = "archivos/grafo.dot"
ARCHIVO_MATRIZ = "archivos/matriz_adyacencia.csv"
ARCHIVO_REPORTE= "archivos/reporte_grafo.txt"

# ======= CLASE GRAFO =======
class GrafoArchivo:
    """
    Grafo no dirigido y ponderado con soporte para guardar/cargar archivos.
    """

    def __init__(self, nombre="MiGrafo"):
        self.nombre    = nombre       # Nombre del grafo
        self._aristas  = []           # Lista de (v1, v2, peso)
        self._vertices = set()        # Conjunto de vértices únicos

    def agregar_arista(self, v1, v2, peso=1):
        """Agrega una arista con su peso al grafo."""
        self._aristas.append((v1, v2, peso))
        self._vertices.add(v1)
        self._vertices.add(v2)
        print(f"  [ARISTA] {v1} ↔ {v2} (peso: {peso})")

    def get_vertices(self):
        """Retorna la lista de vértices ordenada."""
        return sorted(self._vertices)

    def get_vecinos(self, vertice):
        """Retorna los vecinos de un vértice con sus pesos."""
        vecinos = []
        for v1, v2, peso in self._aristas:
            if v1 == vertice:
                vecinos.append((v2, peso))
            elif v2 == vertice:
                vecinos.append((v1, peso))
        return vecinos

    def grado(self, vertice):
        """El grado de un vértice es el número de aristas que tiene."""
        return len(self.get_vecinos(vertice))

    # ======= GUARDAR EN FORMATO DOT =======
    def guardar_dot(self, archivo=ARCHIVO_DOT):
        """
        Guarda el grafo en formato DOT para visualización con Graphviz.
        La sintaxis 'graph' es para grafos no dirigidos.
        """
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(f'graph {self.nombre} {{\n')
            f.write(f'    // Generado automáticamente\n')
            f.write(f'    // Vértices: {len(self._vertices)}, Aristas: {len(self._aristas)}\n\n')

            for v1, v2, peso in self._aristas:
                # Formato DOT: v1 -- v2 [label="peso"];
                f.write(f'    {v1} -- {v2} [label="{peso}"];\n')

            f.write('}\n')
        print(f"  [DOT]    Grafo guardado en '{archivo}'.")

    # ======= LEER DESDE DOT =======
    def cargar_dot(self, archivo=ARCHIVO_DOT):
        """
        Lee un archivo .dot y reconstruye el grafo.
        Busca líneas con el patrón: v1 -- v2 [label="peso"];
        """
        import re   # Expresiones regulares para parsear el archivo

        self._aristas  = []
        self._vertices = set()

        patron = re.compile(r'\s*(\w+)\s+--\s+(\w+)\s+\[label="(\d+)"\];')

        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                coincidencia = patron.match(linea)
                if coincidencia:
                    v1   = coincidencia.group(1)
                    v2   = coincidencia.group(2)
                    peso = int(coincidencia.group(3))
                    self._aristas.append((v1, v2, peso))
                    self._vertices.add(v1)
                    self._vertices.add(v2)

        print(f"  [DOT]    Grafo cargado: {len(self._vertices)} vértices, {len(self._aristas)} aristas.")

    # ======= GUARDAR MATRIZ DE ADYACENCIA EN CSV =======
    def guardar_matriz_csv(self, archivo=ARCHIVO_MATRIZ):
        """Guarda la matriz de adyacencia en formato CSV."""
        vertices = self.get_vertices()
        n = len(vertices)

        # Crear matriz n×n inicializada en 0
        matriz = [[0] * n for _ in range(n)]
        indice = {v: i for i, v in enumerate(vertices)}   # Mapa vértice → índice

        # Llenar la matriz con los pesos de las aristas
        for v1, v2, peso in self._aristas:
            i, j = indice[v1], indice[v2]
            matriz[i][j] = peso
            matriz[j][i] = peso   # Simétrica (no dirigido)

        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([''] + vertices)   # Encabezados
            for i, fila in enumerate(matriz):
                writer.writerow([vertices[i]] + fila)

        print(f"  [CSV]    Matriz de adyacencia guardada en '{archivo}'.")

    # ======= GENERAR REPORTE ESTADÍSTICO =======
    def guardar_reporte(self, archivo=ARCHIVO_REPORTE):
        """Genera un reporte de análisis del grafo en archivo de texto."""
        vertices   = self.get_vertices()
        grados     = [(v, self.grado(v)) for v in vertices]
        pesos      = [p for _, _, p in self._aristas]

        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(f"REPORTE DEL GRAFO: {self.nombre}\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Total de vértices : {len(vertices)}\n")
            f.write(f"Total de aristas  : {len(self._aristas)}\n\n")
            f.write("GRADOS DE LOS VÉRTICES:\n")
            f.write("-" * 30 + "\n")
            for v, g in sorted(grados, key=lambda x: -x[1]):
                f.write(f"  {v:<15} grado: {g}\n")
            f.write("\nESTADÍSTICAS DE PESOS:\n")
            f.write("-" * 30 + "\n")
            f.write(f"  Peso mínimo    : {min(pesos)}\n")
            f.write(f"  Peso máximo    : {max(pesos)}\n")
            f.write(f"  Peso promedio  : {sum(pesos)/len(pesos):.2f}\n")
            f.write(f"  Peso total     : {sum(pesos)}\n")

        print(f"  [REPORTE] Reporte guardado en '{archivo}'.")


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("   ARCHIVOS: Grafo en DOT, CSV y Reporte .txt")
print("=" * 55)

os.makedirs("archivos", exist_ok=True)

# Construir el grafo
grafo = GrafoArchivo("Red_Computadoras")

print("\n--- Construyendo red de computadoras ---")
grafo.agregar_arista("PC1", "PC2",    100)
grafo.agregar_arista("PC1", "PC3",     50)
grafo.agregar_arista("PC2", "Switch1", 1000)
grafo.agregar_arista("PC3", "Switch1", 1000)
grafo.agregar_arista("Switch1", "Router", 500)
grafo.agregar_arista("Router", "Internet", 100)
grafo.agregar_arista("PC4", "Switch1", 1000)

# Guardar en todos los formatos
print("\n--- Guardando archivos ---")
grafo.guardar_dot()
grafo.guardar_matriz_csv()
grafo.guardar_reporte()

# Cargar desde DOT y verificar
print("\n--- Cargar grafo desde archivo DOT ---")
grafo2 = GrafoArchivo("Restaurado")
grafo2.cargar_dot()

print(f"\nGrafo restaurado:")
print(f"  Vértices: {grafo2.get_vertices()}")
for v in grafo2.get_vertices():
    print(f"  Vecinos de '{v}': {grafo2.get_vecinos(v)}")

# Mostrar el reporte
print(f"\n--- Contenido del reporte ---")
with open(ARCHIVO_REPORTE, 'r', encoding='utf-8') as f:
    print(f.read())

