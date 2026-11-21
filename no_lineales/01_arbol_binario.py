"""
========================================
ESTRUCTURA NO LINEAL: ÁRBOL BINARIO (Binary Tree)
========================================
Un Árbol Binario es una estructura jerárquica donde cada nodo
puede tener como máximo DOS hijos: izquierdo y derecho.

Terminología:
  - Raíz (root)   : nodo principal, el primero
  - Hoja (leaf)   : nodo sin hijos
  - Altura        : niveles desde la raíz hasta la hoja más profunda
  - Subárbol      : árbol formado por un nodo y sus descendientes

Recorridos clásicos:
  - Inorden   (In-order)   : izquierdo → raíz → derecho   (da valores ordenados en BST)
  - Preorden  (Pre-order)  : raíz → izquierdo → derecho
  - Postorden (Post-order) : izquierdo → derecho → raíz
"""

class NodoArbol:
    """Representa un nodo del árbol binario."""

    def __init__(self, valor):
        self.valor = valor          # Dato almacenado en el nodo
        self.izquierdo = None       # Hijo izquierdo
        self.derecho = None         # Hijo derecho


class ArbolBinarioBusqueda:
    """
    Árbol Binario de Búsqueda (BST - Binary Search Tree).
    Propiedad: valor_izq < nodo < valor_der
    Esto permite búsquedas muy eficientes: O(log n) en promedio.
    """

    def __init__(self):
        self.raiz = None   # El árbol comienza vacío

    def insertar(self, valor):
        """Inserta un valor manteniendo la propiedad BST."""
        if self.raiz is None:
            # Si el árbol está vacío, el nuevo nodo es la raíz
            self.raiz = NodoArbol(valor)
        else:
            # Llamar al método recursivo de inserción
            self._insertar_recursivo(self.raiz, valor)
        print(f"  [INSERT] {valor} insertado en el árbol.")

    def _insertar_recursivo(self, nodo_actual, valor):
        """Método interno recursivo para insertar un valor."""
        if valor < nodo_actual.valor:
            # El valor es menor → va al subárbol IZQUIERDO
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            # El valor es mayor → va al subárbol DERECHO
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
        # Si valor == nodo_actual.valor, no se insertan duplicados

    def buscar(self, valor):
        """Busca un valor en el árbol. Retorna True si lo encuentra."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        """Búsqueda recursiva dentro del árbol."""
        if nodo is None:
            return False   # Llegamos a un extremo sin encontrarlo
        if valor == nodo.valor:
            return True    # ¡Encontrado!
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)   # Buscar a la izquierda
        else:
            return self._buscar_recursivo(nodo.derecho, valor)     # Buscar a la derecha

    def inorden(self):
        """Recorrido Inorden: retorna los valores de menor a mayor."""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        """Recorre: izquierdo → raíz → derecho"""
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)   # 1. Izquierda
            resultado.append(nodo.valor)                          # 2. Raíz
            self._inorden_recursivo(nodo.derecho, resultado)      # 3. Derecha

    def preorden(self):
        """Recorrido Preorden: raíz → izquierdo → derecho"""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.valor)                           # 1. Raíz
            self._preorden_recursivo(nodo.izquierdo, resultado)   # 2. Izquierda
            self._preorden_recursivo(nodo.derecho, resultado)     # 3. Derecha

    def altura(self):
        """Calcula la altura del árbol (niveles de profundidad)."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        """Altura = 1 + max(altura_izquierda, altura_derecha)"""
        if nodo is None:
            return 0
        altura_izq = self._altura_recursiva(nodo.izquierdo)
        altura_der = self._altura_recursiva(nodo.derecho)
        return 1 + max(altura_izq, altura_der)


# ======= DEMOSTRACIÓN =======
print("=" * 50)
print("   DEMOSTRACIÓN DE ÁRBOL BINARIO DE BÚSQUEDA")
print("=" * 50)

arbol = ArbolBinarioBusqueda()

print("\n--- Insertando valores ---")
valores = [50, 30, 70, 20, 40, 60, 80, 10, 25]
for v in valores:
    arbol.insertar(v)

print(f"\nÁrbol construido con valores: {valores}")
print(f"\nRecorrido INORDEN   (ordenado ↑): {arbol.inorden()}")
print(f"Recorrido PREORDEN  (raíz primero): {arbol.preorden()}")
print(f"Altura del árbol: {arbol.altura()} niveles")

print("\n--- Búsqueda de valores ---")
for val in [40, 99, 10, 55]:
    encontrado = arbol.buscar(val)
    icono = "✓" if encontrado else "✗"
    print(f"  {icono} Buscar {val}: {'Encontrado' if encontrado else 'No existe'}")

print("""
Estructura visual del árbol:
         50
        /  \\
      30    70
     / \\   / \\
   20  40 60  80
   / \\
  10  25
""")

