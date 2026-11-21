"""
========================================
EJEMPLO: Cola para Simular Atención en un Hospital
========================================
Escenario: pacientes llegan a urgencias y son atendidos
por orden de llegada (FIFO). Luego se añade un nivel
de PRIORIDAD: pacientes críticos son atendidos primero.

Parte 1: Cola simple (FIFO) — sin prioridad
Parte 2: Cola de prioridad — pacientes más graves primero
"""

import heapq      # Para la cola de prioridad (min-heap)
import time       # Para simular tiempos de llegada
from collections import deque

# ========================================
#    PARTE 1: COLA SIMPLE
# ========================================
print("=" * 55)
print("   PARTE 1: Sala de Espera FIFO (sin prioridad)")
print("=" * 55)

class SalaEsperaSimple:
    """Cola FIFO para atender pacientes por orden de llegada."""

    def __init__(self):
        self._cola = deque()     # Cola de pacientes
        self._contador = 0      # Número de turno

    def registrar_paciente(self, nombre, motivo):
        """Un nuevo paciente llega a la sala."""
        self._contador += 1
        turno = f"T{self._contador:03d}"   # Turno formateado: T001, T002...
        self._cola.append((turno, nombre, motivo))
        print(f"  [LLEGA] Turno {turno}: {nombre} — Motivo: {motivo}")

    def atender_siguiente(self):
        """Atiende al primer paciente de la cola."""
        if not self._cola:
            print("  [INFO] No hay pacientes en espera.")
            return
        turno, nombre, motivo = self._cola.popleft()
        print(f"  [ATIENDE] Turno {turno}: {nombre} → Dr. en consultorio")
        return (turno, nombre, motivo)

    def pacientes_en_espera(self):
        """Muestra cuántos pacientes esperan."""
        return len(self._cola)


sala_simple = SalaEsperaSimple()

print("\n--- Llegada de pacientes ---")
sala_simple.registrar_paciente("Ana Martínez", "Dolor de cabeza")
sala_simple.registrar_paciente("Luis García", "Fiebre alta")
sala_simple.registrar_paciente("Carmen Ruiz", "Revisión de rutina")
sala_simple.registrar_paciente("Pedro Soto", "Fractura de brazo")

print(f"\nPacientes en espera: {sala_simple.pacientes_en_espera()}")

print("\n--- Atendiendo en orden de llegada ---")
while sala_simple.pacientes_en_espera() > 0:
    sala_simple.atender_siguiente()


# ========================================
#    PARTE 2: COLA DE PRIORIDAD
# ========================================
print("\n" + "=" * 55)
print("   PARTE 2: Urgencias con PRIORIDAD (Triage)")
print("=" * 55)
print("Niveles de prioridad:")
print("  1 = CRÍTICO  (atención inmediata)")
print("  2 = GRAVE    (atención urgente)")
print("  3 = MODERADO (puede esperar un poco)")
print("  4 = LEVE     (puede esperar más tiempo)\n")

class SalaUrgencias:
    """
    Cola de prioridad para urgencias.
    Los pacientes más graves (prioridad 1) se atienden primero.
    """

    def __init__(self):
        self._heap = []          # Min-heap: menor número = mayor urgencia
        self._secuencia = 0      # Desempate para igual prioridad: orden de llegada

    def registrar_paciente(self, nombre, prioridad, motivo):
        """Registra un paciente con su nivel de urgencia."""
        self._secuencia += 1
        # Tupla: (prioridad, secuencia, nombre, motivo)
        # La secuencia desempata cuando dos tienen igual prioridad
        entrada = (prioridad, self._secuencia, nombre, motivo)
        heapq.heappush(self._heap, entrada)
        niveles = {1: "CRÍTICO", 2: "GRAVE", 3: "MODERADO", 4: "LEVE"}
        print(f"  [LLEGA] [{niveles[prioridad]}] {nombre} — {motivo}")

    def atender_siguiente(self):
        """Atiende al paciente más urgente."""
        if not self._heap:
            print("  [INFO] No hay pacientes.")
            return
        prioridad, _, nombre, motivo = heapq.heappop(self._heap)
        niveles = {1: "CRÍTICO", 2: "GRAVE", 3: "MODERADO", 4: "LEVE"}
        print(f"  [ATIENDE] [{niveles[prioridad]}] {nombre} → Sala {prioridad}")

    def en_espera(self):
        return len(self._heap)


urgencias = SalaUrgencias()

print("--- Llegada de pacientes (en desorden de gravedad) ---")
urgencias.registrar_paciente("Sofía Ramos",   3, "Dolor de muelas")
urgencias.registrar_paciente("Mario Díaz",    1, "Infarto cardiaco")
urgencias.registrar_paciente("Elena Torres",  4, "Corte leve en dedo")
urgencias.registrar_paciente("Jorge Mendez",  2, "Fractura con hemorragia")
urgencias.registrar_paciente("Alicia Vega",   1, "Dificultad respiratoria")
urgencias.registrar_paciente("Tomás Ríos",    3, "Fiebre de 38°C")

print(f"\nPacientes en espera: {urgencias.en_espera()}")
print("\n--- Atendiendo por PRIORIDAD (no por llegada) ---")
while urgencias.en_espera() > 0:
    urgencias.atender_siguiente()

