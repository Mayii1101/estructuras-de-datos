"""
========================================
ESTRUCTURA NO LINEAL: CONJUNTO (Set) y TRIE
========================================
Este archivo cubre dos estructuras:

1. CONJUNTO (Set): colección de elementos ÚNICOS sin orden.
   Basado internamente en tabla hash → operaciones O(1).
   Ideal para: eliminar duplicados, operaciones de conjuntos matemáticos.

2. TRIE (Árbol de Prefijos): árbol especial para almacenar cadenas
   de texto. Cada nodo representa un carácter, y los caminos desde
   la raíz forman palabras.
   Ideal para: autocompletado, corrector ortográfico, búsqueda de prefijos.
"""

# ========================================
#    PARTE 1: CONJUNTO (Set)
# ========================================
print("=" * 55)
print("          PARTE 1: CONJUNTO (Set)")
print("=" * 55)

# Crear conjuntos
frutas_A = {"manzana", "pera", "uva", "mango", "manzana"}  # duplicado ignorado
frutas_B = {"uva", "sandía", "mango", "melón"}

print(f"\nConjunto A: {frutas_A}")   # 'manzana' solo aparece una vez
print(f"Conjunto B: {frutas_B}")

# Operaciones de conjuntos (matemáticas):
print("\n--- Operaciones de conjuntos ---")

# Unión: todos los elementos de A y B sin repetir
union = frutas_A | frutas_B
print(f"Unión (A | B):         {union}")

# Intersección: elementos que están en AMBOS conjuntos
interseccion = frutas_A & frutas_B
print(f"Intersección (A & B):  {interseccion}")

# Diferencia: lo que tiene A pero NO tiene B
diferencia = frutas_A - frutas_B
print(f"Diferencia (A - B):    {diferencia}")

# Diferencia simétrica: lo que está en uno pero no en ambos
sim_diff = frutas_A ^ frutas_B
print(f"Diferencia simétrica:  {sim_diff}")

# Agregar y eliminar elementos
print("\n--- Modificar el conjunto ---")
frutas_A.add("durazno")     # Agregar un elemento
print(f"Después de agregar 'durazno': {frutas_A}")
frutas_A.discard("pera")   # Eliminar (no lanza error si no existe)
print(f"Después de eliminar 'pera':   {frutas_A}")

# Verificar membresía
print(f"\n¿'mango' está en A? {'Sí' if 'mango' in frutas_A else 'No'}")
print(f"¿'pera' está en A?  {'Sí' if 'pera' in frutas_A else 'No'}")

# Eliminar duplicados de una lista usando Set
print("\n--- Uso práctico: eliminar duplicados ---")
lista_con_dup = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sin_duplicados = list(set(lista_con_dup))
print(f"Lista original: {lista_con_dup}")
print(f"Sin duplicados: {sorted(sin_duplicados)}")


# ========================================
#    PARTE 2: TRIE (Árbol de Prefijos)
# ========================================
print("\n" + "=" * 55)
print("        PARTE 2: TRIE (Árbol de Prefijos)")
print("=" * 55)

class NodoTrie:
    """Nodo del Trie: cada nodo guarda un carácter."""

    def __init__(self):
        # Diccionario de hijos: carácter → NodoTrie
        self.hijos = {}
        # Marca que indica si este nodo es el final de una palabra
        self.es_fin_de_palabra = False


class Trie:
    """
    Árbol de prefijos para almacenar y buscar cadenas de texto.
    Muy eficiente para autocompletado y validación de palabras.
    """

    def __init__(self):
        self.raiz = NodoTrie()   # La raíz no tiene carácter, solo hijos

    def insertar(self, palabra):
        """
        Inserta una palabra en el Trie.
        Recorre letra a letra, creando nodos si no existen.
        """
        nodo = self.raiz
        for caracter in palabra:
            if caracter not in nodo.hijos:
                # Si el carácter no existe como hijo, crear nuevo nodo
                nodo.hijos[caracter] = NodoTrie()
            nodo = nodo.hijos[caracter]   # Avanzar al hijo
        nodo.es_fin_de_palabra = True     # Marcar el último como fin de palabra
        print(f"  [INSERT] '{palabra}' insertada en el Trie.")

    def buscar(self, palabra):
        """Verifica si la palabra EXACTA está en el Trie."""
        nodo = self.raiz
        for caracter in palabra:
            if caracter not in nodo.hijos:
                return False   # El carácter no existe, palabra no encontrada
            nodo = nodo.hijos[caracter]
        return nodo.es_fin_de_palabra  # True solo si es una palabra completa

    def empieza_con(self, prefijo):
        """Verifica si alguna palabra en el Trie comienza con el prefijo dado."""
        nodo = self.raiz
        for caracter in prefijo:
            if caracter not in nodo.hijos:
                return False
            nodo = nodo.hijos[caracter]
        return True   # El prefijo existe (puede o no ser palabra completa)

    def autocompletar(self, prefijo):
        """Retorna todas las palabras que comienzan con el prefijo dado."""
        nodo = self.raiz
        for caracter in prefijo:
            if caracter not in nodo.hijos:
                return []   # Prefijo no existe
            nodo = nodo.hijos[caracter]

        # Encontrar todas las palabras desde este punto
        palabras = []
        self._dfs_palabras(nodo, prefijo, palabras)
        return palabras

    def _dfs_palabras(self, nodo, prefijo_actual, palabras):
        """Recorre el Trie en profundidad para recolectar palabras."""
        if nodo.es_fin_de_palabra:
            palabras.append(prefijo_actual)   # Es una palabra completa
        for caracter, hijo in nodo.hijos.items():
            self._dfs_palabras(hijo, prefijo_actual + caracter, palabras)


# ======= DEMOSTRACIÓN DEL TRIE =======
print()
trie = Trie()

palabras_dict = ["casa", "casas", "caso", "castillo", "pan", "papel",
                 "para", "park", "pato", "patos", "python", "pro"]
print("--- Insertando palabras ---")
for p in palabras_dict:
    trie.insertar(p)

print("\n--- Búsqueda exacta ---")
for p in ["casa", "cas", "python", "java"]:
    existe = trie.buscar(p)
    print(f"  {'✓' if existe else '✗'} '{p}': {'Existe' if existe else 'No existe'}")

print("\n--- Verificar prefijos ---")
for pref in ["cas", "pa", "py", "java"]:
    existe = trie.empieza_con(pref)
    print(f"  {'✓' if existe else '✗'} Prefijo '{pref}': {'Existe' if existe else 'No existe'}")

print("\n--- Autocompletar ---")
for pref in ["cas", "pa", "pro"]:
    sugerencias = trie.autocompletar(pref)
    print(f"  '{pref}...' → {sugerencias}")

