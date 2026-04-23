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