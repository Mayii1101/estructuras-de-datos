"""
========================================
EJEMPLO: Lista Enlazada para un Reproductor de Música
========================================
Simulamos una playlist de canciones con una Lista Doblemente Enlazada.
Cada canción puede ir hacia adelante o hacia atrás.

Una Lista Doblemente Enlazada (Doubly Linked List) tiene nodos que
apuntan TANTO al siguiente como al anterior:

  None ← [Canción 1] ↔ [Canción 2] ↔ [Canción 3] → None

Ventajas sobre la lista simple:
  - Navegación bidireccional (siguiente y anterior)
  - Eliminación más eficiente (conocemos el nodo anterior)
"""

class NodoCancion:
    """Nodo que representa una canción en la playlist."""

    def __init__(self, titulo, artista, duracion_seg):
        self.titulo      = titulo         # Nombre de la canción
        self.artista     = artista        # Nombre del artista
        self.duracion    = duracion_seg   # Duración en segundos
        self.siguiente   = None           # Puntero al siguiente nodo
        self.anterior    = None           # Puntero al nodo anterior

    def __str__(self):
        mins = self.duracion // 60
        segs = self.duracion % 60
        return f"♪ '{self.titulo}' - {self.artista} [{mins}:{segs:02d}]"


class ReproductorMusica:
    """
    Playlist implementada como Lista Doblemente Enlazada.
    Permite navegar hacia adelante y hacia atrás entre canciones.
    """

    def __init__(self):
        self.cabeza   = None   # Primera canción de la playlist
        self.cola     = None   # Última canción de la playlist
        self.actual   = None   # Canción que se está reproduciendo
        self.tamaño   = 0      # Número de canciones

    def agregar_cancion(self, titulo, artista, duracion):
        """Agrega una canción al FINAL de la playlist."""
        nueva = NodoCancion(titulo, artista, duracion)

        if self.cabeza is None:
            # La lista está vacía: la nueva es cabeza y cola
            self.cabeza = nueva
            self.cola   = nueva
            self.actual = nueva   # Establecer como canción actual
        else:
            # Conectar la nueva canción al final
            nueva.anterior   = self.cola    # La nueva apunta hacia atrás a la última
            self.cola.siguiente = nueva     # La última apunta hacia adelante a la nueva
            self.cola        = nueva        # Actualizar la cola

        self.tamaño += 1
        print(f"  [+] Agregada: {nueva}")

    def siguiente_cancion(self):
        """Avanza a la siguiente canción."""
        if self.actual is None:
            print("  [!] No hay canciones en la playlist.")
            return
        if self.actual.siguiente is None:
            print("  [!] Esta es la última canción. Volviendo al inicio...")
            self.actual = self.cabeza   # Comportamiento circular
        else:
            self.actual = self.actual.siguiente

        print(f"  [▶] Reproduciendo: {self.actual}")

    def cancion_anterior(self):
        """Regresa a la canción anterior."""
        if self.actual is None:
            print("  [!] No hay canciones.")
            return
        if self.actual.anterior is None:
            print("  [!] Esta es la primera canción. Yendo al final...")
            self.actual = self.cola   # Comportamiento circular
        else:
            self.actual = self.actual.anterior

        print(f"  [◀] Reproduciendo: {self.actual}")

    def reproducir_actual(self):
        """Muestra la canción que está sonando actualmente."""
        if self.actual:
            print(f"  [▶▶] Ahora: {self.actual}")
        else:
            print("  [!] Playlist vacía.")

    def eliminar_actual(self):
        """Elimina la canción actual y pasa a la siguiente."""
        if self.actual is None:
            print("  [!] No hay canción actual.")
            return

        eliminada = self.actual
        print(f"  [-] Eliminando: {eliminada}")

        # Determinar cuál será la nueva canción actual
        if self.actual.siguiente:
            nueva_actual = self.actual.siguiente
        elif self.actual.anterior:
            nueva_actual = self.actual.anterior
        else:
            nueva_actual = None   # La lista quedará vacía

        # Reconectar los nodos
        if eliminada.anterior:
            eliminada.anterior.siguiente = eliminada.siguiente
        else:
            self.cabeza = eliminada.siguiente   # Eliminar la cabeza

        if eliminada.siguiente:
            eliminada.siguiente.anterior = eliminada.anterior
        else:
            self.cola = eliminada.anterior      # Eliminar la cola

        self.actual = nueva_actual
        self.tamaño -= 1

    def mostrar_playlist(self):
        """Muestra todas las canciones de la playlist."""
        print(f"\n{'─'*50}")
        print(f"  PLAYLIST ({self.tamaño} canciones):")
        print(f"{'─'*50}")
        nodo = self.cabeza
        pos = 1
        while nodo:
            marcador = " ◄ ACTUAL" if nodo == self.actual else ""
            print(f"  {pos}. {nodo}{marcador}")
            nodo = nodo.siguiente
            pos += 1
        print(f"{'─'*50}")

    def duracion_total(self):
        """Calcula la duración total de la playlist."""
        total = 0
        nodo = self.cabeza
        while nodo:
            total += nodo.duracion
            nodo = nodo.siguiente
        mins = total // 60
        segs = total % 60
        return f"{mins}:{segs:02d}"


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("   EJEMPLO: Reproductor de Música con Lista Doble")
print("=" * 55)

reproductor = ReproductorMusica()

print("\n--- Cargando canciones ---")
reproductor.agregar_cancion("Blinding Lights",   "The Weeknd",   200)
reproductor.agregar_cancion("Shape of You",      "Ed Sheeran",   234)
reproductor.agregar_cancion("Bohemian Rhapsody", "Queen",        354)
reproductor.agregar_cancion("Stairway to Heaven","Led Zeppelin", 482)
reproductor.agregar_cancion("Hotel California",  "Eagles",       391)

reproductor.mostrar_playlist()
print(f"\nDuración total: {reproductor.duracion_total()}")

print("\n--- Navegación entre canciones ---")
reproductor.reproducir_actual()   # Canción 1
reproductor.siguiente_cancion()   # Canción 2
reproductor.siguiente_cancion()   # Canción 3
reproductor.cancion_anterior()    # Volver a canción 2

reproductor.mostrar_playlist()

print("\n--- Eliminar canción actual ---")
reproductor.eliminar_actual()     # Eliminar canción 2

reproductor.mostrar_playlist()

