import subprocess
import re
import statistics
import matplotlib.pyplot as plt


WORKERS = [1, 2, 4]
REPETICIONES = 3


def ejecutar_paralelo(workers):
    tiempos = []

    for prueba in range(REPETICIONES):
        resultado = subprocess.run(
            ["python3", "src/paralelo.py", str(workers)],
            capture_output=True,
            text=True
        )

        coincidencia = re.search(
            r"Tiempo de ejecución: ([0-9.]+) segundos",
            resultado.stdout
        )

        if coincidencia:
            tiempo = float(coincidencia.group(1))
            tiempos.append(tiempo)

            print(
                f"Workers: {workers} | "
                f"Prueba: {prueba + 1} | "
                f"Tiempo: {tiempo:.6f} segundos"
            )

    return tiempos


def main():
    resultados = {}

    print("=== BENCHMARK HPC ===")
    print()

    for workers in WORKERS:
        resultados[workers] = ejecutar_paralelo(workers)
        print()

    promedios = {}

    for workers in WORKERS:
        promedios[workers] = statistics.mean(resultados[workers])

    tiempo_1 = promedios[1]

    texto = []
    texto.append("=== BENCHMARK HPC ===\n")

    for workers in WORKERS:
        promedio = promedios[workers]
        speedup = tiempo_1 / promedio
        eficiencia = speedup / workers

        print(f"Workers: {workers}")
        print(f"Promedio: {promedio:.6f} segundos")
        print(f"Speedup: {speedup:.4f}")
        print(f"Eficiencia: {eficiencia:.4f}")
        print(f"Eficiencia (%): {eficiencia * 100:.2f}%")
        print()

        texto.append(f"Workers: {workers}\n")
        texto.append(
            f"Pruebas: {', '.join(f'{t:.6f}' for t in resultados[workers])}\n"
        )
        texto.append(f"Promedio: {promedio:.6f} segundos\n")
        texto.append(f"Speedup: {speedup:.4f}\n")
        texto.append(f"Eficiencia: {eficiencia:.4f}\n")
        texto.append(f"Eficiencia (%): {eficiencia * 100:.2f}%\n\n")

    with open("resultados/benchmark.txt", "w") as archivo:
        archivo.writelines(texto)

    # Gráfica de workers vs. tiempo
    tiempos = [promedios[w] for w in WORKERS]

    plt.figure(figsize=(8, 5))
    plt.plot(WORKERS, tiempos, marker="o")
    plt.xlabel("Número de workers")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Workers vs. Tiempo de ejecución")
    plt.xticks(WORKERS)
    plt.grid(True)
    plt.savefig("resultados/workers_vs_tiempo.png")
    plt.close()

    # Gráfica de workers vs. speedup
    speedups = [tiempo_1 / promedios[w] for w in WORKERS]

    plt.figure(figsize=(8, 5))
    plt.plot(WORKERS, speedups, marker="o")
    plt.xlabel("Número de workers")
    plt.ylabel("Speedup")
    plt.title("Workers vs. Speedup")
    plt.xticks(WORKERS)
    plt.grid(True)
    plt.savefig("resultados/workers_vs_speedup.png")
    plt.close()

    # Gráfica de workers vs. eficiencia
    eficiencias = [(tiempo_1 / promedios[w]) / w * 100 for w in WORKERS]

    plt.figure(figsize=(8, 5))
    plt.plot(WORKERS, eficiencias, marker="o")
    plt.xlabel("Número de workers")
    plt.ylabel("Eficiencia (%)")
    plt.title("Workers vs. Eficiencia")
    plt.xticks(WORKERS)
    plt.grid(True)
    plt.savefig("resultados/workers_vs_eficiencia.png")
    plt.close()

    print("Resultados guardados en resultados/benchmark.txt")
    print("Gráfica guardada en resultados/workers_vs_tiempo.png")
    print("Gráfica guardada en resultados/workers_vs_speedup.png")
    print("Gráfica guardada en resultados/workers_vs_eficiencia.png")


if __name__ == "__main__":
    main()
