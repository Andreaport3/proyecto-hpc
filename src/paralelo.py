import math
import time
import multiprocessing
import sys


def calcular(x):
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


def main():
    n = 1_000_000
    datos = range(1, n + 1)

    # Obtener número de workers desde la línea de comandos
    if len(sys.argv) > 1:
        num_procesos = int(sys.argv[1])
    else:
        num_procesos = 1

    # Verificar que el número de workers sea válido
    max_procesos = multiprocessing.cpu_count()

    if num_procesos < 1 or num_procesos > max_procesos:
        print(f"Error: el número de workers debe estar entre 1 y {max_procesos}.")
        sys.exit(1)

    inicio = time.perf_counter()

    with multiprocessing.Pool(processes=num_procesos) as pool:
        resultados = pool.map(calcular, datos)

    resultado_total = sum(resultados)

    fin = time.perf_counter()

    print("=== EJECUCIÓN PARALELA ===")
    print(f"Datos procesados: {n:,}")
    print(f"Workers utilizados: {num_procesos}")
    print(f"Resultado: {resultado_total}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
