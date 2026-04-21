import threading 
import time 
 
def trabajador(id_hilo, duracion): 
    print(f"Hilo {id_hilo} iniciando...") 
    time.sleep(duracion) 
    print(f"Hilo {id_hilo} terminado.") 
 
duraciones = [0.5, 0.3, 0.8, 0.2] 
hilos = [] 
 
for i in range(4): 
    # ERROR 1: Thread no recibe argumentos — falta args=(i, duraciones[i]) 
    t = threading.Thread(target=trabajador) 
    hilos.append(t) 
 
# ERROR 2: los hilos nunca se inician (falta t.start()) 
for h in hilos: 
    pass 
 
# ERROR 3: join() se llama antes de start() — orden incorrecto 
for h in hilos: 
    h.join() 
 
# ERROR 4: este print podría ejecutarse antes de que los hilos arranquen 
# (en este código el problema es que join sin start no espera nada útil) 
print("Todos los hilos han terminado.") 
