# Proyecto HPC: Procesamiento Secuencial y Paralelo

## Descripción

Este proyecto tiene como objetivo comparar el rendimiento de un procesamiento **secuencial** frente a un procesamiento **paralelo** utilizando Python.

Se procesan 1,000,000 de datos y se comparan los tiempos de ejecución para analizar la mejora obtenida mediante el uso de múltiples procesos.

## Estructura del proyecto

```text
proyecto-hpc/
├── src/
│   ├── secuencial.py
│   ├── paralelo.py
│   └── benchmark.py
├── resultados/
│   └── benchmark.txt
├── tests/
└── .gitignore
```

## Procesamiento secuencial

El archivo `src/secuencial.py` realiza el procesamiento utilizando un único proceso.

Para ejecutarlo:

```bash
python3 src/secuencial.py
```

## Procesamiento paralelo

El archivo `src/paralelo.py` utiliza múltiples procesos para realizar el procesamiento de manera paralela.

Para ejecutarlo:

```bash
python3 src/paralelo.py
```

La implementación utiliza 8 procesos.

## Benchmark

El archivo `src/benchmark.py` ejecuta varias veces los programas secuencial y paralelo y calcula:

* Tiempo promedio secuencial.
* Tiempo promedio paralelo.
* Speedup.
* Número de procesos.
* Eficiencia.

Para ejecutar el benchmark:

```bash
python3 src/benchmark.py
```

También se puede guardar el resultado en un archivo:

```bash
python3 src/benchmark.py | tee resultados/benchmark.txt
```

## Resultados

Una de las ejecuciones del benchmark produjo los siguientes resultados:

```text
=== BENCHMARK HPC ===
Promedio secuencial: 0.294197 segundos
Promedio paralelo:   0.200741 segundos
Speedup:             1.4656
Procesos:            8
Eficiencia:         0.1832
Eficiencia (%):      18.32%
```

El procesamiento paralelo obtuvo un tiempo menor que el procesamiento secuencial en esta ejecución.

El speedup fue de aproximadamente **1.47**, utilizando 8 procesos.

## Requisitos

* Python 3
* Módulos estándar de Python utilizados por el proyecto.

## Ejecución

Se recomienda utilizar un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Después se pueden ejecutar los programas:

```bash
python3 src/secuencial.py
python3 src/paralelo.py
python3 src/benchmark.py
```

## Control de versiones

El proyecto utiliza Git para el control de versiones.

La implementación paralela se desarrolla en la rama:

```text
feature/paralelo
```
