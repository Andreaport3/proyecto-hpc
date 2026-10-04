# Proyecto HPC: Procesamiento Secuencial y Paralelo

## Descripción

Este proyecto tiene como objetivo comparar el rendimiento de un procesamiento secuencial frente a un procesamiento paralelo utilizando Python y el módulo `multiprocessing`.

El programa procesa 1,000,000 de datos realizando operaciones matemáticas como raíz cuadrada, potencia, seno, coseno y logaritmo.

El experimento evalúa diferentes cantidades de workers para analizar el comportamiento del procesamiento paralelo y calcular speedup y eficiencia.

## Objetivos

- Implementar una versión secuencial.
- Implementar una versión paralela.
- Medir los tiempos de ejecución.
- Evaluar configuraciones de 1, 2 y 4 workers.
- Realizar tres pruebas para cada configuración.
- Calcular el speedup y la eficiencia.
- Generar una gráfica de workers frente al tiempo de ejecución.
- Analizar los resultados obtenidos desde una perspectiva de cómputo de alto rendimiento.

## Estructura del proyecto

```text
proyecto-hpc/
├── src/
│   ├── secuencial.py
│   ├── paralelo.py
│   └── benchmark.py
├── resultados/
│   ├── benchmark.txt
│   └── workers_vs_tiempo.png
├── .gitignore
└── README.md
## Resultados experimentales

Los resultados obtenidos fueron:

### 1 worker

```text
Prueba 1: 0.558892 segundos
Prueba 2: 0.512074 segundos
Prueba 3: 0.504117 segundos

Promedio: 0.525028 segundos
Speedup: 1.0000
Eficiencia: 100.00%

### 2 worker
Prueba 1: 0.282416 segundos
Prueba 2: 0.282182 segundos
Prueba 3: 0.315486 segundos

Promedio: 0.293361 segundos
Speedup: 1.7897
Eficiencia: 89.48%

### 4 worker
Prueba 1: 0.218313 segundos
Prueba 2: 0.336526 segundos
Prueba 3: 0.257778 segundos

Promedio: 0.257778 segundos
Speedup: 2.0367
Eficiencia: 50.92%
