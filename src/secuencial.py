import math
import time


def calcular(x):
    return math.sqrt(x) + x**2 + math.sin(x) + math.cos(x) + math.log(x)


def ejecutar_secuencial(n):
    inicio = time.perf_counter()

    resultado = 0.0

    for i in range(1, n + 1):
        resultado += calcular(float(i))

    fin = time.perf_counter()

    tiempo = fin - inicio

    return resultado, tiempo


if __name__ == "__main__":
    N = 1_000_000

    resultado, tiempo = ejecutar_secuencial(N)

    print("=== EJECUCIÓN SECUENCIAL ===")
    print(f"Datos procesados: {N:,}")
    print(f"Resultado: {resultado}")
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
