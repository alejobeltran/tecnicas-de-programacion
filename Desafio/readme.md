🦠 Análisis de Datos COVID-19 en Colombia
📘 Descripción general

Este programa realiza el análisis y visualización de datos reales de COVID-19 en Colombia, utilizando Python, Pandas y Matplotlib.
Permite explorar información como edades promedio, distribución de contagios por ciudades, comparaciones gráficas y estadísticas generales de recuperación y fallecimiento.

El usuario interactúa a través de un menú en consola, sin necesidad de interfaz gráfica, con una navegación sencilla y mensajes informativos.

🧩 Funcionalidades principales

✅ Carga de datos

Lee una base de datos en formato Excel (.xlsx) ubicada en la carpeta data/.

Realiza limpieza y preprocesamiento automático.

✅ Análisis estadístico

Calcula la media y desviación estándar de la edad de los contagiados.

Interpreta los resultados según el nivel de dispersión de edades.

✅ Filtros y segmentación

Permite obtener listas únicas de municipios y contar casos por ciudad.

Filtra casos recuperados por año (2020 o 2021) y detecta casos sin recuperación (fallecidos).

✅ Visualización de datos (gráficos con Matplotlib)

Histograma de distribución de edades.

Gráfico de barras por género o ciudad.

Gráfico de dispersión entre dos variables (por ejemplo, edad vs ID del caso).

✅ Interfaz en consola limpia y colorida

Usa colorama para resaltar títulos y mensajes.

Incluye pausas (Presiona ENTER para continuar) y limpieza de pantalla.

▶️ Ejecución

-Coloca el archivo Excel de datos en la carpeta data/.

-Abre una terminal en la carpeta raíz (Desafio/).

-Ejecuta el programa:

python main.py

🧠 Ejemplo de menú

=== ANÁLISIS DE DATOS COVID-19 EN COLOMBIA ===
1. Calcular promedio y desviación de edad
2. Ver cantidad de casos por zona geográfica
3. Aplicar filtros de recuperación y fallecimiento
4. Crear gráficos estadísticos
0. Salir


🏗️ Estructura del proyecto

Desafio/
│
├── main.py                     # Punto de entrada del programa (menú principal)
├── data/
│   └── covid_colombia_100.xlsx # Base de datos con los registros
└── src/
    ├── __init__.py
    ├── carga_datos.py          # Funciones para leer y preparar los datos
    ├── analisis.py             # Cálculos estadísticos y filtros
    ├── graficas.py             # Gráficos con Matplotlib
    └── utilidades.py           # Limpieza de consola

🧾 Licencia

Este proyecto se distribuye bajo licencia MIT, por lo que puedes usarlo, modificarlo y compartirlo libremente citando su origen.

✨ Autor

Alejandro Beltrán Cardona
Estudiante de la Universidad Autónoma de Manizales
Desafio académico: Técnicas de Programación