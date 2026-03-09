import itertools

# ─────────────────────────────────────────────────────────
# GENERADOR LAZY DE NÚMEROS PRIMOS
#
# Un generador con 'yield' NO calcula todos los valores de golpe.
# Solo calcula el SIGUIENTE valor cuando se le pide.
#
# Diferencia con una lista normal:
#   lista  = [2, 3, 5, 7, ...]  → guarda TODOS en memoria
#   generador                   → guarda solo el estado actual
#
# Criba de Eratóstenes incremental:
# En lugar de una tabla fija, usamos un diccionario que registra
# para cada número compuesto el primo que lo "tachó".
#
# Ejemplo paso a paso:
#   n=2 → no está en criba → es primo → yield 2
#          registrar: criba[4] = [2]  (próximo múltiplo de 2)
#   n=3 → no está en criba → es primo → yield 3
#          registrar: criba[6] = [3]
#   n=4 → está en criba[4]=[2] → es compuesto
#          mover: criba[6] += [2]
#   n=5 → no está en criba → es primo → yield 5
#   ...
# ─────────────────────────────────────────────────────────

def numeros_primos():
    # Diccionario: { numero_compuesto: [primos que lo generaron] }
    # Empieza vacío → ningún número ha sido "tachado" aún
    criba = {}

    # Recorre todos los enteros desde 2 hasta infinito
    # count(2) es un generador de itertools → también es lazy
    for n in itertools.count(2):

        if n not in criba:
            # n no fue tachado por ningún primo anterior → es primo
            yield n
            # Registrar el primer múltiplo de n que puede ser compuesto
            # n*n porque todos los menores ya fueron tachados por primos anteriores
            criba[n * n] = [n]

        else:
            # n es compuesto → fue tachado por los primos en criba[n]
            for primo in criba[n]:
                # Mover cada primo al siguiente múltiplo no registrado
                siguiente = n + primo
                while siguiente in criba:
                    siguiente += primo
                criba[siguiente] = criba.get(siguiente, []) + [primo]

            # Limpiar la entrada actual para no desperdiciar memoria
            del criba[n]


# ─────────────────────────────────────────────────────────
# FUNCIONES AUXILIARES
# ─────────────────────────────────────────────────────────

def tomar(n, generador):
    # Retorna los primeros n elementos del generador.
    # islice consume solo lo necesario → no agota el generador completo.
    # tomar(5, primos) → [2, 3, 5, 7, 11]
    return list(itertools.islice(generador, n))


def ir_hasta(limite, generador):
    # Retorna todos los elementos del generador menores que limite.
    # takewhile para cuando la condición deja de cumplirse.
    # ir_hasta(20, primos) → [2, 3, 5, 7, 11, 13, 17, 19]
    return list(itertools.takewhile(lambda x: x < limite, generador))


def primer_mayor_que(umbral, generador):
    # Avanza el generador hasta encontrar el primer primo > umbral.
    # next() pide solo UN valor al generador → muy eficiente.
    return next(p for p in generador if p > umbral)


# ─────────────────────────────────────────────────────────
# DEMOSTRACIÓN
# ─────────────────────────────────────────────────────────

# (a) Primeros 10 primos
# Cada llamada a numeros_primos() crea un generador NUEVO e independiente
primeros_10 = tomar(10, numeros_primos())
print("Primeros 10 primos:", primeros_10)

# (b) Primer primo mayor que 100
primo = primer_mayor_que(100, numeros_primos())
print("Primer primo mayor que 100:", primo)

# (c) Suma de todos los primos menores que 50
primos_hasta_50 = ir_hasta(50, numeros_primos())
suma = sum(primos_hasta_50)
print("Primos menores que 50:", primos_hasta_50)
print("Suma:", suma)

# ─────────────────────────────────────────────────────────
# DEMOSTRACIÓN DE USO DE MEMORIA
# El generador no almacena la secuencia completa.
# Solo guarda el diccionario 'criba' con los primos activos.
# ─────────────────────────────────────────────────────────

import sys
gen = numeros_primos()
print("\nTamano del generador en memoria:", sys.getsizeof(gen), "bytes")
# vs una lista de los primeros 10000 primos:
lista_primos = tomar(10000, numeros_primos())
print("Tamano de lista con 10000 primos:", sys.getsizeof(lista_primos), "bytes")
