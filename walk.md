# Matemática Discreta — Guía de Recorrido de la Aplicación

¡La aplicación interactiva en Python (Streamlit) cuenta con todos los módulos implementados y verificados!

---

## ¿Cómo abrir y ejecutar el proyecto?

1. Abre tu terminal y navega hasta la carpeta del proyecto.
2. Asegúrate de tener instaladas las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## Módulos de la Aplicación

### 1. 📊 Permutaciones y Combinaciones
- Permite calcular Permutaciones $P(n, r)$ y Combinaciones $C(n, r)$.
- Manejo exacto de factoriales mediante enteros de precisión arbitraria en Python.
- Muestra el procedimiento detallado paso a paso con fórmulas en LaTeX y desglose de factoriales.

### 2. ✖️ Producto Cartesiano
- Admite de 2 a 10 conjuntos ($A, B, C, \dots$).
- Permite ingresar elementos separados por comas y genera todas las tuplas resultantes.
- Despliega la métrica de total de tuplas, formato matemático en bloque de código y lista desplegable.

### 3. ⭕ Diagrama de Venn (2 y 3 Conjuntos)
- Soporta tanto 2 como 3 conjuntos con su Universo y Complemento.
- Permite seleccionar cualquier término como **Incógnita**, despejándola automáticamente mediante la fórmula de Inclusión-Exclusión.
- Renderizado gráfico visual en Matplotlib con regiones exclusivas calculadas y operaciones adicionales (Unión, Intersección, Complementos, Diferencias).

### 4. 🗺️ Estimación de Ruta en Grafos *(Nuevo)*
- **Ingreso por Matriz:** Edición interactiva directa con `st.data_editor` tipo hoja de cálculo (filas = origen, columnas = destino).
- **Criterios de Optimización:**
  - **Ruta Más Corta:** Algoritmo de Dijkstra paso a paso, mostrando distancias tentativas y predecesores.
  - **Ruta Más Larga:** Búsqueda exhaustiva de caminos simples máximos (evitando ciclos infinitos) y detección de redes acíclicas (DAG / Ruta Crítica PERT-CPM).
- **Tipo de Red:** Dirigida (Dígrafo) o No Dirigida (Bidireccional).
- **Visualización Gráfica:** Renderizado de la red con NetworkX y Matplotlib con nodos y aristas de la ruta destacados en verde esmeralda o ámbar.
- **Plantillas Predefinidas:** Botones rápidos para cargar redes de 4, 5 y 6 nodos o limpiar la matriz.

### 5. 🔢 Cálculo de MSM y MSD (MCM y MCD) *(Nuevo)*
- Entrada de 2 números enteros positivos $a$ y $b$.
- **Método 1 (Por Algoritmo):**
  - **MSD / MCD:** Algoritmo de Euclides con divisiones sucesivas completas ($a = b \cdot q + r$).
  - **MSM / MCM:** Relación Fundamental $\text{MSM}(a, b) = \frac{a \times b}{\text{MSD}(a, b)}$ con sustitución paso a paso.
- **Método 2 (Por Descomposición en Factores Primos):**
  - Factorización individual en potencias de primos con tabla vertical de divisiones.
  - Tabla comparativa de factores primos y exponentes ($\min$ para MSD, $\max$ para MSM).
  - Tabla tradicional de **factorización simultánea conjunta**, resaltando los factores que dividen a ambos simultáneamente.
- **Comprobación:** Verificación automática de la identidad $a \cdot b = \text{MSD} \cdot \text{MSM}$.