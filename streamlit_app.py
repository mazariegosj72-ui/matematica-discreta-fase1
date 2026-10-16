"""
Matemática Discreta — Fase 1 y Nuevos Módulos
Aplicación Streamlit con 5 módulos: Permutaciones/Combinaciones,
Producto Cartesiano, Diagrama de Venn, Estimación de Ruta (Grafos),
y Cálculo de MSM/MSD (MCM/MCD).
"""

import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib_venn import venn3, venn2

from matematica.logica_matematica import (
    factorial,
    permutacion,
    combinacion,
    producto_cartesiano,
    resolver_venn,
    resolver_venn_2_conjuntos,
    VARIABLES_VENN,
    VARIABLES_VENN_2,
    dijkstra_paso_a_paso,
    camino_mas_largo_paso_a_paso,
    generar_figura_grafo,
    algoritmo_euclides,
    calcular_msm_algoritmo,
    descomponer_factores_primos,
    comparar_factores_primos,
    factorizacion_simultanea,
)

matplotlib.use("Agg")

# ═══════════════════════════════════════════════════════════════
#  CONFIGURACIÓN DE PÁGINA
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Matemática Discreta — Fase 1",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════
#  CSS PERSONALIZADO
# ═══════════════════════════════════════════════════════════════
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.main-header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2.5rem 1rem 2rem;
    border-radius: 1rem;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.35);
}
.main-header h1 {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 2.4rem;
    margin: 0 0 0.3rem;
}
.main-header p {
    font-family: 'Inter', sans-serif;
    font-size: 1.05rem;
    opacity: 0.9;
    margin: 0;
}

div[data-testid="stMetric"] {
    background: rgba(124, 92, 252, 0.08);
    border: 1px solid rgba(124, 92, 252, 0.25);
    border-radius: 0.75rem;
    padding: 1rem 1.25rem;
}

.footer-text {
    text-align: center;
    opacity: 0.45;
    font-size: 0.85rem;
    padding: 1rem 0 0.5rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════
#  SIDEBAR - INTEGRANTES
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.header("👥 Integrantes")
    st.markdown("""
- **Javier Mazariegos**
  `5990-26-6549`
- **Eduardo Lemus**
  `5990-19-21951`
- **Ximena Arevalo**
  `5990-26-4631`
- **Jose Contreras**
  `5990-26-5958`
- **Guillermo Paredes**
  `5990-26-4134`
    """)

# ═══════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown(
    """
<div class="main-header">
    <h1>🧮 Matemática Discreta</h1>
    <p>Fase 1 — Proyecto Universitario UMG</p>
</div>
""",
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════
#  TABS PRINCIPALES
# ═══════════════════════════════════════════════════════════════
tab_perm, tab_cart, tab_venn, tab_grafos, tab_msm_msd = st.tabs(
    [
        "📊 Permutaciones y Combinaciones",
        "✖️ Producto Cartesiano",
        "⭕ Diagrama de Venn",
        "🗺️ Estimación de Ruta (Grafos)",
        "🔢 MSM y MSD (MCM y MCD)",
    ]
)



# ──────────────────────────────────────────────────────────────
#  TAB 1 — PERMUTACIONES Y COMBINACIONES
# ──────────────────────────────────────────────────────────────
with tab_perm:
    st.subheader("Permutaciones y Combinaciones")

    col_input, col_formula = st.columns([1, 1], gap="large")

    with col_input:
        tipo = st.radio(
            "Tipo de operación:",
            ["Permutación P(n, r)", "Combinación C(n, r)"],
            horizontal=True,
        )

        col_n, col_r = st.columns(2)
        with col_n:
            n = st.number_input(
                "Valor de n (total):", min_value=0, value=5, step=1, key="pc_n"
            )
        with col_r:
            r = st.number_input(
                "Valor de r (selección):", min_value=0, value=3, step=1, key="pc_r"
            )

        calcular_pc = st.button(
            "🔢 Calcular", key="btn_pc", type="primary", use_container_width=True
        )

    with col_formula:
        st.markdown("**Fórmula:**")
        if tipo.startswith("Permutación"):
            st.latex(r"P(n, r) = \frac{n!}{(n - r)!}")
            st.caption("El orden **sí** importa. Sin repetición.")
        else:
            st.latex(r"C(n, r) = \frac{n!}{r! \cdot (n - r)!}")
            st.caption("El orden **no** importa. Sin repetición.")

    if calcular_pc:
        try:
            if tipo.startswith("Permutación"):
                res = permutacion(n, r)
                st.divider()
                st.metric("Resultado", f"P({n}, {r}) = {res:,}")
                st.markdown("**Procedimiento:**")
                nfact = factorial(n)
                nrfact = factorial(n - r)
                st.latex(
                    rf"P({n}, {r}) = \frac{{{n}!}}{{({n} - {r})!}} = "
                    rf"\frac{{{nfact:,}}}{{{nrfact:,}}} = {res:,}"
                )
                with st.expander("📐 Detalle de factoriales"):
                    st.latex(rf"{n}! = {nfact:,}")
                    st.latex(rf"({n} - {r})! = {n - r}! = {nrfact:,}")
            else:
                res = combinacion(n, r)
                st.divider()
                st.metric("Resultado", f"C({n}, {r}) = {res:,}")
                st.markdown("**Procedimiento:**")
                nfact = factorial(n)
                rfact = factorial(r)
                nrfact = factorial(n - r)
                st.latex(
                    rf"C({n}, {r}) = \frac{{{n}!}}{{{r}! \cdot ({n} - {r})!}} = "
                    rf"\frac{{{nfact:,}}}{{{rfact:,} \cdot {nrfact:,}}} = {res:,}"
                )
                with st.expander("📐 Detalle de factoriales"):
                    st.latex(rf"{n}! = {nfact:,}")
                    st.latex(rf"{r}! = {rfact:,}")
                    st.latex(rf"({n} - {r})! = {n - r}! = {nrfact:,}")
        except ValueError as e:
            st.error(f"⚠️ {e}")


# ──────────────────────────────────────────────────────────────
#  TAB 2 — PRODUCTO CARTESIANO
# ──────────────────────────────────────────────────────────────
with tab_cart:
    st.subheader("Producto Cartesiano")
    st.caption(
        "Ingresa los elementos de cada conjunto separados por comas. "
        "Ejemplo: `a, b, c`"
    )

    num_conjuntos = st.slider("Cantidad de conjuntos:", 2, 10, 3, key="num_conj")

    conjuntos_input = []
    cols = st.columns(min(num_conjuntos, 4))

    for i in range(num_conjuntos):
        col_idx = i % min(num_conjuntos, 4)
        with cols[col_idx]:
            label = chr(65 + i)
            elementos = st.text_input(
                f"Conjunto {label}:",
                placeholder="a, b, c",
                key=f"conj_{i}",
            )
            conjuntos_input.append(elementos)

    if st.button(
        "✖️ Calcular Producto Cartesiano",
        key="btn_cart",
        type="primary",
        use_container_width=True,
    ):
        conjuntos = []
        error = False
        for i, texto in enumerate(conjuntos_input):
            if not texto or not texto.strip():
                st.error(f"⚠️ El Conjunto {chr(65 + i)} está vacío.")
                error = True
                break
            elementos = [e.strip() for e in texto.split(",") if e.strip()]
            if not elementos:
                st.error(
                    f"⚠️ El Conjunto {chr(65 + i)} no tiene elementos válidos."
                )
                error = True
                break
            conjuntos.append(elementos)

        if not error:
            try:
                resultado = producto_cartesiano(conjuntos)

                st.divider()

                # Mostrar la operación
                sets_display = " × ".join(
                    f"\\{{{', '.join(c)}\\}}" for c in conjuntos
                )
                st.markdown(f"**Operación:** {sets_display}")
                st.metric("Total de tuplas", f"{len(resultado):,}")

                # Formato del resultado
                formatted = (
                    "{ " + ",  ".join(str(t) for t in resultado) + " }"
                )
                st.code(formatted, language=None)

                with st.expander(f"📋 Lista detallada ({len(resultado)} tuplas)"):
                    for idx, tupla in enumerate(resultado, 1):
                        st.text(f"  {idx}. {tupla}")

            except ValueError as e:
                st.error(f"⚠️ {e}")


# ──────────────────────────────────────────────────────────────
#  TAB 3 — DIAGRAMA DE VENN
# ──────────────────────────────────────────────────────────────
with tab_venn:
    st.subheader("Diagrama de Venn")
    st.caption(
        "Selecciona la variable incógnita y completa los valores conocidos. "
        "El sistema despejará la incógnita usando Inclusión-Exclusión."
    )

    num_conjuntos = st.radio("¿Cuántos conjuntos deseas relacionar?", [2, 3], horizontal=True)

    st.divider()

    dict_vars = VARIABLES_VENN_2 if num_conjuntos == 2 else VARIABLES_VENN

    incognita = st.selectbox(
        "🔍 Variable incógnita (será despejada):",
        list(dict_vars.keys()),
        format_func=lambda x: dict_vars[x],
        key="venn_inc",
    )

    st.divider()

    # ── Inputs ──
    col1, col2, col3 = st.columns(3)

    defaults_2 = {"U": 100, "A": 50, "B": 40, "AnB": 10, "Complemento": 20}
    defaults_3 = {"U": 100, "A": 50, "B": 40, "C": 30, "AnB": 10, "AnC": 8, "BnC": 12, "AnBnC": 5, "Complemento": 5}
    
    defaults = defaults_2 if num_conjuntos == 2 else defaults_3

    layout_2 = [
        (col1, ["U", "A"]),
        (col2, ["B", "AnB"]),
        (col3, ["Complemento"]),
    ]
    layout_3 = [
        (col1, ["U", "A", "B"]),
        (col2, ["C", "AnB", "AnC"]),
        (col3, ["BnC", "AnBnC", "Complemento"]),
    ]
    
    layout = layout_2 if num_conjuntos == 2 else layout_3

    valores = {}
    for col, var_keys in layout:
        with col:
            for var_key in var_keys:
                if var_key == incognita:
                    st.markdown(f"**🔍 {dict_vars[var_key]}** — *Incógnita*")
                    st.info("¿? — Será calculada")
                    valores[var_key] = 0
                else:
                    valores[var_key] = st.number_input(
                        dict_vars[var_key],
                        min_value=0,
                        value=defaults[var_key],
                        step=1,
                        key=f"venn_{var_key}_{num_conjuntos}",
                    )

    if st.button(
        "🧮 Despejar Incógnita",
        key="btn_venn",
        type="primary",
        use_container_width=True,
    ):
        if num_conjuntos == 2:
            resultado, pasos, regiones = resolver_venn_2_conjuntos(
                U=valores["U"], A=valores["A"], B=valores["B"],
                AnB=valores["AnB"], Complemento=valores["Complemento"],
                incognita=incognita
            )
        else:
            resultado, pasos, regiones = resolver_venn(
                U=valores["U"], A=valores["A"], B=valores["B"], C=valores["C"],
                AnB=valores["AnB"], AnC=valores["AnC"], BnC=valores["BnC"], AnBnC=valores["AnBnC"],
                Complemento=valores["Complemento"], incognita=incognita
            )

        st.divider()

        col_sol, col_diag = st.columns([1, 1], gap="large")

        # ── Columna izquierda: solución paso a paso ──
        with col_sol:
            st.markdown("### 📝 Solución paso a paso")
            st.markdown(pasos)

            if resultado < 0:
                st.warning(
                    "⚠️ El resultado es negativo. Esto indica que "
                    "los datos ingresados son matemáticamente inconsistentes."
                )

        # ── Columna derecha: diagrama de Venn visual ──
        with col_diag:
            st.markdown("### 📊 Diagrama de Venn")

            has_negative = any(v < 0 for v in regiones.values())

            fig, ax = plt.subplots(figsize=(7, 5.5))
            fig.patch.set_facecolor("#0E1117")
            ax.set_facecolor("#0E1117")

            if num_conjuntos == 2:
                subset_values = (1, 1, 1)
                real_labels = [regiones["solo_A"], regiones["solo_B"], regiones["AB"]]
                v = venn2(subsets=subset_values, set_labels=("A", "B"), ax=ax)
            else:
                subset_values = (1, 1, 1, 1, 1, 1, 1)
                real_labels = [
                    regiones["solo_A"], regiones["solo_B"], regiones["solo_AB"],
                    regiones["solo_C"], regiones["solo_AC"], regiones["solo_BC"], regiones["ABC"]
                ]
                v = venn3(subsets=subset_values, set_labels=("A", "B", "C"), ax=ax)

            # Estilizar las regiones
            for patch in v.patches:
                if patch:
                    patch.set_alpha(0.35)
                    patch.set_edgecolor("white")
                    patch.set_linewidth(2)

            # Estilizar las etiquetas de conjuntos
            for label in v.set_labels:
                if label:
                    label.set_color("white")
                    label.set_fontsize(15)
                    label.set_fontweight("bold")

            # Mostrar valores reales en las regiones
            for i, label in enumerate(v.subset_labels):
                if label:
                    label.set_text(str(real_labels[i]))
                    label.set_color("white")
                    label.set_fontsize(11)

            # Universo resuelto
            u_final = valores["U"] if incognita != "U" else resultado
            ax.set_title(
                f"U = {u_final}", color="white", fontsize=14, fontweight="bold", pad=20
            )

            # Complemento
            comp_val = valores["Complemento"] if incognita != "Complemento" else resultado
            ax.text(
                0.95, 0.05, f"Comp = {comp_val}",
                transform=ax.transAxes, color="#c4b5fd", fontsize=11, ha="right", va="bottom",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#1B1F2B", edgecolor="#7C5CFC", alpha=0.9),
            )

            st.pyplot(fig)
            plt.close(fig)

            if has_negative:
                st.warning(
                    "⚠️ Algunas regiones exclusivas son negativas "
                    "(mostradas como valor real). Los datos pueden ser "
                    "inconsistentes para un diagrama de Venn válido."
                )

        st.divider()
        st.markdown("### 🧮 Operaciones de Conjuntos (Resultados Extra)")
        
        # Reconstruir valores finales para los cálculos
        v_final = valores.copy()
        v_final[incognita] = resultado

        col_op1, col_op2 = st.columns(2)
        
        if num_conjuntos == 2:
            with col_op1:
                st.markdown(f"- **Unión ($A \\cup B$):** `{v_final['A'] + v_final['B'] - v_final['AnB']}`")
                st.markdown(f"- **Intersección ($A \\cap B$):** `{v_final['AnB']}`")
                st.markdown(f"- **Complemento de A ($A'$):** `{v_final['U'] - v_final['A']}`")
            with col_op2:
                st.markdown(f"- **Diferencia ($A - B$):** `{regiones['solo_A']}`")
                st.markdown(f"- **Diferencia ($B - A$):** `{regiones['solo_B']}`")
                st.markdown(f"- **Complemento de B ($B'$):** `{v_final['U'] - v_final['B']}`")
        else:
            aubuc = v_final["U"] - v_final["Complemento"]
            with col_op1:
                st.markdown(f"- **Unión ($A \\cup B \\cup C$):** `{aubuc}`")
                st.markdown(f"- **Intersección total ($A \\cap B \\cap C$):** `{v_final['AnBnC']}`")
                st.markdown(f"- **Complemento de A ($A'$):** `{v_final['U'] - v_final['A']}`")
            with col_op2:
                st.markdown(f"- **Diferencia ($A - B$):** `{regiones['solo_A'] + regiones['solo_AC']}`")
                st.markdown(f"- **Diferencia ($B - A$):** `{regiones['solo_B'] + regiones['solo_BC']}`")
                st.markdown(f"- **Complemento de B ($B'$):** `{v_final['U'] - v_final['B']}`")



# ──────────────────────────────────────────────────────────────
#  TAB 4 — ESTIMACIÓN DE RUTA (GRAFOS)
# ──────────────────────────────────────────────────────────────
with tab_grafos:
    st.subheader("🗺️ Estimación de Ruta en Grafos")
    st.caption(
        "Ingresa la matriz de adyacencia y pesos para estimar la **Ruta Más Corta** (Algoritmo de Dijkstra) "
        "o la **Ruta Más Larga** (Camino Simple Máximo / Ruta Crítica PERT-CPM)."
    )

    # Inicializar estado de matriz si no existe
    if "grafo_num_nodos" not in st.session_state:
        st.session_state["grafo_num_nodos"] = 4
    if "grafo_nombres" not in st.session_state:
        st.session_state["grafo_nombres"] = ["A", "B", "C", "D"]
    if "grafo_matriz_df" not in st.session_state:
        df_init = pd.DataFrame(
            [
                [0.0, 2.0, 5.0, 0.0],
                [0.0, 0.0, 1.0, 4.0],
                [0.0, 0.0, 0.0, 2.0],
                [0.0, 0.0, 0.0, 0.0],
            ],
            index=["A", "B", "C", "D"],
            columns=["A", "B", "C", "D"],
        )
        st.session_state["grafo_matriz_df"] = df_init

    # Botones de plantillas de ejemplo
    st.markdown("**⚡ Cargar ejemplos predefinidos:**")
    col_ex1, col_ex2, col_ex3, col_ex4 = st.columns(4)

    def set_matriz(nombres, valores):
        st.session_state["grafo_num_nodos"] = len(nombres)
        st.session_state["grafo_nombres"] = nombres
        st.session_state["grafo_matriz_df"] = pd.DataFrame(
            valores, index=nombres, columns=nombres, dtype=float
        )
        st.rerun()

    with col_ex1:
        if st.button("📋 Red 4 Nodos (Básica)", key="btn_ex1", use_container_width=True):
            set_matriz(
                ["A", "B", "C", "D"],
                [
                    [0.0, 2.0, 5.0, 0.0],
                    [0.0, 0.0, 1.0, 4.0],
                    [0.0, 0.0, 0.0, 2.0],
                    [0.0, 0.0, 0.0, 0.0],
                ],
            )
    with col_ex2:
        if st.button("🚚 Red 5 Nodos (Transporte)", key="btn_ex2", use_container_width=True):
            set_matriz(
                ["A", "B", "C", "D", "E"],
                [
                    [0.0, 4.0, 2.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 5.0, 0.0],
                    [0.0, 0.0, 0.0, 8.0, 10.0],
                    [0.0, 0.0, 0.0, 0.0, 2.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0],
                ],
            )
    with col_ex3:
        if st.button("📈 Red 6 Nodos (Ruta Crítica DAG)", key="btn_ex3", use_container_width=True):
            set_matriz(
                ["A", "B", "C", "D", "E", "F"],
                [
                    [0.0, 3.0, 2.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 4.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0, 5.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 6.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 3.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                ],
            )
    with col_ex4:
        if st.button("🧹 Limpiar Matriz (Ceros)", key="btn_ex_clear", use_container_width=True):
            curr_n = st.session_state["grafo_num_nodos"]
            nombres = [chr(65 + i) for i in range(curr_n)]
            st.session_state["grafo_nombres"] = nombres
            st.session_state["grafo_matriz_df"] = pd.DataFrame(
                0.0, index=nombres, columns=nombres
            )
            st.rerun()

    st.divider()

    # Controles de configuración del grafo
    col_cfg1, col_cfg2, col_cfg3 = st.columns([1, 1, 1])

    with col_cfg1:
        criterio_ruta = st.radio(
            "Criterio de estimación:",
            ["🟢 Ruta más corta (Dijkstra)", "🔴 Ruta más larga (Camino Simple Máximo)"],
            key="radio_criterio_ruta",
        )

    with col_cfg2:
        tipo_grafo = st.radio(
            "Tipo de grafo:",
            ["Grafo Dirigido (Dígrafo)", "Grafo No Dirigido (Bidireccional)"],
            key="radio_tipo_grafo",
        )
        es_dirigido = tipo_grafo.startswith("Grafo Dirigido")

    with col_cfg3:
        nuevo_n = st.slider(
            "Cantidad de nodos en el grafo:",
            min_value=3,
            max_value=8,
            value=st.session_state["grafo_num_nodos"],
            key="slider_num_nodos",
        )
        if nuevo_n != st.session_state["grafo_num_nodos"]:
            nombres_nuevos = [chr(65 + i) for i in range(nuevo_n)]
            df_viejo = st.session_state["grafo_matriz_df"]
            df_nuevo = pd.DataFrame(0.0, index=nombres_nuevos, columns=nombres_nuevos)
            for r in df_viejo.index:
                for c in df_viejo.columns:
                    if r in nombres_nuevos and c in nombres_nuevos:
                        df_nuevo.loc[r, c] = df_viejo.loc[r, c]
            st.session_state["grafo_num_nodos"] = nuevo_n
            st.session_state["grafo_nombres"] = nombres_nuevos
            st.session_state["grafo_matriz_df"] = df_nuevo
            st.rerun()

    nombres_nodos = st.session_state["grafo_nombres"]

    st.markdown("#### 🔢 Matriz de Adyacencia / Costos")
    st.caption(
        "Fila = Nodo Origen, Columna = Nodo Destino. Ingresa el peso o distancia de la arista. "
        "Usa `0` para indicar ausencia de conexión directa."
    )

    matriz_editada = st.data_editor(
        st.session_state["grafo_matriz_df"],
        key="editor_matriz_grafo",
        use_container_width=True,
    )
    st.session_state["grafo_matriz_df"] = matriz_editada

    col_org, col_dst, col_btn = st.columns([1, 1, 1])
    with col_org:
        origen_sel = st.selectbox(
            "Nodo Origen (Inicio):",
            nombres_nodos,
            index=0,
            key="grafo_origen",
        )
    with col_dst:
        destino_sel = st.selectbox(
            "Nodo Destino (Fin):",
            nombres_nodos,
            index=len(nombres_nodos) - 1,
            key="grafo_destino",
        )
    with col_btn:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        calcular_ruta_btn = st.button(
            "🚀 Calcular Estimación de Ruta",
            key="btn_calc_ruta",
            type="primary",
            use_container_width=True,
        )

    if calcular_ruta_btn:
        matriz_vals = matriz_editada.to_numpy().astype(float).tolist()
        n = len(nombres_nodos)

        if not es_dirigido:
            for i in range(n):
                for j in range(n):
                    val_max = max(matriz_vals[i][j], matriz_vals[j][i])
                    matriz_vals[i][j] = val_max
                    matriz_vals[j][i] = val_max

        es_corta = criterio_ruta.startswith("🟢 Ruta más corta")

        if es_corta:
            resultado_ruta = dijkstra_paso_a_paso(
                matriz_vals, nombres_nodos, origen_sel, destino_sel, es_dirigido=es_dirigido
            )
        else:
            resultado_ruta = camino_mas_largo_paso_a_paso(
                matriz_vals, nombres_nodos, origen_sel, destino_sel, es_dirigido=es_dirigido
            )

        st.divider()

        if not resultado_ruta["encontrada"]:
            st.error(resultado_ruta["pasos"])
            fig_err = generar_figura_grafo(
                matriz_vals, nombres_nodos, ruta_destacada=None, es_dirigido=es_dirigido
            )
            st.pyplot(fig_err)
            plt.close(fig_err)
        else:
            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1:
                tipo_txt = "Distancia Mínima" if es_corta else "Distancia Máxima"
                st.metric(tipo_txt, f"{resultado_ruta['distancia']:g}")
            with col_m2:
                st.metric("Ruta Óptima", " ➔ ".join(resultado_ruta["ruta"]))
            with col_m3:
                st.metric("Tramos / Aristas", f"{len(resultado_ruta['aristas_ruta'])}")
            with col_m4:
                if not es_corta:
                    st.metric("¿Es Grafo DAG?", "Sí (Acíclico)" if resultado_ruta.get("es_dag") else "No / Con Ciclos")
                else:
                    st.metric("Algoritmo", "Dijkstra")

            col_viz, col_detalles = st.columns([1.1, 1], gap="large")

            with col_viz:
                st.markdown("### 📊 Visualización del Grafo y Ruta")
                fig_grafo = generar_figura_grafo(
                    matriz_vals,
                    nombres_nodos,
                    ruta_destacada=resultado_ruta["ruta"],
                    es_dirigido=es_dirigido,
                    es_mas_larga=not es_corta,
                )
                st.pyplot(fig_grafo)
                plt.close(fig_grafo)
                st.caption(
                    "🟡/🟢 Los nodos y aristas de la ruta óptima calculada aparecen destacados. "
                    "Las aristas normales se muestran en gris atenuado."
                )

            with col_detalles:
                st.markdown(resultado_ruta["pasos"])

                if es_corta:
                    with st.expander("📝 Tabla de Iteraciones de Dijkstra (Paso a Paso)", expanded=True):
                        filas_tabla = []
                        for fila in resultado_ruta["tabla_iteraciones"]:
                            dists_str = ", ".join([f"{k}:{v}" for k, v in fila["distancias"].items()])
                            preds_str = ", ".join([f"{k}←{v}" for k, v in fila["predecesores"].items() if v != "-"])
                            filas_tabla.append({
                                "Paso": fila["paso"],
                                "Nodo": fila["nodo_actual"],
                                "Acción / Relajación": fila["accion"],
                                "Distancias": dists_str,
                                "Predecesores": preds_str or "-",
                            })
                        st.dataframe(pd.DataFrame(filas_tabla), use_container_width=True, hide_index=True)
                else:
                    with st.expander("📋 Comparativa de Todos los Caminos Simples Evaluados", expanded=True):
                        caminos_df = []
                        for idx, item in enumerate(resultado_ruta["todos_los_caminos"], 1):
                            es_ganador = "🏆 (MÁS LARGO)" if idx == 1 else ""
                            caminos_df.append({
                                "N°": idx,
                                "Camino": " ➔ ".join(item["ruta"]),
                                "Distancia Acumulada": f"{item['peso']:g}",
                                "Estado": es_ganador or "Alternativa",
                            })
                        st.dataframe(pd.DataFrame(caminos_df), use_container_width=True, hide_index=True)


# ──────────────────────────────────────────────────────────────
#  TAB 5 — MSM Y MSD (MCM Y MCD)
# ──────────────────────────────────────────────────────────────
with tab_msm_msd:
    st.subheader("🔢 Cálculo de MSM y MSD (MCM y MCD)")
    st.caption(
        "Cálculo del **MSD** (Máximo Sub-Divisor / MCD) y del **MSM** (Mínimo Sub-Múltiplo / MCM) "
        "para dos números enteros positivos. Permite trabajar por **Algoritmo de Euclides** "
        "o por **Descomposición en Factores Primos**."
    )

    col_in_a, col_in_b, col_in_met = st.columns([1, 1, 1.2])

    with col_in_a:
        num_a = st.number_input(
            "Primer número (a):",
            min_value=1,
            value=48,
            step=1,
            key="input_num_a",
        )
    with col_in_b:
        num_b = st.number_input(
            "Segundo número (b):",
            min_value=1,
            value=18,
            step=1,
            key="input_num_b",
        )
    with col_in_met:
        metodo_calc = st.radio(
            "Método de trabajo:",
            [
                "⚙️ Por Algoritmo (Euclides y Relación Fundamental)",
                "🌲 Por Descomposición en Factores Primos",
                "🌟 Ambos Métodos (Comparativa Completa)",
            ],
            key="radio_metodo_msm_msd",
        )

    btn_calc_msm_msd = st.button(
        "🧮 Calcular MSM y MSD",
        key="btn_calc_msm_msd",
        type="primary",
        use_container_width=True,
    )

    if btn_calc_msm_msd:
        mcd_val, pasos_euclides = algoritmo_euclides(num_a, num_b)
        msm_val, exp_msm = calcular_msm_algoritmo(num_a, num_b, mcd_val)
        comp_factores = comparar_factores_primos(num_a, num_b)
        filas_sim, sim_msd, sim_msm = factorizacion_simultanea(num_a, num_b)

        st.divider()

        # Métricas principales
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric("MSD / MCD (Máximo Divisor)", f"{mcd_val:,}")
            st.caption("Mayor número entero que divide exactamente a ambos.")
        with col_res2:
            st.metric("MSM / MCM (Mínimo Múltiplo)", f"{msm_val:,}")
            st.caption("Menor número positivo que es múltiplo de ambos.")
        with col_res3:
            prod_ab = num_a * num_b
            prod_ms = mcd_val * msm_val
            st.metric("Comprobación (a × b)", f"{prod_ab:,}")
            st.caption(f"MSD × MSM = {mcd_val} × {msm_val} = {prod_ms}")

        st.divider()

        mostrar_algoritmo = ("Por Algoritmo" in metodo_calc) or ("Ambos" in metodo_calc)
        mostrar_factores = ("Factores Primos" in metodo_calc) or ("Ambos" in metodo_calc)

        # ── SECCIÓN 1: MÉTODO POR ALGORITMO ──
        if mostrar_algoritmo:
            st.markdown("### ⚙️ Método 1: Por Algoritmo")
            st.markdown(
                "En matemática discreta, el **Algoritmo de Euclides** es el procedimiento algorítmico fundamental "
                "para calcular el MCD mediante divisiones sucesivas. Posteriormente, el MSM se obtiene mediante la "
                "**Relación Fundamental** entre MCD y MCM."
            )

            col_euc1, col_euc2 = st.columns([1.2, 1], gap="large")

            with col_euc1:
                st.markdown("#### 1.1 Algoritmo de Euclides (Divisiones Sucesivas para MSD)")
                st.markdown(
                    "Teorema: $\\text{mcd}(a, b) = \\text{mcd}(b, r)$, donde $a = b \\cdot q + r$. "
                    "El algoritmo finaliza cuando el residuo es 0; el último residuo no nulo es el **MSD**."
                )

                df_euclides = pd.DataFrame([
                    {
                        "Paso": f["paso"],
                        "Dividendo (a)": f["dividendo"],
                        "Divisor (b)": f["divisor"],
                        "Cociente (q)": f["cociente"],
                        "Residuo (r)": f["residuo"],
                        "Ecuación": f"{f['dividendo']} = {f['divisor']} × {f['cociente']} + {f['residuo']}",
                    }
                    for f in pasos_euclides
                ])
                st.dataframe(df_euclides, use_container_width=True, hide_index=True)

                st.success(f"✅ **Último residuo no nulo:** `{mcd_val}` ➔ **MSD({num_a}, {num_b}) = {mcd_val}**")

            with col_euc2:
                st.markdown("#### 1.2 Relación Fundamental (Algoritmo para MSM)")
                st.markdown(
                    "Se aplica la propiedad que relaciona el producto de dos números con su MCD y MCM: "
                    "$$\\text{MSM}(a, b) \\times \\text{MSD}(a, b) = a \\times b$$"
                )
                st.markdown("Despejando el MSM:")
                st.latex(rf"\text{{MSM}}({num_a}, {num_b}) = \frac{{{num_a} \times {num_b}}}{{\text{{MSD}}({num_a}, {num_b})}}")
                st.latex(rf"\text{{MSM}}({num_a}, {num_b}) = \frac{{{num_a * num_b:,}}}{{{mcd_val}}} = {msm_val:,}")
                st.info(f"🎯 **Resultado:** **MSM({num_a}, {num_b}) = {msm_val:,}**")

            if mostrar_factores:
                st.divider()

        # ── SECCIÓN 2: MÉTODO POR FACTORES PRIMOS ──
        if mostrar_factores:
            st.markdown("### 🌲 Método 2: Por Descomposición en Factores Primos")
            st.markdown(
                "Descompone cada número en sus factores primos canónicos. "
                "- Para el **MSD**: Se toman únicamente los factores primos **comunes** con su **menor exponente** ($\\min$).\n"
                "- Para el **MSM**: Se toman todos los factores primos (**comunes y no comunes**) con su **mayor exponente** ($\\max$)."
            )

            col_f1, col_f2 = st.columns(2)

            with col_f1:
                st.markdown(f"**Factorización de a = {num_a}:**")
                st.latex(rf"{num_a} = {comp_factores['str_a']}")
                with st.expander(f"Ver divisiones sucesivas de {num_a}"):
                    df_pa = pd.DataFrame(comp_factores["pasos_a"], columns=["Valor", "Divisor Primo"])
                    st.dataframe(df_pa, use_container_width=True, hide_index=True)

            with col_f2:
                st.markdown(f"**Factorización de b = {num_b}:**")
                st.latex(rf"{num_b} = {comp_factores['str_b']}")
                with st.expander(f"Ver divisiones sucesivas de {num_b}"):
                    df_pb = pd.DataFrame(comp_factores["pasos_b"], columns=["Valor", "Divisor Primo"])
                    st.dataframe(df_pb, use_container_width=True, hide_index=True)

            st.markdown("#### 📊 Tabla Comparativa de Factores y Exponentes")
            df_comp = pd.DataFrame([
                {
                    "Factor Primo (p)": r["primo"],
                    f"Exponente en {num_a}": r["exp_a"],
                    f"Exponente en {num_b}": r["exp_b"],
                    "¿Es Factor Común?": r["comun"],
                    "Exp para MSD (Mínimo)": r["exp_msd"],
                    "Exp para MSM (Máximo)": r["exp_msm"],
                }
                for r in comp_factores["tabla_comparativa"]
            ])
            st.dataframe(df_comp, use_container_width=True, hide_index=True)

            col_calc_msd, col_calc_msm = st.columns(2)
            with col_calc_msd:
                st.markdown("**Cálculo de MSD:**")
                st.latex(rf"\text{{MSD}}({num_a}, {num_b}) = {comp_factores['str_msd']} = {comp_factores['msd']}")
                st.caption("Producto de factores comunes elevados al menor exponente.")
            with col_calc_msm:
                st.markdown("**Cálculo de MSM:**")
                st.latex(rf"\text{{MSM}}({num_a}, {num_b}) = {comp_factores['str_msm']} = {comp_factores['msm']}")
                st.caption("Producto de todos los factores elevados al mayor exponente.")

            st.markdown("#### 📋 Factorización Simultánea Tradicional (Conjunta)")
            st.caption(
                "Disposición escolar tradicional en la que ambos números se dividen simultáneamente por números primos. "
                "Los factores que dividen a ambos al mismo tiempo (resaltados con `✓ Sí (Común)`) son los que conforman el MSD."
            )
            df_sim = pd.DataFrame([
                {
                    f"Número A ({num_a})": fila["a"],
                    f"Número B ({num_b})": fila["b"],
                    "Divisor Primo": fila["primo"],
                    "¿Divide a ambos? (Aporta a MSD)": "✓ Sí (Común)" if fila["divide_ambos"] else ("-" if fila["primo"] == "-" else "No"),
                }
                for fila in filas_sim
            ])
            st.dataframe(df_sim, use_container_width=True, hide_index=True)

        # ── VERIFICACIÓN MATEMÁTICA FINAL ──
        st.divider()
        st.markdown("### 🔍 Identidad y Comprobación Aritmética")
        st.latex(rf"\text{{MSD}}({num_a}, {num_b}) \times \text{{MSM}}({num_a}, {num_b}) = {mcd_val} \times {msm_val} = {mcd_val * msm_val:,}")
        st.latex(rf"{num_a} \times {num_b} = {num_a * num_b:,}")
        if (num_a * num_b) == (mcd_val * msm_val):
            st.success(f"✨ **Comprobación exitosa:** Se cumple la identidad fundamental: {num_a} × {num_b} = {mcd_val} × {msm_val} = {num_a * num_b:,}.")



# ═══════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════
st.divider()
st.markdown(
    '<div class="footer-text">'
    "Matemática Discreta — Fase 1 | Universidad Mariano Gálvez"
    "</div>",
    unsafe_allow_html=True,
)
