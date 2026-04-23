import threading, queue, random, time

cola = queue.Queue() # cola thread-safe

def productor():
    for _ in range(10):
        num = random.randint(1, 50) 
        # TODO 1: imprime '[Productor] Generado: <num>' 
        # TODO 2: pon num en la cola 
        time.sleep(0.1)
    
    # TODO 3: pon el centinela -1 en la cola para avisar al consumidor
    
def consumidor():
    acumulado = 0
    while True:
        item = _______________ # TODO 4: saca elemento de la cola (bloqueante)
        if item == -1:
            break
        acumulado += item
        # TODO 5: imprime '[Consumidor] Recibido: <item> | Suma: <acumulado>'
    
    print(f"Suma total: {acumulado}")
    
# TODO 6: crea hilos para productor y consumidor, inicialos y aplica join