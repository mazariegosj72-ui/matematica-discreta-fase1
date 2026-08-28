# Proyecto Fase 1 - Matemática Discreta (Streamlit Python)

Esta aplicación web resuelve los módulos solicitados de Matemática Discreta utilizando Python y el framework Streamlit para proporcionar una interfaz ágil, reactiva e interactiva.

## Módulos Implementados

1. **Permutaciones y Combinaciones:** Cálculo exacto con factoriales y validación de variables.
2. **Producto Cartesiano:** Manejo de hasta 10 conjuntos y despliegue del listado completo de pares ordenados (tuplas).
3. **Diagrama de Venn (3 Conjuntos):** Cálculo de 9 variables de la Inclusión-Exclusión utilizando variables y el Complemento. Permite dejar cualquiera de estas como "incógnita", calculando su valor y renderizando dinámicamente un gráfico de conjuntos y sus intersecciones.

## Cómo ejecutar de forma local

Requisitos:
- Tener Python 3.9 o superior instalado.
- Opcional pero recomendado: un entorno virtual (venv o conda).

**Instalación:**
```bash
# 1. Clona el repositorio y navega a esta carpeta.
# 2. Instala las dependencias:
pip install -r requirements.txt
```

**Ejecución:**
```bash
streamlit run app.py
```
Se abrirá automáticamente una pestaña en tu navegador con la interfaz gráfica de la aplicación.

## Despliegue en la Nube
El proyecto se encuentra optimizado para ser desplegado utilizando **Streamlit Community Cloud** (share.streamlit.io). El archivo `requirements.txt` ya incluye todas las bibliotecas gráficas necesarias (`streamlit`, `matplotlib`, `matplotlib-venn`) para que el renderizado remoto de los diagramas funcione perfectamente.