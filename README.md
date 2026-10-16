# Proyecto Fase 1 - Matemática Discreta (Streamlit Python)

Esta aplicación web resuelve los módulos de Matemática Discreta utilizando Python y el framework Streamlit para proporcionar una interfaz ágil, reactiva e interactiva.

## Módulos Implementados

1. **Permutaciones y Combinaciones:** Cálculo exacto con factoriales y validación de variables ($n$ y $r$).
2. **Producto Cartesiano:** Manejo de hasta 10 conjuntos y despliegue del listado completo de pares ordenados (tuplas).
3. **Diagrama de Venn (2 y 3 Conjuntos):** Cálculo de variables de la Inclusión-Exclusión utilizando variables y el Complemento. Permite despejar cualquier incógnita y renderizar dinámicamente el diagrama de conjuntos con sus intersecciones.
4. **Estimación de Ruta en Grafos:**
   - **Ingreso mediante Matriz de Adyacencia / Costos:** Editor interactivo tipo hoja de cálculo para definir los pesos entre nodos.
   - **Ruta Más Corta:** Implementación detallada con el **Algoritmo de Dijkstra**, incluyendo tabla paso a paso de distancias tentativas y predecesores.
   - **Ruta Más Larga:** Búsqueda exhaustiva de caminos simples máximos (DFS con backtracking) y detección de redes acíclicas (**DAG / Ruta Crítica PERT-CPM**).
   - **Visualización Gráfica:** Representación de la red con NetworkX y Matplotlib destacando los nodos y aristas de la ruta calculada.
   - **Plantillas Predefinidas:** Carga instantánea de redes de 4, 5 y 6 nodos para demostración rápida.
5. **Cálculo de MSM y MSD (MCM y MCD):**
   - **Por Algoritmo:** Cálculo del MSD mediante el **Algoritmo de Euclides** (divisiones sucesivas detalladas paso a paso) y del MSM mediante la **Relación Fundamental** ($\text{MSM} \times \text{MSD} = a \times b$).
   - **Por Descomposición en Factores Primos:** Factorización individual, tabla comparativa de exponentes ($\min$ para MSD, $\max$ para MSM) y **tabla de factorización simultánea tradicional**.
   - **Comprobación Aritmética:** Verificación de la identidad $a \times b = \text{MSD}(a, b) \times \text{MSM}(a, b)$.

## Cómo ejecutar de forma local

Requisitos:
- Tener Python 3.9 o superior instalado.
- Opcional pero recomendado: un entorno virtual (venv o conda).

**Instalación de dependencias:**
```bash
pip install -r requirements.txt
```

**Ejecución de la aplicación:**
```bash
streamlit run streamlit_app.py
```
Se abrirá automáticamente una pestaña en tu navegador con la interfaz gráfica de la aplicación (`http://localhost:8501`).

## Despliegue en la Nube
El proyecto se encuentra optimizado para ser desplegado en **Streamlit Community Cloud** (share.streamlit.io). El archivo `requirements.txt` incluye todas las dependencias (`streamlit`, `matplotlib`, `matplotlib-venn`, `networkx`, `pandas`) para el correcto funcionamiento en la nube.