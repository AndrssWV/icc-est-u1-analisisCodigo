class MetodosOrdenamiento:

    def sort_bubble(self, array):  
        arreglo = array.copy()
        for i in range(len(arreglo)):
            for j in range(i+1,len(arreglo)):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)-1):
            intercambio = False
            for j in range(i+1,len(arreglo)-1-i):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break

    def sort_seleccion(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)-1):
            iM = arreglo[i]
            for j in range(i+1, len(arreglo)):
                if arreglo[j] < arreglo[iM]:
                    iM = j
            if iM != i:
                arreglo[i], arreglo[iM] = arreglo[iM], arreglo[i]



