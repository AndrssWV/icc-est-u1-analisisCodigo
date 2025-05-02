class MetodosOrdenamiento:

    def sort_bubble(self, array):  
        arreglo = array.copy()
        for i in range(len(arreglo)):
            for j in range(i+1,len(arreglo)):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

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
            iM = i
            for j in range(i+1, len(arreglo)):
                if arreglo[j] < arreglo[iM]:
                    iM = j
            if iM != i:
                arreglo[i], arreglo[iM] = arreglo[iM], arreglo[i]

    def sort_shell(self, array):
        arreglo = array.copy()
        gap = len(arreglo)//2
        while gap > 0:
            for i in range(gap, len(arreglo)):
                temp = arreglo[i]
                j = i
                while j>= gap and arreglo[j-gap] > temp:
                    arreglo[j] = arreglo[j-gap]
                    j-= gap
                arreglo[j] = temp
            gap//=2




