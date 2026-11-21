"""
========================================
ESTRUCTURA LINEAL: PILA (Stack)
========================================
Una Pila es una estructura de datos tipo LIFO (Last In, First Out),
es decir, el ÚLTIMO elemento en entrar es el PRIMERO en salir.
Ejemplo del mundo real: una pila de platos — añades y quitas desde arriba.

Operaciones principales:
  - push (apilar)  : agregar un elemento encima de la pila
  - pop  (desapilar): quitar el elemento del tope
  - peek           : ver el elemento del tope sin quitarlo
  - is_empty       : verificar si la pila está vacía
"""

class Pila:
    """Implementación de una Pila usando una lista de Python."""

    def __init__(self):
        # Inicializamos la pila como una lista vacía
        self._elementos = []

    def push(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self._elementos.append(elemento)
        print(f"  [PUSH] Elemento '{elemento}' apilado.")

    def pop(self):
        """Elimina y retorna el elemento del tope de la pila."""
        if self.is_empty():
            print("  [ERROR] La pila está vacía. No se puede desapilar.")
            return None
        elemento = self._elementos.pop()  # pop() de lista elimina el último
        print(f"  [POP]  Elemento '{elemento}' desapilado.")
        return elemento

    def peek(self):
        """Retorna el elemento del tope sin eliminarlo."""
        if self.is_empty():
            print("  [ERROR] La pila está vacía.")
            return None
        return self._elementos[-1]  # El índice -1 accede al último elemento

    def is_empty(self):
        """Verifica si la pila no tiene elementos."""
        return len(self._elementos) == 0

    def size(self):
        """Retorna el número de elementos en la pila."""
        return len(self._elementos)

    def __str__(self):
        """Representación visual de la pila (tope arriba)."""
        if self.is_empty():
            return "Pila vacía"
        visual = " ← TOPE\n".join(str(e) for e in reversed(self._elementos))
        return visual + " ← TOPE"


# ======= DEMOSTRACIÓN =======
print("=" * 40)
print("       DEMOSTRACIÓN DE PILA")
print("=" * 40)

pila = Pila()

# Verificar si está vacía al inicio
print(f"\n¿Está vacía? {pila.is_empty()}")

# Apilar varios elementos
print("\n--- Apilando elementos ---")
pila.push("Libro A")
pila.push("Libro B")
pila.push("Libro C")
pila.push("Libro D")

# Ver el estado actual
print("\nEstado de la pila (tope arriba):")
print(pila)

# Ver el tope sin eliminar
print(f"\nTope actual (peek): {pila.peek()}")
print(f"Tamaño de la pila: {pila.size()}")

# Desapilar elementos
print("\n--- Desapilando elementos ---")
pila.pop()
pila.pop()

print("\nEstado después de 2 pops:")
print(pila)

# Desapilar hasta vaciar
print("\n--- Vaciando la pila ---")
pila.pop()
pila.pop()
pila.pop()  # Intento sobre pila vacía

