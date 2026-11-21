"""
========================================
ESTRUCTURA LINEAL: DEQUE (Double-Ended Queue)
========================================
Un Deque (pronunciado "deck") es una cola de doble extremo.
Permite agregar y eliminar elementos TANTO por el frente
COMO por el final.

Es una generalización de la Pila y la Cola:
  - Como PILA  → usar solo el extremo derecho (append + pop)
  - Como COLA  → usar append al final y popleft al frente
  - Como DEQUE → usar ambos extremos libremente

Operaciones:
  - agregar_frente  : inserta al inicio
  - agregar_final   : inserta al final
  - quitar_frente   : elimina el primero
  - quitar_final    : elimina el último
"""

class Deque:
    """Implementación manual de un Deque con lista de Python."""

    def __init__(self):
        # Usamos una lista para almacenar los elementos del deque
        self._datos = []

    def agregar_frente(self, elemento):
        """Inserta un elemento al inicio (frente) del deque."""
        self._datos.insert(0, elemento)   # insert(0, ...) inserta al inicio
        print(f"  [FRENTE ←] '{elemento}' agregado al frente.")

    def agregar_final(self, elemento):
        """Inserta un elemento al final del deque."""
        self._datos.append(elemento)      # append() agrega al final
        print(f"  [→ FINAL]  '{elemento}' agregado al final.")

    def quitar_frente(self):
        """Elimina y retorna el primer elemento del deque."""
        if self.is_empty():
            print("  [ERROR] El deque está vacío.")
            return None
        elemento = self._datos.pop(0)     # pop(0) elimina el primero
        print(f"  [← FRENTE] '{elemento}' quitado del frente.")
        return elemento

    def quitar_final(self):
        """Elimina y retorna el último elemento del deque."""
        if self.is_empty():
            print("  [ERROR] El deque está vacío.")
            return None
        elemento = self._datos.pop()      # pop() sin argumento elimina el último
        print(f"  [FINAL →]  '{elemento}' quitado del final.")
        return elemento

    def ver_frente(self):
        """Retorna el primer elemento sin eliminarlo."""
        return self._datos[0] if not self.is_empty() else None

    def ver_final(self):
        """Retorna el último elemento sin eliminarlo."""
        return self._datos[-1] if not self.is_empty() else None

    def is_empty(self):
        """Verifica si el deque no tiene elementos."""
        return len(self._datos) == 0

    def size(self):
        """Retorna el número de elementos."""
        return len(self._datos)

    def __str__(self):
        """Representación visual del deque."""
        if self.is_empty():
            return "Deque vacío"
        return "[FRENTE] " + " | ".join(str(e) for e in self._datos) + " [FINAL]"


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("          DEMOSTRACIÓN DE DEQUE")
print("=" * 55)

dq = Deque()

print("\n--- Agregando por ambos extremos ---")
dq.agregar_final("Centro")
dq.agregar_frente("Inicio")
dq.agregar_final("Fin")
dq.agregar_frente("Antes del inicio")
dq.agregar_final("Después del fin")

print("\nEstado del deque:")
print(dq)
print(f"Frente: {dq.ver_frente()} | Final: {dq.ver_final()}")
print(f"Tamaño: {dq.size()}")

print("\n--- Quitando por ambos extremos ---")
dq.quitar_frente()
dq.quitar_final()

print("\nDeque actualizado:")
print(dq)

# Uso del deque como palíndromo checker
print("\n" + "=" * 55)
print("  APLICACIÓN: Verificar palíndromo con Deque")
print("=" * 55)

def es_palindromo(palabra):
    """
    Usa un deque para verificar si una palabra es palíndromo.
    Compara letra del frente con letra del final iterativamente.
    """
    from collections import deque
    d = deque(palabra.lower())   # Convertir a minúsculas y cargar en deque

    while len(d) > 1:
        if d.popleft() != d.pop():  # Comparar primer y último carácter
            return False
    return True

palabras = ["radar", "python", "anilina", "datos", "reconocer", "casa"]
for p in palabras:
    resultado = "✓ ES palíndromo" if es_palindromo(p) else "✗ NO es palíndromo"
    print(f"  '{p}': {resultado}")

