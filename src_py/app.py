import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
    print('funciona')
    bench = bm.Benchmarking()
    metodos = MetodosOrdenamiento()
    tamanos = [2500, 5000, 10000, 10500]
    resultados = []
    for tam in tamanos:
        arreglo = bench.build_arreglo(tam)
        metodos_object = {
            "burbuja": metodos.sort_bubble,
            "burbuja_mejorado": metodos.sort_burbuja_mejorado_optimizado,
            "seleccion": metodos.sort_seleccion,
            "shell": metodos.sort_shell
        }

        for nombre, metodo in metodos_object.items():
            tiempo_resultado = bench.medir_tiempo(metodo, arreglo)
            tupla = (tam, nombre, tiempo_resultado)
            resultados.append(tupla)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos")
    
    print(resultados)

    tiempo_metodos = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "shell": []
    }

    for tam, nombre, tiempo in resultados:
        tiempo_metodos[nombre].append(tiempo)
    
    plt.figure(figsize=(10,6))
    for nombre, tiempos in tiempo_metodos.items():
        plt.plot(tamanos, tiempos, label=nombre, marker="o")
    plt.title("Andres Villalta " + str(datetime.now()))
    plt.xlabel("Tamaño arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.show()
    