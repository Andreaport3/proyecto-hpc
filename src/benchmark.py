import subprocess
import re
import statistics


def ejecutar(programa, repeticiones=5):
    tiempos = []

    for _ in range(repeticiones):
        resultado = subprocess.run(
            ["python3", programa],
            capture_output=True,
            text=True
        )

        coincidencia = re.search(
            r"Tiempo de ejecución: ([0-9.]+) segundos",
            resultado.stdout
        )

        if coincidencia:
            tiempos.append(float(coincidencia.group(1)))

    return tiempos


def main():
    secuencial = ejecutar("src/secuencial.py")
    paralelo = ejecutar("src/paralelo.py")

    promedio_secuencial = statistics.mean(secuencial)
    promedio_paralelo = statistics.mean(paralelo)

    speedup = promedio_secuencial / promedio_paralelo
    procesos = 8
    eficiencia = speedup / procesos

    print("=== BENCHMARK HPC ===")
    print(f"Promedio secuencial: {promedio_secuencial:.6f} segundos")
    print(f"Promedio paralelo:   {promedio_paralelo:.6f} segundos")
    print(f"Speedup:             {speedup:.4f}")
    print(f"Procesos:            {procesos}")
    print(f"Eficiencia:         {eficiencia:.4f}")
    print(f"Eficiencia (%):      {eficiencia * 100:.2f}%")


if __name__ == "__main__":
    main()
