# Patrón Productor–Consumidor en Python

## ¿Qué hace el programa?

Dos hilos corren al mismo tiempo: el **Productor** genera números aleatorios y los mete en una cola compartida; el **Consumidor** los saca de esa misma cola, los imprime y los suma. Al final se muestra la suma total.

---

## Diagrama de flujo general

```
[Hilo Productor]          [Cola compartida]         [Hilo Consumidor]
     |                          |                          |
  genera num  ---put(num)---->  |  ---get()----------->  lee num
     |                          |                          |
  (repite 10 veces)             |                       acumula suma
     |                          |                          |
  put(-1)  ------------------>  |  ---get()----------->  recibe -1 → para
```

---

## Explicación línea por línea

### Importaciones

```python
import threading, queue, random, time
```

| Módulo | Para qué se usa |
|---|---|
| `threading` | Crear y manejar hilos |
| `queue` | Cola thread-safe entre hilos |
| `random` | Generar números aleatorios |
| `time` | Pausar la ejecución con `sleep` |

---

### Cola compartida

```python~
cola = queue.Queue()
```

- Se crea **una sola cola** que comparten ambos hilos.
- `queue.Queue` es **thread-safe**: internamente maneja los bloqueos para que dos hilos no corrompan los datos al acceder al mismo tiempo.
- No se necesita un `Lock` explícito gracias a esto.

---

### Función `productor()`

```python
def productor():
```
Define la función que ejecutará el hilo productor.

```python
    for _ in range(10):
```
Repite el bloque 10 veces. La variable `_` se usa por convención cuando no necesitamos el valor del índice.

```python
        num = random.randint(1, 50)
```
Genera un número entero aleatorio entre 1 y 50 (ambos inclusive) y lo guarda en `num`.

```python
        print(f"[Productor] Generado: {num}")
```
Imprime el número generado para que se vea en consola. El prefijo `[Productor]` ayuda a identificar qué hilo está hablando.

```python
        cola.put(num)
```
**Inserta `num` al final de la cola.** Si la cola estuviera llena (no es el caso aquí), este método bloquearía el hilo hasta que hubiera espacio.

```python
        time.sleep(0.1)
```
Pausa el hilo 0.1 segundos (100 ms) para simular que la producción de datos tarda tiempo. Esto también le da al consumidor tiempo de procesar.

```python
    cola.put(-1)
```
Al terminar el bucle, mete el valor **centinela `-1`** en la cola. Este valor especial le indica al consumidor que ya no habrá más datos y que debe detenerse.

---

### Función `consumidor()`

```python
def consumidor():
```
Define la función que ejecutará el hilo consumidor.

```python
    acumulado = 0
```
Variable local que acumula la suma de todos los números recibidos. Empieza en 0.

```python
    while True:
```
Bucle infinito: el consumidor sigue leyendo de la cola hasta que reciba la señal de parada.

```python
        item = cola.get()
```
**Saca el próximo elemento de la cola.** Si la cola está vacía, este método **bloquea el hilo** (lo pone a dormir) hasta que el productor ponga algo. Esto evita el "busy waiting" (no gasta CPU esperando).

```python
        if item == -1:
            break
```
Comprueba si el elemento es el centinela `-1`. Si lo es, sale del bucle `while True` y termina la función.

```python
        acumulado += item
```
Si no es el centinela, suma el número al acumulado.

```python
        print(f"[Consumidor] Recibido: {item} | Suma: {acumulado}")
```
Imprime el número recibido y la suma parcial hasta ese momento.

```python
    print(f"Suma total: {acumulado}")
```
Cuando el bucle termina (se recibió `-1`), imprime la suma final de todos los números procesados.

---

### Creación de los hilos

```python
t_prod = threading.Thread(target=productor)
t_cons = threading.Thread(target=consumidor)
```

- Crea dos objetos `Thread`.
- `target=productor` le dice al hilo qué función debe ejecutar.
- En este punto los hilos **no han comenzado aún**, solo están creados.

---

### Inicio de los hilos

```python
t_prod.start()
t_cons.start()
```

- `.start()` lanza cada hilo: el sistema operativo los ejecuta en paralelo con el programa principal.
- Después de estas dos líneas, **tres flujos de ejecución corren al mismo tiempo**: el hilo principal, el productor y el consumidor.

---

### Espera a que terminen

```python
t_prod.join()
t_cons.join()
```

- `.join()` hace que el hilo principal **espere** a que ese hilo termine antes de continuar.
- Sin `join()`, el programa principal podría terminar antes que los hilos, cerrando el proceso abruptamente.
- `t_prod.join()` espera al productor → `t_cons.join()` espera al consumidor.

---

## Ejemplo de salida

```
[Productor] Generado: 9
[Consumidor] Recibido: 9 | Suma: 9
[Productor] Generado: 36
[Consumidor] Recibido: 36 | Suma: 45
[Productor] Generado: 20
[Consumidor] Recibido: 20 | Suma: 65
...
[Productor] Generado: 46
[Consumidor] Recibido: 46 | Suma: 271
Suma total: 271
```

> Los números cambian en cada ejecución porque son aleatorios.

---

## Conceptos clave

| Concepto | Descripción |
|---|---|
| **Hilo (Thread)** | Flujo de ejecución independiente dentro del mismo proceso |
| **Cola thread-safe** | Estructura de datos que permite acceso seguro desde múltiples hilos |
| **`put()`** | Inserta un elemento al final de la cola |
| **`get()`** | Saca y devuelve el elemento del frente de la cola (bloquea si está vacía) |
| **Centinela** | Valor especial (`-1`) que señala "no hay más datos" |
| **`join()`** | Espera a que un hilo termine antes de continuar |
