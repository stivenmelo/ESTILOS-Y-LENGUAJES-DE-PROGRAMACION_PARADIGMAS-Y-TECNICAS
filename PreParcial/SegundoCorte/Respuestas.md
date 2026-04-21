# ejercicio1

|#|Línea / Sección|Explicación del error y corrección|
| ------------- |:-------------:|:-------------:|
|1|14|en la insersion del hilo metodo trabajador no tiene los argunetos de id_hilo y duracion , se agregan los argumentos al metodo **`trabajador(i,duraciones[i])`**|
|2|19 - 18|no se inicia el hilo, se corije inicalizandolo **`h.start()`**|
|3|23|como no se habian inicializado los hilos no se podia ejecutar el join para esperar que terminaran, con el ajuste de erro numero dos se corrije|
|4|27|como no se habian inicializado los hilos, puede que se ejecutara el print antes de finalizar la ejecucion, no asegurando la correcta implementacion, con el ajuste de erro numero dos se corrije |

## Codigo Corregido

```python
import threading 
import time 
 
def trabajador(id_hilo, duracion): 
    print(f"Hilo {id_hilo} iniciando...") 
    time.sleep(duracion) 
    print(f"Hilo {id_hilo} terminado.") 
 
duraciones = [0.5, 0.3, 0.8, 0.2] 
hilos = [] 
 
for i in range(4): 
    t = threading.Thread(target=trabajador(i,duraciones[i])) 
    hilos.append(t) 
 
for h in hilos: 
    h.start()
    pass 
 
for h in hilos: 
    h.join() 
 
print("Todos los hilos han terminado.") 
```

## Preguntas de analisis

¿Qué sucede en tiempo de ejecución si un hilo no tiene start()? ¿El programa lanza error o continúa 
silenciosamente?

> como no se inicializaron los hilos, quedan asingados en memoria pero no se ejecutan y como no se inicializan el join genera error ya que no hay hijo ejecutandose que esperar.

¿Por qué es obligatorio pasar args=(id, duracion) al crear el Thread? ¿Qué excepción genera Python al llamar 
trabajador() sin argumentos? 

> por que el metodo por defecto se genero para recibir argumentos y si estos no funcionara ya que los argumentos son null. Este metodo al no recibir algumentos generaria un TypeError el cual indicaria los argunmentos que faltan.

¿Por qué el join() debe llamarse después del start()? Explica qué ocurre si el orden es el contrario. 

> Porque el join funciona como eperador a que el hijo se termine de ejecutar, entonces si no se inicia el hilo pues no hay nada que esperar a ejecutar.

