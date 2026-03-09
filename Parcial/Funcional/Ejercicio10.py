import time

# ─────────────────────────────────────────────────────────
# DECORADOR @memoizar
#
# Un decorador es una función que envuelve a otra función
# para agregar comportamiento adicional sin modificarla.
#
# @memoizar sobre una función f:
#   - Primera vez que se llama f(x): calcula y guarda en cache
#   - Segunda vez que se llama f(x): retorna el resultado guardado
#     sin volver a calcular → llamada "ahorrada"
#
# Solo válido en funciones PURAS: mismo input → mismo output.
# Si la función tuviera efectos secundarios, la cache devolvería
# resultados incorrectos.
# ─────────────────────────────────────────────────────────

def memoizar(funcion):
    cache = {}          # diccionario: { argumentos: resultado }
    ahorros = [0]       # lista de un elemento para poder modificarla desde la función interna

    def envoltura(*args):
        if args in cache:
            # Ya calculado antes → retornar directamente sin llamar a funcion
            ahorros[0] += 1
            return cache[args]

        # Primera vez → calcular y guardar
        resultado = funcion(*args)
        cache[args] = resultado
        return resultado

    # Agregar acceso al cache y ahorros desde afuera
    envoltura.cache   = cache
    envoltura.ahorros = ahorros
    return envoltura


# ─────────────────────────────────────────────────────────
# (a) FIBONACCI con y sin memoización
#
# Sin memo: fib(5) llama a fib(4) y fib(3)
#           fib(4) llama a fib(3) y fib(2)  ← fib(3) se recalcula
#           fib(3) llama a fib(2) y fib(1)  ← fib(2) se recalcula
# Árbol de llamadas crece exponencialmente → O(2^n)
#
# Con memo: fib(3) se calcula UNA vez y se reutiliza → O(n)
# ─────────────────────────────────────────────────────────

def fibonacci_sin_memo(n):
    if n <= 1:
        return n
    return fibonacci_sin_memo(n - 1) + fibonacci_sin_memo(n - 2)

@memoizar
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ─────────────────────────────────────────────────────────
# (b) CAMINO MÁS CORTO en grafo con recursión + memoización
#
# Grafo representado como diccionario de adyacencia con pesos:
# { nodo: [(vecino, costo), ...] }
#
# La función busca el costo mínimo de 'inicio' a 'fin'.
# Sin memo: recalcula los mismos subcaminos muchas veces.
# Con memo: cada subcamino se calcula solo una vez.
# ─────────────────────────────────────────────────────────

GRAFO = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def camino_sin_memo(grafo, actual, destino, visitados=()):
    if actual == destino:
        return 0
    if actual not in grafo or not grafo[actual]:
        return float('inf')

    nueva_visitados = visitados + (actual,)
    costos = []
    for vecino, peso in grafo[actual]:
        if vecino not in nueva_visitados:
            sub = camino_sin_memo(grafo, vecino, destino, nueva_visitados)
            if sub != float('inf'):
                costos.append(peso + sub)

    return min(costos) if costos else float('inf')

@memoizar
def camino(actual, destino, visitados=()):
    if actual == destino:
        return 0
    if actual not in GRAFO or not GRAFO[actual]:
        return float('inf')

    nueva_visitados = visitados + (actual,)
    costos = []
    for vecino, peso in GRAFO[actual]:
        if vecino not in nueva_visitados:
            sub = camino(vecino, destino, nueva_visitados)
            if sub != float('inf'):
                costos.append(peso + sub)

    return min(costos) if costos else float('inf')


# ─────────────────────────────────────────────────────────
# (c) EVALUACIÓN DE ÁRBOL MATEMÁTICO con memoización
#
# El árbol representa expresiones como diccionarios:
# { "op": "+", "izq": {...}, "der": {...} }
# { "val": 5 }  ← hoja (número)
#
# Ejemplo: (3 + 4) * (3 + 4)
# Sin memo: evalúa (3+4) dos veces
# Con memo: evalúa (3+4) una vez y reutiliza
#
# Las tuplas son hashables → podemos usar el árbol como clave
# convirtiendo el diccionario a tupla con arbol_a_tupla()
# ─────────────────────────────────────────────────────────

def arbol_a_tupla(nodo):
    # Convierte el árbol (dict) a tupla anidada para que sea hashable
    if "val" in nodo:
        return ("val", nodo["val"])
    return (nodo["op"], arbol_a_tupla(nodo["izq"]), arbol_a_tupla(nodo["der"]))

def evaluar_sin_memo(nodo):
    if "val" in nodo:
        return nodo["val"]
    izq = evaluar_sin_memo(nodo["izq"])
    der = evaluar_sin_memo(nodo["der"])
    if nodo["op"] == "+": return izq + der
    if nodo["op"] == "-": return izq - der
    if nodo["op"] == "*": return izq * der
    if nodo["op"] == "/": return izq / der

@memoizar
def evaluar(clave):
    # clave es la tupla del árbol → hashable para la cache
    if clave[0] == "val":
        return clave[1]
    op, izq, der = clave
    v_izq = evaluar(izq)
    v_der = evaluar(der)
    if op == "+": return v_izq + v_der
    if op == "-": return v_izq - v_der
    if op == "*": return v_izq * v_der
    if op == "/": return v_izq / v_der


# ─────────────────────────────────────────────────────────
# MEDICIÓN DE TIEMPOS
# ─────────────────────────────────────────────────────────

def medir(nombre, funcion, *args):
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    print(f"  {nombre:30} resultado={resultado}  tiempo={fin - inicio:.6f}s")
    return resultado


print("=" * 60)
print("(a) FIBONACCI n=35")
print("=" * 60)
medir("Sin memoizacion", fibonacci_sin_memo, 35)
medir("Con memoizacion", fibonacci,          35)
print(f"  Llamadas ahorradas por cache: {fibonacci.ahorros[0]}")

print()
print("=" * 60)
print("(b) CAMINO MAS CORTO A->D")
print("=" * 60)
medir("Sin memoizacion", camino_sin_memo, GRAFO, 'A', 'D')
medir("Con memoizacion", camino,          'A', 'D')
print(f"  Llamadas ahorradas por cache: {camino.ahorros[0]}")

print()
print("=" * 60)
print("(c) ARBOL: (3 + 4) * (3 + 4)")
print("=" * 60)
arbol = {
    "op": "*",
    "izq": {"op": "+", "izq": {"val": 3}, "der": {"val": 4}},
    "der": {"op": "+", "izq": {"val": 3}, "der": {"val": 4}}
}
clave = arbol_a_tupla(arbol)
medir("Sin memoizacion", evaluar_sin_memo, arbol)
medir("Con memoizacion", evaluar,          clave)
print(f"  Llamadas ahorradas por cache: {evaluar.ahorros[0]}")
