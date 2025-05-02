import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print('funciona')
    bench = bm.Benchmarking()
    metodos = MetodosOrdenamiento()
    tamanos = [5000, 10000, 10500]
    for tam in tamanos:
        arreglo = bench.build_arreglo(tam)
        metodos_object = {
            "burbuja": metodos.sort_bubble,
            "burbuja_mejorado": metodos.sort_burbuja_mejorado_optimizado,
            "seleccion": metodos.sort_seleccion,
            "shell": metodos.sort_shell
        }

        resultados = []

        for nombre, metodo in metodos_object.items():
            tiempo_resultado = bench.medir_tiempo(metodo, arreglo)
            tupla = (tam, nombre, tiempo_resultado)
            resultados.append(tupla)

        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos")