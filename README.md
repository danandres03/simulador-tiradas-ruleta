# Simulador de Apuestas en la Ruleta

Un proyecto en Python que simula diversas estrategias de apuestas en la ruleta europea (0–36), realiza simulaciones Monte Carlo y ofrece visualizaciones estadísticas detalladas.

---

## Contenido

- [Descripción](#descripción)
- [Características](#características)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Opciones de Estrategia](#opciones-de-estrategia)
- [Visualizaciones y Estadísticas](#visualizaciones-y-estadísticas)
- [Ejemplos de Ejecución](#ejemplos-de-ejecución)
- [Extensiones](#extensiones)
- [Licencia](#licencia)

---

## Descripción

Este simulador permite probar diferentes estrategias de apuestas en la ruleta, comparando su rendimiento mediante:

- Multisimulaciones de Monte Carlo.
- Análisis de trayectoria de balance.
- Estadísticas finales y distribuciones.

## Características

- Simulación de 8 estrategias:
  1. Martingala
  2. Docena
  3. James Bond
  4. D'Alembert
  5. Paroli
  6. Labouchere
  7. Stupid
  8. Fibonacci
- Configuración dinámica de parámetros (balance, apuesta, secuencia, jugadas, simulaciones).
- Gráficas de trayectorias y confianza.
- Cálculos estadísticos con Polars para aprovechar multithreading.

## Estructura del proyecto

```
ruleta_simulator/
├── main.py            # Lógica de menú y bucle de simulaciones
├── ruleta.py          # Clase Ruleta: genera número y color
├── estrategias.py     # Clase Estrategia: implementa todas las estrategias
├── graficos.py        # Funciones de graficación y estadísticos
├── requirements.txt   # Dependencias
└── README.md          # Documentación (este archivo)
```

## Requisitos

- Python 3.8 o superior
- Dependencias (en `requirements.txt`):
  - numpy
  - matplotlib
  - seaborn
  - polars
  - pandas (opcional)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/ruleta_simulator.git
   cd ruleta_simulator
   ```
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el script principal:
```bash
python main.py
```

1. Selecciona la estrategia.
2. Ingresa parámetros (balance, apuesta, secuencia si aplica, número de jugadas y simulaciones).
3. Observa las gráficas y estadísticas generadas.

## Opciones de Estrategia

Cada estrategia ofrece distintos requisitos de entrada:

- **Martingala, D'Alembert, Paroli**: balance, apuesta, apuesta doblada inicial = apuesta.
- **Docena, James Bond, Stupid**: balance, apuesta fija.
- **Labouchere**: secuencia de números (p.ej. `1-2-3-4`), balance inicial = 0.
- **Fibonacci**: apuesta inicial fijo = 2, balance inicial = 0.

## Visualizaciones y Estadísticas

- **Trayectorias individuales**: evolución del balance por simulación.
- **Banda de confianza**: media y percentiles 10%/90% usando Polars.
- **Histograma**: distribución de balances finales.
- **Boxplot/Violinplot**: resumen de estadísticos y colas.
- **Tiempo hasta quiebra**: cuántas tiradas hasta balance ≤ 0.
- **Estadísticos finales**: media, mediana, varianza, probabilidades de quiebra.

## Ejemplos de Ejecución

```bash
$ python main.py
------ MENÚ PRINCIPAL ------
1. Martingala
2. Docena
... 8. Fibonacci
Otro. Salir
----------------------------
Elija la estrategia: 1
Ingrese el balance: 1000
Ingrese la apuesta: 10
Número de jugadas (-1 para infinito): 100
Número de simulaciones: 50
```

El programa generará:

- Gráfica de 50 trayectorias.
- Estadísticos en consola.
- Gráfica de banda de confianza.

## Extensiones

- Añadir nuevas estrategias: crear método en `Estrategias` y registrar en el menú.
- Exportar resultados a CSV o Excel.
- Integrar interfaz web con Flask o Django.
- Incluir benchmarks de rendimiento.
- Diseñar estrategias propias para simular (números, docenas, par-impar, combinadas...)

## Licencia

Este proyecto está licenciado bajo MIT License. ¡Úsalo y modifícalo libremente!
