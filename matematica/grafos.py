"""
Módulo de Teoría de Grafos y Estimación de Rutas para Matemática Discreta.

Funcionalidades:
- Búsqueda de Ruta Más Corta (Algoritmo de Dijkstra paso a paso).
- Búsqueda de Ruta Más Larga (Camino simple de peso máximo con DFS y análisis de DAG).
- Generación de visualizaciones gráficas profesionales con NetworkX y Matplotlib.
- Validación y manipulación de matrices de adyacencia/costos.
"""

from typing import List, Tuple, Dict, Any, Optional, Union
import networkx as nx
import matplotlib.pyplot as plt


def construir_grafo_desde_matriz(
    matriz: List[List[float]],
    nombres_nodos: List[str],
    es_dirigido: bool = True,
) -> Union[nx.DiGraph, nx.Graph]:
    """
    Construye un grafo de NetworkX a partir de una matriz de adyacencia de costos.
    Los valores > 0 representan aristas con su respectivo peso.
    """
    G = nx.DiGraph() if es_dirigido else nx.Graph()
    n = len(nombres_nodos)

    for nodo in nombres_nodos:
        G.add_node(nodo)

    for i in range(n):
        for j in range(n):
            if i == j and not es_dirigido:
                continue
            peso = float(matriz[i][j])
            if peso > 0:
                G.add_edge(nombres_nodos[i], nombres_nodos[j], weight=peso)

    return G


def dijkstra_paso_a_paso(
    matriz: List[List[float]],
    nombres_nodos: List[str],
    origen: str,
    destino: str,
    es_dirigido: bool = True,
) -> Dict[str, Any]:
    """
    Ejecuta el algoritmo de Dijkstra paso a paso para hallar la ruta más corta.
    Retorna la ruta óptima, costo total, tabla de iteraciones y reporte detallado.
    """
    n = len(nombres_nodos)
    idx_map = {nombre: i for i, nombre in enumerate(nombres_nodos)}

    if origen not in idx_map or destino not in idx_map:
        raise ValueError("Los nodos de origen y destino deben estar en la lista de nodos.")

    s = idx_map[origen]
    t = idx_map[destino]

    if s == t:
        return {
            "distancia": 0.0,
            "ruta": [origen],
            "aristas_ruta": [],
            "pasos": f"El nodo de origen **{origen}** es idéntico al nodo de destino. Distancia = 0.",
            "tabla_iteraciones": [],
            "encontrada": True,
        }

    # Inicialización
    INF = float("inf")
    dist = [INF] * n
    pred = [None] * n
    visitados = [False] * n

    dist[s] = 0.0

    tabla_iteraciones = []
    paso_num = 1

    # Registro de paso 0 (estado inicial)
    tabla_iteraciones.append({
        "paso": 0,
        "nodo_actual": "-",
        "accion": f"Inicialización: distancia a {origen} = 0, demás nodos = ∞",
        "distancias": {nombres_nodos[i]: (dist[i] if dist[i] != INF else "∞") for i in range(n)},
        "predecesores": {nombres_nodos[i]: ("-" if pred[i] is None else nombres_nodos[pred[i]]) for i in range(n)},
    })

    while True:
        # Seleccionar nodo no visitado con menor distancia
        u = -1
        min_d = INF
        for i in range(n):
            if not visitados[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i

        if u == -1 or min_d == INF:
            # No hay más nodos alcanzables
            break

        visitados[u] = True
        u_nombre = nombres_nodos[u]

        # Si llegamos al destino, registramos y podemos detenernos
        if u == t:
            tabla_iteraciones.append({
                "paso": paso_num,
                "nodo_actual": u_nombre,
                "accion": f"Se alcanzó el nodo destino {destino} con distancia mínima {min_d:g}",
                "distancias": {nombres_nodos[i]: (dist[i] if dist[i] != INF else "∞") for i in range(n)},
                "predecesores": {nombres_nodos[i]: ("-" if pred[i] is None else nombres_nodos[pred[i]]) for i in range(n)},
            })
            break

        # Relajar aristas salientes de u
        relajaciones = []
        for v in range(n):
            if visitados[v]:
                continue

            peso = float(matriz[u][v])
            if peso > 0:
                if dist[u] + peso < dist[v]:
                    dist_anterior = dist[v]
                    dist[v] = dist[u] + peso
                    pred[v] = u
                    v_nombre = nombres_nodos[v]
                    relajaciones.append(
                        f"Actualiza d({v_nombre}): {('∞' if dist_anterior == INF else f'{dist_anterior:g}')} ➔ {dist[v]:g} vía {u_nombre}"
                    )

        accion_str = f"Explora vecinos de {u_nombre}."
        if relajaciones:
            accion_str += " " + "; ".join(relajaciones)
        else:
            accion_str += " No hubo mejoras en las distancias."

        tabla_iteraciones.append({
            "paso": paso_num,
            "nodo_actual": u_nombre,
            "accion": accion_str,
            "distancias": {nombres_nodos[i]: (dist[i] if dist[i] != INF else "∞") for i in range(n)},
            "predecesores": {nombres_nodos[i]: ("-" if pred[i] is None else nombres_nodos[pred[i]]) for i in range(n)},
        })
        paso_num += 1

    # Reconstrucción de la ruta
    if dist[t] == INF:
        return {
            "distancia": INF,
            "ruta": [],
            "aristas_ruta": [],
            "pasos": f"⚠️ No existe ninguna ruta factible desde **{origen}** hacia **{destino}**.",
            "tabla_iteraciones": tabla_iteraciones,
            "encontrada": False,
        }

    ruta_indices = []
    curr = t
    while curr is not None:
        ruta_indices.append(curr)
        curr = pred[curr]
    ruta_indices.reverse()

    ruta = [nombres_nodos[i] for i in ruta_indices]
    aristas_ruta = []
    for k in range(len(ruta) - 1):
        u_idx = ruta_indices[k]
        v_idx = ruta_indices[k + 1]
        aristas_ruta.append((ruta[k], ruta[k + 1], float(matriz[u_idx][v_idx])))

    # Generar explicación Markdown
    pasos_md = f"### 🟢 Ruta Más Corta — Algoritmo de Dijkstra\n\n"
    pasos_md += f"- **Origen:** `{origen}` | **Destino:** `{destino}`\n"
    pasos_md += f"- **Distancia mínima total:** `{dist[t]:g}`\n"
    pasos_md += f"- **Secuencia óptima:** " + " ➔ ".join([f"`{nodo}`" for nodo in ruta]) + "\n\n"

    pasos_md += "#### Desglose de tramos:\n"
    for idx, (u_nom, v_nom, w) in enumerate(aristas_ruta, 1):
        pasos_md += f"{idx}. Arista `{u_nom}` ➔ `{v_nom}`: costo = `{w:g}`\n"

    return {
        "distancia": dist[t],
        "ruta": ruta,
        "aristas_ruta": aristas_ruta,
        "pasos": pasos_md,
        "tabla_iteraciones": tabla_iteraciones,
        "encontrada": True,
    }


def camino_mas_largo_paso_a_paso(
    matriz: List[List[float]],
    nombres_nodos: List[str],
    origen: str,
    destino: str,
    es_dirigido: bool = True,
) -> Dict[str, Any]:
    """
    Encuentra el camino simple (sin repetir vértices) de mayor longitud/peso
    entre origen y destino mediante búsqueda exhaustiva en profundidad (DFS con backtracking).
    Verifica también si el grafo es un DAG (Grafo Acíclico Dirigido).
    """
    n = len(nombres_nodos)
    idx_map = {nombre: i for i, nombre in enumerate(nombres_nodos)}

    if origen not in idx_map or destino not in idx_map:
        raise ValueError("Los nodos de origen y destino deben estar en la lista de nodos.")

    s = idx_map[origen]
    t = idx_map[destino]

    if s == t:
        return {
            "distancia": 0.0,
            "ruta": [origen],
            "aristas_ruta": [],
            "pasos": f"El nodo de origen **{origen}** es idéntico al destino. Distancia = 0.",
            "todos_los_caminos": [{"ruta": [origen], "peso": 0.0}],
            "es_dag": True,
            "encontrada": True,
        }

    G = construir_grafo_desde_matriz(matriz, nombres_nodos, es_dirigido)
    es_dag = nx.is_directed_acyclic_graph(G) if es_dirigido else False

    # Búsqueda de todos los caminos simples
    todos_los_caminos = []
    visitados = [False] * n

    def dfs(u: int, camino_actual: List[int], peso_acumulado: float):
        if u == t:
            ruta_nombres = [nombres_nodos[x] for x in camino_actual]
            todos_los_caminos.append({
                "ruta": ruta_nombres,
                "peso": peso_acumulado,
            })
            return

        visitados[u] = True
        for v in range(n):
            if not visitados[v]:
                peso = float(matriz[u][v])
                if peso > 0:
                    camino_actual.append(v)
                    dfs(v, camino_actual, peso_acumulado + peso)
                    camino_actual.pop()
        visitados[u] = False

    dfs(s, [s], 0.0)

    if not todos_los_caminos:
        return {
            "distancia": float("-inf"),
            "ruta": [],
            "aristas_ruta": [],
            "pasos": f"⚠️ No existe ningún camino entre **{origen}** y **{destino}**.",
            "todos_los_caminos": [],
            "es_dag": es_dag,
            "encontrada": False,
        }

    # Ordenar caminos de mayor a menor peso
    todos_los_caminos.sort(key=lambda x: x["peso"], reverse=True)
    mejor = todos_los_caminos[0]

    ruta = mejor["ruta"]
    distancia = mejor["peso"]

    aristas_ruta = []
    for k in range(len(ruta) - 1):
        u_idx = idx_map[ruta[k]]
        v_idx = idx_map[ruta[k + 1]]
        aristas_ruta.append((ruta[k], ruta[k + 1], float(matriz[u_idx][v_idx])))

    pasos_md = f"### 🔴 Ruta Más Larga — Búsqueda de Camino Simple Máximo\n\n"
    pasos_md += f"- **Origen:** `{origen}` | **Destino:** `{destino}`\n"
    pasos_md += f"- **Distancia máxima acumulada:** `{distancia:g}`\n"
    pasos_md += f"- **Secuencia óptima:** " + " ➔ ".join([f"`{nodo}`" for nodo in ruta]) + "\n\n"

    if es_dag:
        pasos_md += "💡 *El grafo es un **DAG (Grafo Acíclico Dirigido)**. En teoría de redes y gestión de proyectos (PERT/CPM), este camino corresponde a la **Ruta Crítica**, determinando la duración máxima del proyecto.*\n\n"
    else:
        pasos_md += "ℹ️ *El grafo contiene posibles ciclos o es no dirigido; por definición rigurosa en teoría de grafos, se calculó el **camino simple** de peso máximo (evitando ciclos infinitos).*\n\n"

    pasos_md += "#### Desglose de tramos de la ruta más larga:\n"
    for idx, (u_nom, v_nom, w) in enumerate(aristas_ruta, 1):
        pasos_md += f"{idx}. Arista `{u_nom}` ➔ `{v_nom}`: costo = `{w:g}`\n"

    return {
        "distancia": distancia,
        "ruta": ruta,
        "aristas_ruta": aristas_ruta,
        "pasos": pasos_md,
        "todos_los_caminos": todos_los_caminos,
        "es_dag": es_dag,
        "encontrada": True,
    }


def generar_figura_grafo(
    matriz: List[List[float]],
    nombres_nodos: List[str],
    ruta_destacada: Optional[List[str]] = None,
    es_dirigido: bool = True,
    es_mas_larga: bool = False,
) -> plt.Figure:
    """
    Renderiza una figura de Matplotlib con el grafo, destacando la ruta óptima.
    Estética oscura moderna premium, compatible con la paleta de Streamlit.
    """
    G = construir_grafo_desde_matriz(matriz, nombres_nodos, es_dirigido)
    fig, ax = plt.subplots(figsize=(8.5, 6.0))

    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    if len(nombres_nodos) == 0:
        return fig

    # Disposición de los nodos
    if len(nombres_nodos) <= 4:
        pos = nx.circular_layout(G)
    else:
        try:
            pos = nx.kamada_kawai_layout(G)
        except Exception:
            pos = nx.spring_layout(G, seed=42, k=1.2)

    # Identificar aristas de la ruta
    aristas_ruta_set = set()
    if ruta_destacada and len(ruta_destacada) > 1:
        for k in range(len(ruta_destacada) - 1):
            aristas_ruta_set.add((ruta_destacada[k], ruta_destacada[k + 1]))
            if not es_dirigido:
                aristas_ruta_set.add((ruta_destacada[k + 1], ruta_destacada[k]))

    nodos_ruta_set = set(ruta_destacada) if ruta_destacada else set()

    color_destacado = "#F59E0B" if es_mas_larga else "#10B981"  # Ámbar o Esmeralda
    color_borde_destacado = "#FDE68A" if es_mas_larga else "#A7F3D0"

    # Separar aristas en normales y de ruta
    aristas_normales = [e for e in G.edges() if (e[0], e[1]) not in aristas_ruta_set]
    aristas_optimas = [e for e in G.edges() if (e[0], e[1]) in aristas_ruta_set]

    # Dibujar aristas normales
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=aristas_normales,
        ax=ax,
        edge_color="#4B5563",
        width=1.5,
        alpha=0.6,
        arrows=es_dirigido,
        arrowsize=16 if es_dirigido else 10,
        arrowstyle="-|>",
        connectionstyle="arc3,rad=0.08" if es_dirigido else "arc3,rad=0",
    )

    # Dibujar aristas óptimas
    if aristas_optimas:
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=aristas_optimas,
            ax=ax,
            edge_color=color_destacado,
            width=3.8,
            alpha=0.95,
            arrows=es_dirigido,
            arrowsize=22 if es_dirigido else 10,
            arrowstyle="-|>",
            connectionstyle="arc3,rad=0.08" if es_dirigido else "arc3,rad=0",
        )

    # Dibujar nodos normales y destacados
    nodos_normales = [n for n in G.nodes() if n not in nodos_ruta_set]
    nodos_optimos = [n for n in G.nodes() if n in nodos_ruta_set]

    if nodos_normales:
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=nodos_normales,
            ax=ax,
            node_color="#1E293B",
            edgecolors="#64748B",
            linewidths=2.0,
            node_size=850,
        )

    if nodos_optimos:
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=nodos_optimos,
            ax=ax,
            node_color=color_destacado,
            edgecolors=color_borde_destacado,
            linewidths=3.0,
            node_size=1050,
        )

    # Etiquetas de nodos
    labels_normales = {n: n for n in nodos_normales}
    labels_optimos = {n: n for n in nodos_optimos}

    if labels_normales:
        nx.draw_networkx_labels(
            G,
            pos,
            labels=labels_normales,
            ax=ax,
            font_color="#E2E8F0",
            font_size=11,
            font_family="sans-serif",
            font_weight="bold",
        )

    if labels_optimos:
        nx.draw_networkx_labels(
            G,
            pos,
            labels=labels_optimos,
            ax=ax,
            font_color="#0F172A",
            font_size=12,
            font_family="sans-serif",
            font_weight="heavy",
        )

    # Etiquetas de pesos en las aristas
    edge_labels = {(u, v): f"{d['weight']:g}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        ax=ax,
        font_color="#CBD5E1",
        font_size=9,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#111827", edgecolor="#374151", alpha=0.85),
    )

    ax.axis("off")
    plt.tight_layout()
    return fig
