"""
========================================
EJEMPLO: Uso de Pila para Verificar Paréntesis Balanceados
========================================
Problema clásico: dado un texto con paréntesis (), corchetes []
y llaves {}, verificar si están correctamente balanceados.

Ejemplo válido  : "(a + b) * [c - {d}]"
Ejemplo inválido: "(a + b] * [c"

La PILA es perfecta para este problema porque:
  - Al abrir un símbolo, lo apilamos
  - Al cerrar un símbolo, verificamos que el tope sea su pareja
"""

class VerificadorParentesis:
    """
    Usa una pila para validar que los símbolos de agrupación
    estén correctamente abiertos y cerrados.
    """

    # Diccionario que mapea cada cierre con su apertura correspondiente
    PARES = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Conjunto de símbolos de apertura
    APERTURA = set(PARES.values())

    def verificar(self, expresion):
        """
        Recorre la expresión carácter a carácter.
        Retorna True si está balanceada, False si no.
        """
        pila = []   # Nuestra pila para rastrear aperturas pendientes

        for i, caracter in enumerate(expresion):
            if caracter in self.APERTURA:
                # Si es un símbolo de apertura, lo apilamos
                pila.append(caracter)
                print(f"  Pos {i}: '{caracter}' abierto  → Pila: {pila}")

            elif caracter in self.PARES:
                # Es un símbolo de cierre
                if not pila:
                    # La pila está vacía: cierre sin apertura correspondiente
                    print(f"  Pos {i}: '{caracter}' cierra pero la pila está vacía → ✗ INVÁLIDO")
                    return False

                tope = pila.pop()   # Sacar el último símbolo abierto
                esperado = self.PARES[caracter]  # Qué apertura esperamos

                if tope != esperado:
                    # El cierre no corresponde con la apertura
                    print(f"  Pos {i}: '{caracter}' esperaba '{esperado}' pero encontró '{tope}' → ✗ INVÁLIDO")
                    return False

                print(f"  Pos {i}: '{caracter}' cierra '{tope}' correctamente → Pila: {pila}")

        # Al final, la pila debe estar vacía (todo lo abierto fue cerrado)
        if pila:
            print(f"  Símbolos sin cerrar: {pila} → ✗ INVÁLIDO")
            return False

        return True


# ======= DEMOSTRACIÓN =======
print("=" * 55)
print("  EJEMPLO: Verificador de Paréntesis con Pila")
print("=" * 55)

verificador = VerificadorParentesis()

casos = [
    "(a + b) * [c - {d}]",    # Válido
    "((()))",                   # Válido
    "{[()]}",                   # Válido
    "(a + b]",                  # Inválido: cierre incorrecto
    "(((",                      # Inválido: nunca se cierra
    ")",                        # Inválido: cierre sin apertura
    "[({})]",                   # Válido
    "[{()}]({",                 # Inválido
]

for expresion in casos:
    print(f"\nExpresión: '{expresion}'")
    es_valida = verificador.verificar(expresion)
    icono = "✓ BALANCEADA" if es_valida else "✗ NO BALANCEADA"
    print(f"  → Resultado: {icono}")
    print("-" * 40)

