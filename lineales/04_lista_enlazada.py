"""
========================================
ESTRUCTURA LINEAL: LISTA ENLAZADA (Linked List)
========================================
Una Lista Enlazada es una secuencia de NODOS donde cada nodo contiene:
  - Un dato (valor)
  - Una referencia (puntero) al siguiente nodo

A diferencia de las listas normales, los nodos no están en memoria
contigua. Se conectan mediante punteros.

Tipos:
  - Simple: cada nodo apunta solo al siguiente
  - Doble : cada nodo apunta al siguiente Y al anterior
  - Circular: el último nodo apunta al primero

Este ejemplo implementa una Lista Enlazada Simple.
"""

class Nodo:
    """Representa un nodo individual de la lista enlazada."""

    def __init__(self, dato):
        self.dato = dato        # El valor que almacena el nodo
        self.siguiente = None   # Puntero al siguiente nodo (None = fin de lista)


class ListaEnlazada:
    """Implementación de una Lista Enlazada Simple."""

    def __init__(self):
        self.cabeza = None   # El primer nodo (inicialmente no existe)
        self.tamaño = 0      # Contador de nodos

    def agregar_al_inicio(self, dato):
        """Inserta un nuevo nodo al principio de la lista."""
        nuevo_nodo = Nodo(dato)       # Crear el nuevo nodo
        nuevo_nodo.siguiente = self.cabeza  # El nuevo apunta a quien era el primero
        self.cabeza = nuevo_nodo      # El nuevo nodo pasa a ser la cabeza
        self.tamaño += 1
        print(f"  [INICIO] Agregado '{dato}' al inicio.")

    def agregar_al_final(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo es la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Recorrer hasta el último nodo
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente   # Avanzar al siguiente nodo
            actual.siguiente = nuevo_nodo  # El último ahora apunta al nuevo
        self.tamaño += 1
        print(f"  [FINAL]  Agregado '{dato}' al final.")

    def eliminar(self, dato):
        """Elimina el primer nodo con el valor especificado."""
        if self.cabeza is None:
            print("  [ERROR] Lista vacía.")
            return

        # Caso especial: el nodo a eliminar es la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente  # La nueva cabeza es el segundo nodo
            self.tamaño -= 1
            print(f"  [DELETE] '{dato}' eliminado (era la cabeza).")
            return

        # Buscar el nodo anterior al que se quiere eliminar
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                # Saltamos el nodo que queremos eliminar
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                print(f"  [DELETE] '{dato}' eliminado.")
                return
            actual = actual.siguiente

        print(f"  [ERROR] '{dato}' no encontrado en la lista.")

    def buscar(self, dato):
        """Busca un valor y retorna su posición (o -1 si no existe)."""
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # No encontrado

    def __str__(self):
        """Muestra la lista como: dato1 → dato2 → ... → None"""
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " → ".join(elementos) + " → None" if elementos else "Lista vacía"


# ======= DEMOSTRACIÓN =======
print("=" * 50)
print("    DEMOSTRACIÓN DE LISTA ENLAZADA")
print("=" * 50)

lista = ListaEnlazada()

print("\n--- Agregando elementos ---")
lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)
lista.agregar_al_inicio(5)   # Se inserta antes del 10
lista.agregar_al_final(40)

print("\nLista actual:")
print(lista)
print(f"Tamaño: {lista.tamaño}")

print("\n--- Buscar elementos ---")
pos = lista.buscar(20)
print(f"Posición de '20': {pos}")
pos = lista.buscar(99)
print(f"Posición de '99': {pos} (no existe)")

print("\n--- Eliminar elementos ---")
lista.eliminar(5)    # Eliminar cabeza
lista.eliminar(30)   # Eliminar del medio
lista.eliminar(99)   # Elemento inexistente

print("\nLista final:")
print(lista)

