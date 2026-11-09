# AD_ATV-1

Repositorio de la actividad de Analítica de Datos.

## Estructura del proyecto

- `src/clases_po/`: clases para cargar datos desde Hugging Face y generar reportes.
- `src/sincronicas/`: notebook de la actividad, datos y reportes generados.
- `requirements.txt`: dependencias del proyecto.
- `.github/workflows/`: flujo de trabajo automatizado de GitHub Actions.


## Evolución y desarrollo del proyecto

### 1. Reutilización de la estructura inicial

Para iniciar la actividad, se tomó como base la estructura de código disponible en el repositorio. A partir de ella, se revisaron y reutilizaron los componentes que podían servir para cumplir los requisitos de la actividad de analítica de datos.

Se mantuvo la organización del proyecto en clases de Python, un notebook de Jupyter y archivos de datos y reportes, adaptando sus elementos a las necesidades del nuevo análisis.

### 2. Adaptación de las clases de Python

Se organizaron los componentes principales para separar las responsabilidades del proceso:

- **`HFDatasetLoader` (`src/clases_po/hf_loader.py`):** se utiliza para cargar un dataset de Hugging Face, seleccionar la división correspondiente y obtener los datos en un DataFrame de pandas.
- **`Reportes` (`src/clases_po/reportes.py`):** recibe un DataFrame y genera un resumen textual que incluye dimensiones, nombres y tipos de columnas, valores nulos y estadísticas descriptivas numéricas. También permite guardar el resultado en un archivo `.txt`.

Esta separación facilita la reutilización de las clases y mantiene independiente la carga de datos de la generación de reportes.

### 3. Cambio del conjunto de datos

En la versión inicial del proyecto se trabajaba con archivos relacionados con restaurantes de comida rápida:

- `fast_food_restaurants.csv`
- `fast_food_restaurants.txt`

Posteriormente, se cambió el enfoque del proyecto al análisis del rendimiento estudiantil. Para ello, se seleccionó el dataset [`mstz/student_performance`](https://huggingface.co/datasets/mstz/student_performance), disponible en Hugging Face.

La clase de carga se configuró para utilizar la división `train` del dataset. Los datos obtenidos se convierten en un DataFrame de pandas y se guardan en `src/sincronicas/datos/student_performance.csv`.

Como parte de esta adaptación, se retiraron los archivos del conjunto de datos anterior y se incorporaron los correspondientes al nuevo dataset.

### 4. Actualización del notebook y del reporte

El notebook `src/sincronicas/Semana_1SINC.ipynb` se adaptó para documentar y ejecutar el flujo de trabajo con los datos de rendimiento estudiantil.

El proceso actual incluye:

1. Preparar el entorno e importar las clases del proyecto.
2. Configurar y cargar el dataset de Hugging Face.
3. Crear y examinar el DataFrame obtenido.
4. Generar y visualizar el reporte descriptivo.
5. Guardar el reporte en `src/sincronicas/reportes/student_performance.txt`.

El reporte permite inspeccionar la estructura y la calidad básica de los datos, incluyendo las dimensiones del DataFrame, los tipos de datos, los valores nulos y las estadísticas numéricas.

### 5. Organización actual del proyecto

Los archivos principales utilizados en esta etapa son:

```text
src/
├── clases_po/
│   ├── __init__.py
│   ├── hf_loader.py
│   └── reportes.py
└── sincronicas/
    ├── Semana_1SINC.ipynb
    ├── datos/
    │   └── student_performance.csv
    └── reportes/
        └── student_performance.txt
```

La estructura permite mantener separadas las clases reutilizables, el notebook de ejecución, los datos obtenidos y el reporte generado.

### 6. Control de versiones

Durante el desarrollo se utilizaron commits de Git para registrar avances, integrar los cambios y mantener sincronizado  el repositorio remoto de GitHub.

También se corrigió un conflicto en el archivo del notebook para recuperar su estructura JSON válida y comprobar que pudiera abrirse y ejecutarse correctamente desde VS Code.

### Transformación de datos y generación del reporte

En el notebook `src/sincronicas/Semana_1SINC.ipynb` se coordina el flujo de trabajo entre las clases de carga y generación de reportes.

El proceso consiste en:

1. Obtener desde Hugging Face el conjunto de datos `mstz/student_performance` y cargarlo en un DataFrame de pandas mediante la clase `HFDatasetLoader`.
2. Aplicar una transformación mínima, filtrando los registros cuya puntuación de lectura (`reading_score`) sea mayor o igual a 80.
3. Pasar el DataFrame transformado a la clase `Reportes` para generar el resumen descriptivo.
4. Mostrar el resultado y guardarlo en `src/sincronicas/reportes/student_performance.txt`.

La transformación reduce el conjunto original de 1.000 registros a 261 registros que cumplen la condición del filtro. De esta manera, el reporte generado corresponde a los datos transformados y no al conjunto original completo.

Este flujo demuestra la separación de responsabilidades: la clase de carga obtiene los datos, el notebook realiza la transformación y la clase de reportes genera el resumen en formato `.txt`.