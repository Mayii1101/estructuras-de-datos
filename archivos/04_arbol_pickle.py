"""
========================================
ARCHIVOS: Serialización de Árbol con Pickle
========================================
Pickle es un módulo de Python para SERIALIZAR objetos:
convertir cualquier objeto Python (incluidas estructuras
de datos complejas como árboles) en bytes para guardarlo
en archivo y recuperarlo exactamente igual después.

Ventaja  : guarda el objeto completo, listo para usar
Desventaja: solo legible por Python (no es texto plano)

USO TÍPICO: guardar el estado de un programa entre sesiones.

⚠️ ADVERTENCIA: nunca cargar archivos pickle de fuentes
   no confiables (pueden contener código malicioso).
"""

import pickle   # Módulo de serialización de Python
import os       # Para operaciones del sistema de archivos

ARCHIVO_ARBOL = "archivos/arbol_guardado.pkl"

# ======= Clase del Árbol Binario de Búsqueda =======
# (Versión simplificada del archivo no_lineales/01_arbol_binario.py)

class Nodo:
    """Nodo del árbol binario."""
    def __init__(self, valor):
        self.valor     = valor
        self.izquierdo = None
        self.derecho   = None


class ArbolBST:
    """Árbol Binario de Búsqueda serializable con Pickle."""

    def __init__(self):
        self.raiz = None
        self.total_nodos = 0   # Contador de nodos insertados

    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        self.raiz = self._insertar(self.raiz, valor)
        self.total_nodos += 1

    def _insertar(self, nodo, valor):
        """Recursivamente inserta en la posición correcta."""
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho   = self._insertar(nodo.derecho, valor)
        return nodo

    def inorden(self):
        """Recorrido que devuelve los valores ordenados."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecho, resultado)

    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierdo, valor)
        else:
            return self._buscar(nodo.derecho, valor)

    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))


# ======= FUNCIONES DE PICKLE =======

def guardar_arbol(arbol, archivo=ARCHIVO_ARBOL):
    """
    Serializa el árbol completo en un archivo .pkl.
    Modo 'wb' = write binary (escritura en binario).
    """
    with open(archivo, 'wb') as f:
        pickle.dump(arbol, f)   # dump() serializa y escribe
    tamaño = os.path.getsize(archivo)
    print(f"  [GUARDADO] Árbol serializado en '{archivo}' ({tamaño} bytes).")


def cargar_arbol(archivo=ARCHIVO_ARBOL):
    """
    Deserializa el árbol desde el archivo .pkl.
    Modo 'rb' = read binary (lectura en binario).
    """
    if not os.path.exists(archivo):
        print(f"  [ERROR] El archivo '{archivo}' no existe.")
        return None
    with open(archivo, 'rb') as f:
        arbol = pickle.load(f)   # load() lee y deserializa
    print(f"  [CARGADO]  Árbol recuperado desde '{archivo}'.")
    return arbol


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("   ARCHIVOS: Árbol Binario guardado con Pickle")
print("=" * 55)

os.makedirs("archivos", exist_ok=True)

# --- Crear y poblar el árbol ---
print("\n--- Construyendo árbol original ---")
arbol_original = ArbolBST()
valores = [50, 30, 70, 20, 40, 60, 80, 15, 25, 45, 55]
for v in valores:
    arbol_original.insertar(v)
    print(f"  Insertado: {v}")

print(f"\nÁrbol original:")
print(f"  Nodos en inorden (ordenado) : {arbol_original.inorden()}")
print(f"  Total nodos                 : {arbol_original.total_nodos}")
print(f"  Altura                      : {arbol_original.altura()}")

# --- Guardar con Pickle ---
print("\n--- Serializar y guardar ---")
guardar_arbol(arbol_original)

# Simulamos "cerrar el programa" eliminando el objeto de memoria
del arbol_original
print("  Objeto en memoria eliminado (simulando cierre de programa).")

# --- Cargar con Pickle ---
print("\n--- Deserializar y recuperar ---")
arbol_recuperado = cargar_arbol()

if arbol_recuperado:
    print(f"\nÁrbol recuperado (verificación):")
    print(f"  Nodos en inorden : {arbol_recuperado.inorden()}")
    print(f"  Total nodos      : {arbol_recuperado.total_nodos}")
    print(f"  Altura           : {arbol_recuperado.altura()}")

    print("\n--- Buscar en el árbol recuperado ---")
    for val in [40, 55, 99]:
        encontrado = arbol_recuperado.buscar(val)
        print(f"  {'✓' if encontrado else '✗'} Buscar {val}: {'Encontrado' if encontrado else 'No existe'}")

    # El árbol recuperado funciona exactamente igual que el original
    print("\n--- Insertar nuevos valores al árbol recuperado ---")
    arbol_recuperado.insertar(35)
    arbol_recuperado.insertar(65)
    print(f"  Inorden actualizado: {arbol_recuperado.inorden()}")

    # Guardar la versión actualizada
    guardar_arbol(arbol_recuperado)

