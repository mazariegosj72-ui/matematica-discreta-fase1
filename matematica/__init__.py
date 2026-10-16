# Paquete de lógica matemática para Matemática Discreta — Fase 1 y extensiones

from .logica_matematica import (
    factorial,
    permutacion,
    combinacion,
    producto_cartesiano,
    resolver_venn,
    resolver_venn_2_conjuntos,
    VARIABLES_VENN,
    VARIABLES_VENN_2,
)

from .grafos import (
    construir_grafo_desde_matriz,
    dijkstra_paso_a_paso,
    camino_mas_largo_paso_a_paso,
    generar_figura_grafo,
)

from .aritmetica import (
    descomponer_factores_primos,
    algoritmo_euclides,
    calcular_msm_algoritmo,
    factorizacion_simultanea,
    comparar_factores_primos,
)
