"""
========================================
ESTRUCTURA LINEAL: COLA (Queue)
========================================
Una Cola es una estructura de datos tipo FIFO (First In, First Out),
es decir, el PRIMERO en entrar es el PRIMERO en salir.
Ejemplo del mundo real: la fila de un banco — el primero que llega,
primero es atendido.

Operaciones principales:
  - enqueue (encolar) : agregar al final de la cola
  - dequeue (desencolar): eliminar el primero de la cola
  - front            : ver el primero sin eliminarlo
  - is_empty         : verificar si está vacía
"""

from collections import deque  # deque es eficiente para operaciones en ambos extremos

class Cola:
    """Implementación de una Cola usando deque de Python."""

    def __init__(self):
        # Usamos deque para eficiencia O(1) al agregar/quitar
        self._elementos = deque()

    def enqueue(self, elemento):
        """Agrega un elemento al final de la cola (encolar)."""
        self._elementos.append(elemento)
        print(f"  [ENQUEUE] '{elemento}' ha entrado a la cola.")

    def dequeue(self):
        """Elimina y retorna el elemento del frente de la cola."""
        if self.is_empty():
            print("  [ERROR] La cola está vacía. No se puede desencolar.")
            return None
        elemento = self._elementos.popleft()  # popleft() elimina el primero
        print(f"  [DEQUEUE] '{elemento}' ha salido de la cola.")
        return elemento

    def front(self):
        """Retorna el elemento al frente sin eliminarlo."""
        if self.is_empty():
            return None
        return self._elementos[0]

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self._elementos) == 0

    def size(self):
        """Retorna el número de elementos en la cola."""
        return len(self._elementos)

    def __str__(self):
        """Representación visual: FRENTE → ... → FINAL"""
        if self.is_empty():
            return "Cola vacía"
        return "FRENTE → " + " → ".join(str(e) for e in self._elementos) + " → FINAL"


# ======= DEMOSTRACIÓN =======
print("=" * 50)
print("        DEMOSTRACIÓN DE COLA (Queue)")
print("=" * 50)

cola = Cola()

print(f"\n¿Está vacía? {cola.is_empty()}")

# Simular una fila de personas en un banco
print("\n--- Personas entrando al banco ---")
cola.enqueue("Carlos")
cola.enqueue("María")
cola.enqueue("Pedro")
cola.enqueue("Lucía")
cola.enqueue("Andrés")

# Ver el estado
print("\nEstado de la cola:")
print(cola)
print(f"Primero en ser atendido: {cola.front()}")
print(f"Total en espera: {cola.size()} personas")

# Atender personas (desencolar)
print("\n--- Atendiendo personas ---")
cola.dequeue()
cola.dequeue()

print("\nCola después de atender 2 personas:")
print(cola)

# Llega una persona más
print("\n--- Nueva persona llega ---")
cola.enqueue("Sofía")
print("Cola actualizada:")
print(cola)

