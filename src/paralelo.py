import math
import time
import multiprocessing


def calcular(x):
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


def main():
    n = 1_000_000
    datos = range(1, n + 1)

    inicio = time.perf_counter()

    num_procesos = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=num_procesos) as pool:
        resultados = pool.map(calcular, datos)

    resultado_total = sum(resultados)

    fin = time.perf_counter()

    print("=== EJECUCIÓN PARALELA ===")
    print(f"Datos procesados: {n:,}")
    print(f"Procesos utilizados: {num_procesos}")
    print(f"Resultado: {resultado_total}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")


if __name__ == "__main__":
    main()
