"""
Motor matemático para Matemática Discreta — Fase 1.
Traducción de LogicaMatematica.cpp a Python.

Ventaja principal: Python maneja enteros de precisión arbitraria,
eliminando por completo el problema de desbordamiento que existía en C++.
"""

from math import factorial as _factorial
from itertools import product as _product
from typing import List, Tuple, Dict


# ═══════════════════════════════════════════════════════════════
#  COMBINATORIA
# ═══════════════════════════════════════════════════════════════

def factorial(n: int) -> int:
    """
    Calcula n! (factorial de n).
    Python soporta enteros de precisión arbitraria — sin límite de overflow.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return _factorial(n)


def permutacion(n: int, r: int) -> int:
    """Calcula P(n, r) = n! / (n - r)!"""
    if n < 0 or r < 0:
        raise ValueError("Los valores de n y r deben ser no negativos.")
    if n < r:
        raise ValueError("El valor de n debe ser mayor o igual a r.")
    return _factorial(n) // _factorial(n - r)


def combinacion(n: int, r: int) -> int:
    """Calcula C(n, r) = n! / (r! × (n - r)!)"""
    if n < 0 or r < 0:
        raise ValueError("Los valores de n y r deben ser no negativos.")
    if n < r:
        raise ValueError("El valor de n debe ser mayor o igual a r.")
    return _factorial(n) // (_factorial(r) * _factorial(n - r))


# ═══════════════════════════════════════════════════════════════
#  PRODUCTO CARTESIANO
# ═══════════════════════════════════════════════════════════════

MAX_TUPLAS = 10_000


def producto_cartesiano(conjuntos: List[List[str]]) -> List[Tuple[str, ...]]:
    """
    Calcula el producto cartesiano de múltiples conjuntos.
    Limita el resultado a MAX_TUPLAS para evitar uso excesivo de memoria.
    """
    if not conjuntos or any(len(c) == 0 for c in conjuntos):
        return []

    total = 1
    for c in conjuntos:
        total *= len(c)

    if total > MAX_TUPLAS:
        raise ValueError(
            f"El resultado tendría {total:,} tuplas, lo cual excede "
            f"el límite de {MAX_TUPLAS:,}. Reduce la cantidad de elementos."
        )

    return list(_product(*conjuntos))


# ═══════════════════════════════════════════════════════════════
#  DIAGRAMA DE VENN — INCLUSIÓN-EXCLUSIÓN (3 CONJUNTOS)
# ═══════════════════════════════════════════════════════════════

VARIABLES_VENN = {
    "U": "Universo (U)",
    "A": "Conjunto A",
    "B": "Conjunto B",
    "C": "Conjunto C",
    "AnB": "A ∩ B",
    "AnC": "A ∩ C",
    "BnC": "B ∩ C",
    "AnBnC": "A ∩ B ∩ C",
    "Complemento": "Complemento",
}

VARIABLES_VENN_2 = {
    "U": "Universo (U)",
    "A": "Conjunto A",
    "B": "Conjunto B",
    "AnB": "A ∩ B",
    "Complemento": "Complemento",
}


def resolver_venn(
    *,
    U: int, A: int, B: int, C: int,
    AnB: int, AnC: int, BnC: int, AnBnC: int,
    Complemento: int,
    incognita: str,
) -> Tuple[int, str, Dict[str, int]]:
    """
    Resuelve la fórmula de Inclusión-Exclusión para 3 conjuntos.
    Despeja la variable indicada como incógnita.

    Args:
        U, A, B, C, AnB, AnC, BnC, AnBnC, Complemento: valores conocidos (0 para incógnita)
        incognita: nombre de la variable a despejar

    Returns:
        (resultado, pasos_markdown, regiones_exclusivas)
    """
    pasos = "### Fórmula de Inclusión-Exclusión\n\n"
    pasos += "$$|A \\cup B \\cup C| = |A| + |B| + |C| - |A \\cap B| - |A \\cap C| - |B \\cap C| + |A \\cap B \\cap C|$$\n\n"
    pasos += "$$U = |A \\cup B \\cup C| + \\text{Complemento}$$\n\n"
    pasos += "---\n\n"

    resultado = 0

    if incognita == "U":
        resultado = A + B + C - AnB - AnC - BnC + AnBnC + Complemento
        U = resultado
        pasos += "**Incógnita: Universo (U)**\n\n"
        pasos += "$$U = |A| + |B| + |C| - |A \\cap B| - |A \\cap C| - |B \\cap C| + |A \\cap B \\cap C| + \\text{Comp}$$\n\n"
        pasos += f"$$U = {A} + {B} + {C} - {AnB} - {AnC} - {BnC} + {AnBnC} + {Complemento}$$\n\n"
        pasos += f"$$\\boxed{{U = {resultado}}}$$"

    elif incognita == "Complemento":
        AUBUC = A + B + C - AnB - AnC - BnC + AnBnC
        resultado = U - AUBUC
        Complemento = resultado
        pasos += "**Incógnita: Complemento**\n\n"
        pasos += "$$\\text{Comp} = U - (|A| + |B| + |C| - |A \\cap B| - |A \\cap C| - |B \\cap C| + |A \\cap B \\cap C|)$$\n\n"
        pasos += f"$$\\text{{Comp}} = {U} - ({A} + {B} + {C} - {AnB} - {AnC} - {BnC} + {AnBnC})$$\n\n"
        pasos += f"$$\\text{{Comp}} = {U} - {AUBUC}$$\n\n"
        pasos += f"$$\\boxed{{\\text{{Complemento}} = {resultado}}}$$"

    elif incognita == "A":
        AUBUC = U - Complemento
        resultado = AUBUC - B - C + AnB + AnC + BnC - AnBnC
        A = resultado
        pasos += "**Incógnita: Conjunto A**\n\n"
        pasos += "$$|A| = |A \\cup B \\cup C| - |B| - |C| + |A \\cap B| + |A \\cap C| + |B \\cap C| - |A \\cap B \\cap C|$$\n\n"
        pasos += f"$$|A| = ({U} - {Complemento}) - {B} - {C} + {AnB} + {AnC} + {BnC} - {AnBnC}$$\n\n"
        pasos += f"$$\\boxed{{A = {resultado}}}$$"

    elif incognita == "B":
        AUBUC = U - Complemento
        resultado = AUBUC - A - C + AnB + AnC + BnC - AnBnC
        B = resultado
        pasos += "**Incógnita: Conjunto B**\n\n"
        pasos += "$$|B| = |A \\cup B \\cup C| - |A| - |C| + |A \\cap B| + |A \\cap C| + |B \\cap C| - |A \\cap B \\cap C|$$\n\n"
        pasos += f"$$|B| = ({U} - {Complemento}) - {A} - {C} + {AnB} + {AnC} + {BnC} - {AnBnC}$$\n\n"
        pasos += f"$$\\boxed{{B = {resultado}}}$$"

    elif incognita == "C":
        AUBUC = U - Complemento
        resultado = AUBUC - A - B + AnB + AnC + BnC - AnBnC
        C = resultado
        pasos += "**Incógnita: Conjunto C**\n\n"
        pasos += "$$|C| = |A \\cup B \\cup C| - |A| - |B| + |A \\cap B| + |A \\cap C| + |B \\cap C| - |A \\cap B \\cap C|$$\n\n"
        pasos += f"$$|C| = ({U} - {Complemento}) - {A} - {B} + {AnB} + {AnC} + {BnC} - {AnBnC}$$\n\n"
        pasos += f"$$\\boxed{{C = {resultado}}}$$"

    elif incognita == "AnB":
        AUBUC = U - Complemento
        resultado = A + B + C - AnC - BnC + AnBnC - AUBUC
        AnB = resultado
        pasos += "**Incógnita: A ∩ B**\n\n"
        pasos += "$$|A \\cap B| = |A| + |B| + |C| - |A \\cap C| - |B \\cap C| + |A \\cap B \\cap C| - |A \\cup B \\cup C|$$\n\n"
        pasos += f"$$|A \\cap B| = {A} + {B} + {C} - {AnC} - {BnC} + {AnBnC} - {AUBUC}$$\n\n"
        pasos += f"$$\\boxed{{A \\cap B = {resultado}}}$$"

    elif incognita == "AnC":
        AUBUC = U - Complemento
        resultado = A + B + C - AnB - BnC + AnBnC - AUBUC
        AnC = resultado
        pasos += "**Incógnita: A ∩ C**\n\n"
        pasos += "$$|A \\cap C| = |A| + |B| + |C| - |A \\cap B| - |B \\cap C| + |A \\cap B \\cap C| - |A \\cup B \\cup C|$$\n\n"
        pasos += f"$$|A \\cap C| = {A} + {B} + {C} - {AnB} - {BnC} + {AnBnC} - {AUBUC}$$\n\n"
        pasos += f"$$\\boxed{{A \\cap C = {resultado}}}$$"

    elif incognita == "BnC":
        AUBUC = U - Complemento
        resultado = A + B + C - AnB - AnC + AnBnC - AUBUC
        BnC = resultado
        pasos += "**Incógnita: B ∩ C**\n\n"
        pasos += "$$|B \\cap C| = |A| + |B| + |C| - |A \\cap B| - |A \\cap C| + |A \\cap B \\cap C| - |A \\cup B \\cup C|$$\n\n"
        pasos += f"$$|B \\cap C| = {A} + {B} + {C} - {AnB} - {AnC} + {AnBnC} - {AUBUC}$$\n\n"
        pasos += f"$$\\boxed{{B \\cap C = {resultado}}}$$"

    elif incognita == "AnBnC":
        AUBUC = U - Complemento
        resultado = AUBUC - A - B - C + AnB + AnC + BnC
        AnBnC = resultado
        pasos += "**Incógnita: A ∩ B ∩ C**\n\n"
        pasos += "$$|A \\cap B \\cap C| = |A \\cup B \\cup C| - |A| - |B| - |C| + |A \\cap B| + |A \\cap C| + |B \\cap C|$$\n\n"
        pasos += f"$$|A \\cap B \\cap C| = {AUBUC} - {A} - {B} - {C} + {AnB} + {AnC} + {BnC}$$\n\n"
        pasos += f"$$\\boxed{{A \\cap B \\cap C = {resultado}}}$$"

    # ── Regiones exclusivas para el diagrama visual ──
    # venn3 espera: (solo_A, solo_B, solo_AB, solo_C, solo_AC, solo_BC, ABC)
    regiones = {
        "solo_A": A - AnB - AnC + AnBnC,
        "solo_B": B - AnB - BnC + AnBnC,
        "solo_AB": AnB - AnBnC,
        "solo_C": C - AnC - BnC + AnBnC,
        "solo_AC": AnC - AnBnC,
        "solo_BC": BnC - AnBnC,
        "ABC": AnBnC,
        "complemento": Complemento,
    }

    return resultado, pasos, regiones


# ═══════════════════════════════════════════════════════════════
#  DIAGRAMA DE VENN — INCLUSIÓN-EXCLUSIÓN (2 CONJUNTOS)
# ═══════════════════════════════════════════════════════════════

def resolver_venn_2_conjuntos(
    *,
    U: int, A: int, B: int,
    AnB: int,
    Complemento: int,
    incognita: str,
) -> Tuple[int, str, Dict[str, int]]:
    """
    Resuelve la fórmula de Inclusión-Exclusión para 2 conjuntos.
    """
    pasos = "### Fórmula de Inclusión-Exclusión (2 Conjuntos)\n\n"
    pasos += "$$|A \cup B| = |A| + |B| - |A \cap B|$$\n\n"
    pasos += "$$U = |A \cup B| + \text{Complemento}$$\n\n"
    pasos += "---\n\n"

    resultado = 0

    if incognita == "U":
        resultado = A + B - AnB + Complemento
        U = resultado
        pasos += "**Incógnita: Universo (U)**\n\n"
        pasos += "$$U = |A| + |B| - |A \cap B| + \text{Comp}$$\n\n"
        pasos += f"$$U = {A} + {B} - {AnB} + {Complemento}$$\n\n"
        pasos += f"$$\\boxed{{U = {resultado}}}$$"

    elif incognita == "Complemento":
        AUB = A + B - AnB
        resultado = U - AUB
        Complemento = resultado
        pasos += "**Incógnita: Complemento**\n\n"
        pasos += "$$\text{Comp} = U - (|A| + |B| - |A \cap B|)$$\n\n"
        pasos += f"$$\text{{Comp}} = {U} - ({A} + {B} - {AnB})$$\n\n"
        pasos += f"$$\text{{Comp}} = {U} - {AUB}$$\n\n"
        pasos += f"$$\\boxed{{\text{{Complemento}} = {resultado}}}$$"

    elif incognita == "A":
        AUB = U - Complemento
        resultado = AUB - B + AnB
        A = resultado
        pasos += "**Incógnita: Conjunto A**\n\n"
        pasos += "$$|A| = |A \cup B| - |B| + |A \cap B|$$\\n\n"
        pasos += f"$$|A| = ({U} - {Complemento}) - {B} + {AnB}$$\n\n"
        pasos += f"$$\\boxed{{A = {resultado}}}$$"

    elif incognita == "B":
        AUB = U - Complemento
        resultado = AUB - A + AnB
        B = resultado
        pasos += "**Incógnita: Conjunto B**\n\n"
        pasos += "$$|B| = |A \cup B| - |A| + |A \cap B|$$\\n\n"
        pasos += f"$$|B| = ({U} - {Complemento}) - {A} + {AnB}$$\n\n"
        pasos += f"$$\\boxed{{B = {resultado}}}$$"

    elif incognita == "AnB":
        AUB = U - Complemento
        resultado = A + B - AUB
        AnB = resultado
        pasos += "**Incógnita: A ∩ B**\n\n"
        pasos += "$$|A \cap B| = |A| + |B| - |A \cup B|$$\n\n"
        pasos += f"$$|A \cap B| = {A} + {B} - ({U} - {Complemento})$$\n\n"
        pasos += f"$$\\boxed{{A \cap B = {resultado}}}$$"

    regiones = {
        "solo_A": A - AnB,
        "solo_B": B - AnB,
        "AB": AnB,
        "complemento": Complemento,
    }

    return resultado, pasos, regiones
