"""
========================================
EJEMPLO: Árbol Binario para Expresiones Matemáticas
========================================
Un Árbol de Expresión (Expression Tree) representa una
fórmula matemática como árbol binario donde:
  - Las HOJAS son operandos (números)
  - Los NODOS INTERNOS son operadores (+, -, *, /)

Ejemplo: (3 + 5) * (10 - 2)

         *
        / \\
       +   -
      / \\ / \\
     3  5 10  2

Al recorrer el árbol en Postorden se obtiene la notación polaca
inversa (RPN), que es fácil de evaluar con una pila.
"""

class NodoExpresion:
    """Nodo del árbol de expresión."""

    def __init__(self, valor):
        self.valor = valor         # Operador o número
        self.izquierdo = None      # Operando/subexpresión izquierda
        self.derecho = None        # Operando/subexpresión derecha

    def es_hoja(self):
        """Un nodo es hoja si no tiene hijos (es un número)."""
        return self.izquierdo is None and self.derecho is None


class ArbolExpresion:
    """
    Árbol Binario de Expresión Matemática.
    Permite construir, mostrar y evaluar expresiones matemáticas.
    """

    def __init__(self, raiz=None):
        self.raiz = raiz   # Nodo raíz del árbol

    def evaluar(self, nodo=None):
        """
        Evalúa recursivamente la expresión representada por el árbol.
        Los nodos hoja son números, los internos son operadores.
        """
        if nodo is None:
            nodo = self.raiz

        # Caso base: si es una hoja, retornar su valor numérico
        if nodo.es_hoja():
            return float(nodo.valor)

        # Evaluar recursivamente los subárboles
        valor_izq = self.evaluar(nodo.izquierdo)
        valor_der = self.evaluar(nodo.derecho)

        # Aplicar el operador del nodo actual
        if nodo.valor == '+':
            return valor_izq + valor_der
        elif nodo.valor == '-':
            return valor_izq - valor_der
        elif nodo.valor == '*':
            return valor_izq * valor_der
        elif nodo.valor == '/':
            if valor_der == 0:
                raise ZeroDivisionError("División por cero en la expresión.")
            return valor_izq / valor_der

    def inorden(self, nodo=None, primer_llamado=True):
        """
        Recorrido Inorden → produce la expresión en notación INFIJA:
        operando operador operando (la forma que usamos normalmente).
        """
        if primer_llamado:
            nodo = self.raiz
        if nodo is None:
            return ""
        if nodo.es_hoja():
            return str(nodo.valor)

        izq = self.inorden(nodo.izquierdo, False)
        der = self.inorden(nodo.derecho, False)
        return f"({izq} {nodo.valor} {der})"

    def postorden(self, nodo=None, primer_llamado=True):
        """
        Recorrido Postorden → notación POLACA INVERSA (RPN).
        Los operadores van después de sus operandos.
        """
        if primer_llamado:
            nodo = self.raiz
        if nodo is None:
            return ""
        if nodo.es_hoja():
            return str(nodo.valor)

        izq = self.postorden(nodo.izquierdo, False)
        der = self.postorden(nodo.derecho, False)
        return f"{izq} {der} {nodo.valor}"

    def preorden(self, nodo=None, primer_llamado=True):
        """
        Recorrido Preorden → notación POLACA PREFIJA.
        El operador va antes de sus operandos.
        """
        if primer_llamado:
            nodo = self.raiz
        if nodo is None:
            return ""
        if nodo.es_hoja():
            return str(nodo.valor)

        izq = self.preorden(nodo.izquierdo, False)
        der = self.preorden(nodo.derecho, False)
        return f"{nodo.valor} {izq} {der}"


def construir_arbol_1():
    """
    Construye el árbol para: (3 + 5) * (10 - 2)
    Resultado esperado: 64.0
    """
    raiz = NodoExpresion('*')

    # Subárbol izquierdo: (3 + 5)
    suma = NodoExpresion('+')
    suma.izquierdo = NodoExpresion('3')
    suma.derecho   = NodoExpresion('5')

    # Subárbol derecho: (10 - 2)
    resta = NodoExpresion('-')
    resta.izquierdo = NodoExpresion('10')
    resta.derecho   = NodoExpresion('2')

    raiz.izquierdo = suma
    raiz.derecho   = resta
    return raiz


def construir_arbol_2():
    """
    Construye el árbol para: (6 / 2) + (4 * 3)
    Resultado esperado: 15.0
    """
    raiz = NodoExpresion('+')

    # (6 / 2)
    div = NodoExpresion('/')
    div.izquierdo = NodoExpresion('6')
    div.derecho   = NodoExpresion('2')

    # (4 * 3)
    mult = NodoExpresion('*')
    mult.izquierdo = NodoExpresion('4')
    mult.derecho   = NodoExpresion('3')

    raiz.izquierdo = div
    raiz.derecho   = mult
    return raiz


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("   EJEMPLO: Árbol de Expresión Matemática")
print("=" * 55)

expresiones = [
    ("(3 + 5) * (10 - 2)", construir_arbol_1()),
    ("(6 / 2) + (4 * 3)",  construir_arbol_2()),
]

for descripcion, raiz in expresiones:
    arbol = ArbolExpresion(raiz)
    print(f"\nExpresión: {descripcion}")
    print(f"  Notación Infija  (Inorden)   : {arbol.inorden()}")
    print(f"  Notación Prefija (Preorden)  : {arbol.preorden()}")
    print(f"  Notación RPN     (Postorden) : {arbol.postorden()}")
    print(f"  Resultado evaluado           : {arbol.evaluar()}")
    print("-" * 50)

