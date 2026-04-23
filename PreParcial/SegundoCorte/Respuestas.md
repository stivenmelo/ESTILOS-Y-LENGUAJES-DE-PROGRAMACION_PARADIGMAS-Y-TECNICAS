# EJERCICIO 1

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

# EJERCICIO 2

## Codigo Corregido
```python
import threading, queue, random, time

cola = queue.Queue() # cola thread-safe

def productor():
    for _ in range(10):
        num = random.randint(1, 50)
        print(f"[Productor] Generado: {num}")
        cola.put(num)
        time.sleep(0.1)
    cola.put(-1)

def consumidor():
    acumulado = 0
    while True:
        item = cola.get()
        if item == -1:
            break
        acumulado += item
        print(f"[Consumidor] Recibido: {item} | Suma: {acumulado}")

    print(f"Suma total: {acumulado}")

t_prod = threading.Thread(target=productor)
t_cons = threading.Thread(target=consumidor)

t_prod.start()
t_cons.start()

t_prod.join()
t_cons.join()
```

## Salida

```cmd
[Productor] Generado: 50
[Consumidor] Recibido: 50 | Suma: 50
[Productor] Generado: 32
[Consumidor] Recibido: 32 | Suma: 82
[Productor] Generado: 50
[Consumidor] Recibido: 50 | Suma: 132
[Productor] Generado: 24
[Consumidor] Recibido: 24 | Suma: 156
[Productor] Generado: 1
[Consumidor] Recibido: 1 | Suma: 157
[Productor] Generado: 21
[Consumidor] Recibido: 21 | Suma: 178
[Productor] Generado: 33
[Consumidor] Recibido: 33 | Suma: 211
[Productor] Generado: 49
[Consumidor] Recibido: 49 | Suma: 260
[Productor] Generado: 16
[Consumidor] Recibido: 16 | Suma: 276
[Productor] Generado: 8
[Consumidor] Recibido: 8 | Suma: 284
Suma total: 284
```

## Preguntas de analisis

¿Por qué queue.Queue hace innecesario usar un Lock explícito? ¿Qué garantiza internamente esa clase?

> el `queue.Queue`  por defento tiene configurado el Lock, lo cual permite bloquear el hilo de producto cuando se llena y el hilo de consumidor espera que se libere el lock para poder extraer el elemento de la cola, evitando corrupcion del hilo en el mismo momento de ejecucion de los hilos.


¿El consumidor siempre recibe los números en el mismo orden en que el productor los generó? Justifica tu respuesta.

> si por que el `queue.Queue` esta configurado por defecto FIFO, entonces el primer elemento en ingresar siempre es el mismo en salir.

¿Qué pasaría si hubiera 2 consumidores y solo un centinela -1? ¿Cómo lo resolverías?

> se procesaria uno de los consumidores pero el siguiente quedaria bloqueado esperando, para corregir esto se agregaria un centinela por cada consumidor que se agregre, permitiendo la finalizacion de cada cola sin que ninguno quede bloqueado esperando. 

por ejemplo:
```python
    NUM_CONSUMIDORES = 2
    for _ in range(NUM_CONSUMIDORES):
        cola.put(-1)
```


¿Qué ventaja tiene usar queue.get() bloqueante en lugar de un bucle activo (busy-wait) que compruebe si la cola está vacía?

>La ventaja principal es que consume menos CPU ya que el busy-wait esta comprobando todo el tiempo si la cola esta vacia `cola.empty()` y pasando `pass`.


