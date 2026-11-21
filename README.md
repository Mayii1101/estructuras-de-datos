# 📚 Repositorio de Estructuras de Datos en Python

Repositorio educativo con ejemplos comentados de las principales estructuras de datos, implementadas en Python desde cero.

---

## 🗂️ Estructura del Repositorio

```
estructuras_datos/
│
├── lineales/              # Estructuras de acceso secuencial
│   ├── 01_lista.py
│   ├── 02_pila.py
│   ├── 03_cola.py
│   ├── 04_lista_enlazada.py
│   └── 05_deque.py
│
├── no_lineales/           # Estructuras jerárquicas y de red
│   ├── 01_arbol_binario.py
│   ├── 02_grafo.py
│   ├── 03_heap.py
│   ├── 04_tabla_hash.py
│   └── 05_conjunto_trie.py
│
├── ejemplos/              # Aplicaciones prácticas reales
│   ├── 01_pila_parentesis.py
│   ├── 02_cola_hospital.py
│   ├── 03_arbol_expresiones.py
│   ├── 04_lista_doble_reproductor.py
│   └── 05_grafo_dijkstra.py
│
├── archivos/              # Persistencia de estructuras en archivos
│   ├── 01_lista_archivo_txt.py
│   ├── 02_diccionario_json.py
│   ├── 03_pila_cola_csv.py
│   ├── 04_arbol_pickle.py
│   └── 05_grafo_archivos.py
│
└── README.md
```

---

## 📂 Carpeta: `lineales/`

Estructuras donde los elementos se organizan en secuencia, uno tras otro.

| Archivo | Estructura | Concepto clave |
|---|---|---|
| `01_lista.py` | Lista dinámica | `append`, `insert`, `remove`, índices |
| `02_pila.py` | Pila (Stack) | LIFO — último en entrar, primero en salir |
| `03_cola.py` | Cola (Queue) | FIFO — primero en entrar, primero en salir |
| `04_lista_enlazada.py` | Lista enlazada simple | Nodos con punteros al siguiente |
| `05_deque.py` | Deque (doble extremo) | Operaciones en ambos extremos |

---

## 📂 Carpeta: `no_lineales/`

Estructuras con relaciones jerárquicas o en red entre elementos.

| Archivo | Estructura | Concepto clave |
|---|---|---|
| `01_arbol_binario.py` | Árbol BST | Nodos con hijo izq/der, recorridos (inorden, preorden, postorden) |
| `02_grafo.py` | Grafo no dirigido | Vértices y aristas, BFS y DFS |
| `03_heap.py` | Montículo (Heap) | Min-Heap, Max-Heap, Cola de prioridad |
| `04_tabla_hash.py` | Tabla Hash | Función hash, colisiones, dict de Python |
| `05_conjunto_trie.py` | Conjunto + Trie | Operaciones de conjuntos, autocompletado |

---

## 📂 Carpeta: `ejemplos/`

Aplicaciones del mundo real que combinan múltiples estructuras.

| Archivo | Uso | Estructura usada |
|---|---|---|
| `01_pila_parentesis.py` | Verificar paréntesis balanceados | Pila |
| `02_cola_hospital.py` | Sistema de atención hospitalaria | Cola + Heap (prioridad) |
| `03_arbol_expresiones.py` | Evaluar fórmulas matemáticas | Árbol binario |
| `04_lista_doble_reproductor.py` | Playlist de música navegable | Lista doblemente enlazada |
| `05_grafo_dijkstra.py` | Ruta más corta entre ciudades | Grafo + Heap (Dijkstra) |

---

## 📂 Carpeta: `archivos/`

Cómo guardar y recuperar estructuras de datos en diferentes formatos.

| Archivo | Formato | Estructura guardada |
|---|---|---|
| `01_lista_archivo_txt.py` | `.txt` | Lista de elementos (una por línea) |
| `02_diccionario_json.py` | `.json` | Diccionario/base de datos de estudiantes |
| `03_pila_cola_csv.py` | `.csv` | Historial de pila + transacciones bancarias |
| `04_arbol_pickle.py` | `.pkl` | Árbol BST completo serializado |
| `05_grafo_archivos.py` | `.dot` / `.csv` / `.txt` | Grafo en múltiples formatos |

---

## ▶️ Cómo ejecutar

Desde la carpeta raíz del proyecto, ejecutar cualquier archivo:

```bash
# Ejemplo: ejecutar la pila
python lineales/02_pila.py

# Ejemplo: ejecutar Dijkstra
python ejemplos/05_grafo_dijkstra.py

# Ejemplo: guardar árbol en Pickle
python archivos/04_arbol_pickle.py
```

> No se requieren librerías externas. Solo Python 3.6+ y módulos estándar.

---

## 🧠 Conceptos cubiertos

- **Complejidad temporal**: O(1), O(log n), O(n), O(n log n)
- **Recursión**: árboles, grafos DFS
- **Iteración**: listas, colas, búsquedas
- **Orientación a objetos**: clases `Nodo`, `Pila`, `Cola`, `Arbol`, `Grafo`
- **Módulos estándar**: `collections`, `heapq`, `json`, `csv`, `pickle`, `os`

---

## 📝 Notas de estudio

Cada archivo contiene:
- Explicación de la estructura al inicio (docstring)
- Comentarios línea por línea explicando cada operación
- Una sección `# ======= DEMOSTRACIÓN =======` con ejemplos ejecutables
- Salida en consola con emojis e indicadores visuales

