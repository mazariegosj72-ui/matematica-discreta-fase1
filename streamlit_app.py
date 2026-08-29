"""
Matemática Discreta — Fase 1
Aplicación Streamlit con 3 módulos: Permutaciones/Combinaciones,
Producto Cartesiano, y Diagrama de Venn.
"""

import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
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
tab_perm, tab_cart, tab_venn = st.tabs(
    [
        "📊 Permutaciones y Combinaciones",
        "✖️ Producto Cartesiano",
        "⭕ Diagrama de Venn",
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
