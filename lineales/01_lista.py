"""
========================================
ESTRUCTURA LINEAL: LISTA (List)
========================================
Una lista es una colección ordenada de elementos que permite
almacenar múltiples valores en una sola variable.
En Python, las listas son dinámicas (pueden cambiar de tamaño).
"""

# ---- Creación de una lista vacía ----
mi_lista = []

# ---- Agregar elementos al final de la lista ----
mi_lista.append(10)   # Agrega 10 al final
mi_lista.append(20)   # Agrega 20 al final
mi_lista.append(30)   # Agrega 30 al final
mi_lista.append(40)   # Agrega 40 al final
mi_lista.append(50)   # Agrega 50 al final

print("Lista inicial:", mi_lista)

# ---- Acceder a elementos por índice ----
# Los índices comienzan en 0
print("Primer elemento (índice 0):", mi_lista[0])
print("Último elemento (índice -1):", mi_lista[-1])

# ---- Insertar un elemento en una posición específica ----
mi_lista.insert(2, 99)  # Inserta 99 en la posición 2
print("Después de insertar 99 en posición 2:", mi_lista)

# ---- Eliminar un elemento por valor ----
mi_lista.remove(99)  # Elimina la primera ocurrencia del valor 99
print("Después de eliminar 99:", mi_lista)

# ---- Eliminar el último elemento con pop() ----
eliminado = mi_lista.pop()  # Remueve y retorna el último elemento
print("Elemento eliminado con pop():", eliminado)
print("Lista después del pop:", mi_lista)

# ---- Recorrer la lista con un bucle for ----
print("\nRecorriendo la lista:")
for i, elemento in enumerate(mi_lista):
    print(f"  Posición {i} → Valor: {elemento}")

# ---- Ordenar la lista ----
mi_lista_desordenada = [5, 1, 4, 2, 8, 3]
mi_lista_desordenada.sort()          # Ordena de menor a mayor
print("\nLista ordenada ascendente:", mi_lista_desordenada)
mi_lista_desordenada.sort(reverse=True)  # Ordena de mayor a menor
print("Lista ordenada descendente:", mi_lista_desordenada)

# ---- Longitud de la lista ----
print("\nLongitud de la lista:", len(mi_lista))

# ---- Verificar si un elemento existe ----
print("¿El 20 está en la lista?", 20 in mi_lista)
print("¿El 99 está en la lista?", 99 in mi_lista)

