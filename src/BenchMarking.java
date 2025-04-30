import java.util.Random;

public class BenchMarking {
    private MetodosOrdenamiento mb;

    public BenchMarking() {
        long currentMilliseconds = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println(currentMilliseconds);
        System.out.println(currentNano);
        mb = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatoria(100000);
        Runnable runnable = () -> mb.burbujaTradicional(arreglo);
        System.out.println(medirCurrentMiles(runnable));
        double m = medirCurrentMiles(runnable);
        double n = medirNanoTime(runnable);
        System.out.println(m+ "  " +n);
    }

    public int[] generarArregloAleatoria(int tamano) {
        Random random = new Random();
        int[] arr = new int[tamano];
        for(int i = 0; i < tamano - 1; i++) {
            arr[i] = random.nextInt(1000000);
        }
        return arr;
    }

    private double medirCurrentMiles(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long f1nal = System.currentTimeMillis();
        double tiempoSegundos = (f1nal - inicio)/1000.0;
        return tiempoSegundos;
    }

    private double medirNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long f1nal = System.nanoTime();
        double tiempoSegundos = (f1nal - inicio)/1000000000.0;
        return tiempoSegundos;
    }
    
}
