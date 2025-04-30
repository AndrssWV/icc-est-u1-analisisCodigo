from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:
    def __init__(self):
        print('benchmarking instanciado')
        self.mo = MetodosOrdenamiento()
        arreglo = self.build_arreglo(10000)
        #tarea = lambda: self.mo.sort_bubble(arreglo)
        #milles = self.contar_con_current_time_milles(tarea)
        #nano = self.contar_con_nano_time(tarea)
        #print(f'Tiempo con milisegundo '+str(milles))
        #print(f'Tiempo con nano '+str(nano))
        b = lambda: self.mo.sort_bubble(arreglo)
        bm = lambda: self.mo.sort_burbuja_mejorado_optimizado(arreglo)
        s = lambda: self.mo.sort_seleccion(arreglo)
        tb = self.contar_con_nano_time(b)
        tbm = self.contar_con_nano_time(bm)
        ts = self.contar_con_nano_time(s)
        print(f'Tiempo con Burbuja '+str(tb))
        print(f'Tiempo con Burbuja Mejorado '+str(tbm))
        print(f'Tiempo con Seleccion '+str(ts))

    def build_arreglo(self, tamano):
        arreglo = []
        for i in range(tamano):
            numeroAletorio = random.randint(0,999)
            arreglo.append(numeroAletorio)
        return arreglo
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        return time.time() - inicio
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        return (time.time_ns() - inicio) / 1000000000.0