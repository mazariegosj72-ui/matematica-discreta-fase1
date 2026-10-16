"""
Módulo de Aritmética y Teoría de Números para Matemática Discreta.

Cálculo de:
- MSM (Mínimo Sub-Múltiplo / Mínimo Común Múltiplo - MCM)
- MSD (Máximo Sub-Divisor / Máximo Común Divisor - MCD)

Métodos disponibles:
1. Por Algoritmo (Algoritmo de Euclides para MCD y Relación Fundamental para MCM).
2. Por Descomposición en Factores Primos (Factorización individual con comparación de exponentes y tabla de factorización simultánea tradicional).
"""

from typing import List, Tuple, Dict, Any


def descomponer_factores_primos(n: int) -> Tuple[Dict[int, int], List[Tuple[int, int]]]:
    """
    Descompone un número entero positivo n en sus factores primos.

    Retorna:
        - factores: Dict {primo: exponente}
        - pasos: Lista de tuplas (valor_antes_de_dividir, factor_primo)
    """
    if n <= 0:
        raise ValueError("El número debe ser un entero positivo mayor a 0.")

    factores = {}
    pasos = []
    d = 2
    temp = n

    while d * d <= temp:
        while temp % d == 0:
            pasos.append((temp, d))
            factores[d] = factores.get(d, 0) + 1
            temp //= d
        d += 1 if d == 2 else 2

    if temp > 1:
        pasos.append((temp, temp))
        factores[temp] = factores.get(temp, 0) + 1

    return factores, pasos


def algoritmo_euclides(a: int, b: int) -> Tuple[int, List[Dict[str, Any]]]:
    """
    Calcula el Máximo Común Divisor (MSD / MCD) mediante el Algoritmo de Euclides.
    Retorna el valor de MCD y la lista de filas con cada división sucesiva:
    Dividendo = Divisor × Cociente + Residuo.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser enteros positivos mayores que 0.")

    # Asegurar que num1 >= num2 para orden de presentación clásico
    num1, num2 = max(a, b), min(a, b)
    filas = []
    paso = 1

    while num2 != 0:
        q = num1 // num2
        r = num1 % num2
        filas.append({
            "paso": paso,
            "dividendo": num1,
            "divisor": num2,
            "cociente": q,
            "residuo": r,
            "ecuacion": f"{num1} = {num2} \\times {q} + {r}",
        })
        num1, num2 = num2, r
        paso += 1

    mcd = num1
    return mcd, filas


def calcular_msm_algoritmo(a: int, b: int, mcd: int) -> Tuple[int, str]:
    """
    Calcula el Mínimo Común Múltiplo (MSM / MCM) usando la Relación Fundamental:
    MSM(a, b) = (a × b) / MSD(a, b).
    """
    producto = a * b
    msm = producto // mcd
    explicacion = (
        f"$$\\text{{MSM}}({a}, {b}) = \\frac{{{a} \\times {b}}}{{\\text{{MSD}}({a}, {b})}} = "
        f"\\frac{{{producto:,}}}{{{mcd}}} = {msm:,}$$"
    )
    return msm, explicacion


def factorizacion_simultanea(a: int, b: int) -> Tuple[List[Dict[str, Any]], int, int]:
    """
    Ejecuta la descomposición simultánea clásica de dos números en factores primos.
    Retorna:
        - filas: Lista con el estado de a, b, el divisor primo y si dividió a ambos
        - msd: Máximo Sub-Divisor obtenido
        - msm: Mínimo Sub-Múltiplo obtenido
    """
    curr_a, curr_b = a, b
    filas = []
    primo = 2
    msd = 1
    msm = 1

    while curr_a > 1 or curr_b > 1:
        # Verificar si el primo actual divide a al menos uno
        divide_a = (curr_a % primo == 0)
        divide_b = (curr_b % primo == 0)

        if divide_a or divide_b:
            divide_ambos = divide_a and divide_b
            filas.append({
                "a": curr_a,
                "b": curr_b,
                "primo": primo,
                "divide_ambos": divide_ambos,
            })

            msm *= primo
            if divide_ambos:
                msd *= primo

            if divide_a:
                curr_a //= primo
            if divide_b:
                curr_b //= primo
        else:
            primo += 1 if primo == 2 else 2

    # Fila final (1, 1)
    filas.append({
        "a": 1,
        "b": 1,
        "primo": "-",
        "divide_ambos": False,
    })

    return filas, msd, msm


def comparar_factores_primos(a: int, b: int) -> Dict[str, Any]:
    """
    Compara los factores primos de a y b.
    Calcula:
        - MSD tomando los factores comunes con el menor exponente (min).
        - MSM tomando todos los factores con el mayor exponente (max).
    """
    factores_a, pasos_a = descomponer_factores_primos(a)
    factores_b, pasos_b = descomponer_factores_primos(b)

    todos_los_primos = sorted(list(set(factores_a.keys()) | set(factores_b.keys())))

    tabla_comparativa = []
    msd_factores = []
    msm_factores = []

    msd = 1
    msm = 1

    for p in todos_los_primos:
        exp_a = factores_a.get(p, 0)
        exp_b = factores_b.get(p, 0)
        min_exp = min(exp_a, exp_b)
        max_exp = max(exp_a, exp_b)

        es_comun = (exp_a > 0 and exp_b > 0)

        if min_exp > 0:
            msd *= (p ** min_exp)
            msd_factores.append(f"{p}^{min_exp}" if min_exp > 1 else str(p))

        if max_exp > 0:
            msm *= (p ** max_exp)
            msm_factores.append(f"{p}^{max_exp}" if max_exp > 1 else str(p))

        tabla_comparativa.append({
            "primo": p,
            "exp_a": exp_a,
            "exp_b": exp_b,
            "comun": "Sí" if es_comun else "No",
            "exp_msd": min_exp,
            "exp_msm": max_exp,
        })

    str_factores_a = " \\times ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factores_a.items()]) or "1"
    str_factores_b = " \\times ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factores_b.items()]) or "1"

    str_msd = " \\times ".join(msd_factores) if msd_factores else "1"
    str_msm = " \\times ".join(msm_factores) if msm_factores else "1"

    return {
        "factores_a": factores_a,
        "pasos_a": pasos_a,
        "str_a": str_factores_a,
        "factores_b": factores_b,
        "pasos_b": pasos_b,
        "str_b": str_factores_b,
        "tabla_comparativa": tabla_comparativa,
        "msd": msd,
        "str_msd": str_msd,
        "msm": msm,
        "str_msm": str_msm,
    }
