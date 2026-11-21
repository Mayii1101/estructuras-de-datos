"""
========================================
ARCHIVOS: Guardar y Leer una Pila/Cola en CSV
========================================
CSV (Comma-Separated Values) es un formato tabular simple
donde los datos se separan por comas (o punto y coma).

Muy usado para:
  - Hojas de cálculo (Excel, Google Sheets)
  - Exportar/importar datos entre sistemas
  - Registros de logs y transacciones

Aquí simulamos el HISTORIAL DE OPERACIONES de una pila
y un registro de TRANSACCIONES bancarias guardado en CSV.
"""

import csv      # Módulo estándar para leer y escribir CSV
import os       # Para operaciones del sistema de archivos
from datetime import datetime   # Para marcas de tiempo

ARCHIVO_HISTORIAL = "archivos/historial_pila.csv"
ARCHIVO_BANCO     = "archivos/transacciones_banco.csv"

# =========================================
#   PARTE 1: Historial de Pila en CSV
# =========================================

class PilaConHistorial:
    """
    Pila que registra cada operación en un archivo CSV.
    Permite auditar qué se apilló y desapiló, cuándo y quién.
    """

    ENCABEZADOS = ["Timestamp", "Operación", "Elemento", "Tamaño_Pila"]

    def __init__(self, archivo=ARCHIVO_HISTORIAL, usuario="Sistema"):
        self._pila   = []          # La pila en memoria
        self._archivo = archivo    # Archivo CSV para el historial
        self._usuario = usuario    # Quién realiza las operaciones

        # Crear el archivo CSV con encabezados si no existe
        if not os.path.exists(archivo):
            with open(archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self.ENCABEZADOS)   # Escribir fila de encabezados
            print(f"  [CREADO] Archivo historial: '{archivo}'")

    def _registrar(self, operacion, elemento):
        """Escribe una línea en el CSV con los detalles de la operación."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self._archivo, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, operacion, elemento, len(self._pila)])

    def push(self, elemento):
        """Apila un elemento y registra la operación."""
        self._pila.append(elemento)
        self._registrar("PUSH", elemento)
        print(f"  [PUSH] '{elemento}' apilado. Pila: {self._pila}")

    def pop(self):
        """Desapila y registra la operación."""
        if not self._pila:
            print("  [ERROR] Pila vacía.")
            return None
        elemento = self._pila.pop()
        self._registrar("POP", elemento)
        print(f"  [POP]  '{elemento}' desapilado. Pila: {self._pila}")
        return elemento

    def ver_historial(self):
        """Lee y muestra el historial completo del CSV."""
        print(f"\n📋 Historial de operaciones ('{self._archivo}'):")
        print(f"{'─'*65}")
        with open(self._archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)   # Leer como diccionarios
            for fila in reader:
                print(f"  {fila['Timestamp']} | {fila['Operación']:<6} | "
                      f"'{fila['Elemento']:<15}' | Tamaño: {fila['Tamaño_Pila']}")
        print(f"{'─'*65}")


# =========================================
#   PARTE 2: Transacciones Bancarias en CSV
# =========================================

def crear_registro_banco():
    """Crea el archivo CSV de transacciones bancarias."""
    encabezados = ["ID", "Fecha", "Tipo", "Monto", "Saldo", "Descripción"]
    with open(ARCHIVO_BANCO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)

def registrar_transaccion(id_trans, tipo, monto, saldo, descripcion):
    """Agrega una transacción al archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(ARCHIVO_BANCO, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([id_trans, fecha, tipo, f"{monto:.2f}", f"{saldo:.2f}", descripcion])
    icono = "↑" if tipo == "DEPÓSITO" else "↓"
    print(f"  [{icono}] {tipo}: ${monto:.2f} | Saldo: ${saldo:.2f} | {descripcion}")

def calcular_balance():
    """Lee el CSV y calcula el saldo total."""
    total = 0.0
    with open(ARCHIVO_BANCO, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila['Tipo'] == 'DEPÓSITO':
                total += float(fila['Monto'])
            elif fila['Tipo'] == 'RETIRO':
                total -= float(fila['Monto'])
    return total


# ======= DEMOSTRACIÓN =======
print("=" * 65)
print("   ARCHIVOS: Pila y Transacciones guardadas en CSV")
print("=" * 65)

os.makedirs("archivos", exist_ok=True)

# -- Parte 1: Pila con historial --
print("\n--- Pila con historial en CSV ---")
pila = PilaConHistorial()
pila.push("Tarea_1")
pila.push("Tarea_2")
pila.push("Tarea_3")
pila.pop()
pila.push("Tarea_4")
pila.pop()
pila.pop()

pila.ver_historial()

# -- Parte 2: Banco --
print("\n--- Registro de transacciones bancarias ---")
crear_registro_banco()
saldo = 0.0

transacciones = [
    ("DEP001", "DEPÓSITO", 1000000, "Sueldo mensual"),
    ("RET001", "RETIRO",    150000, "Pago servicios"),
    ("DEP002", "DEPÓSITO",  200000, "Transferencia recibida"),
    ("RET002", "RETIRO",     80000, "Supermercado"),
    ("RET003", "RETIRO",    300000, "Arriendo"),
    ("DEP003", "DEPÓSITO",  500000, "Venta de artículo"),
]

for id_t, tipo, monto, desc in transacciones:
    if tipo == "DEPÓSITO":
        saldo += monto
    else:
        saldo -= monto
    registrar_transaccion(id_t, tipo, monto, saldo, desc)

print(f"\nBalance calculado desde el CSV: ${calcular_balance():,.2f}")

print(f"\nContenido completo de '{ARCHIVO_BANCO}':")
with open(ARCHIVO_BANCO, 'r', encoding='utf-8') as f:
    print(f.read())

