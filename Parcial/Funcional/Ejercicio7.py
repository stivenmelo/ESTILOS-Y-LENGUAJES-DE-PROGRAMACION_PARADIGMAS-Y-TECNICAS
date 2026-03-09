# ─────────────────────────────────────────────────────────
# ÁRBOL BINARIO
# Cada nodo es un diccionario con tres claves:
#   "valor" → número entero
#   "izq"   → nodo hijo izquierdo (o None si no existe)
#   "der"   → nodo hijo derecho   (o None si no existe)
#
# Ejemplo visual:
#
#         10
#        /  \
#       5    15
#      / \     \
#     3   7    20
#
# En diccionarios:
# {
#   "valor": 10,
#   "izq": {
#       "valor": 5,
#       "izq": {"valor": 3, "izq": None, "der": None},
#       "der": {"valor": 7, "izq": None, "der": None}
#   },
#   "der": {
#       "valor": 15,
#       "izq": None,
#       "der": {"valor": 20, "izq": None, "der": None}
#   }
# }
# ─────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────
# VERSIÓN 1: Recursión directa (sin TCO)
#
# PROBLEMA: cada llamada recursiva queda "pendiente" en la pila
# esperando el resultado de sus hijos antes de poder sumar.
# Con árboles muy profundos esto puede causar RecursionError.
#
# Pila de llamadas para el árbol de ejemplo:
#   suma(10)
#     suma(5)
#       suma(3) → 3
#       suma(7) → 7
#     5 + 3 + 7 = 15
#     suma(15)
#       suma(20) → 20
#     15 + 20 = 35
#   10 + 15 + 35 = 60
# ─────────────────────────────────────────────────────────

def suma_arbol(nodo):
    # Caso base: nodo vacío aporta 0
    if nodo is None:
        return 0

    # Suma el valor actual + suma del subárbol izquierdo + suma del subárbol derecho
    # ⚠️ La llamada recursiva NO es la última instrucción → no es TCO
    # Python debe guardar en memoria el valor actual mientras espera a los hijos
    return nodo["valor"] + suma_arbol(nodo["izq"]) + suma_arbol(nodo["der"])


# ─────────────────────────────────────────────────────────
# VERSIÓN 2: Recursión con acumulador (estilo TCO)
#
# SOLUCIÓN: en lugar de esperar el resultado de los hijos,
# se pasa una lista de nodos pendientes y un acumulador
# que va cargando la suma parcial.
#
# La llamada recursiva ES la última instrucción → patrón TCO.
# En lenguajes con TCO real (Haskell, Scala, etc.) esto no
# crece la pila de llamadas. En Python el patrón es válido
# y preparable para otros lenguajes o para usar con trampolín.
#
# Flujo para el árbol de ejemplo:
#   pendientes=[raiz],      acum=0
#   pendientes=[izq, der],  acum=10
#   pendientes=[3, 7, der], acum=15
#   pendientes=[7, der],    acum=18
#   pendientes=[der],       acum=25
#   pendientes=[20],        acum=40
#   pendientes=[],          acum=60  ← resultado
# ─────────────────────────────────────────────────────────

def suma_arbol_tco(nodo, pendientes=None, acumulador=0):
    # Inicializar la lista de nodos pendientes en la primera llamada
    if pendientes is None:
        pendientes = []

    # Caso base: nodo actual vacío y no hay más pendientes → retorna acumulador
    if nodo is None:
        if not pendientes:
            return acumulador
        # Tomar el siguiente nodo pendiente y continuar
        # Esta es la ÚLTIMA instrucción → patrón TCO
        return suma_arbol_tco(pendientes[0], pendientes[1:], acumulador)

    # Sumar el valor actual al acumulador (nuevo valor, no modifica el original)
    nuevo_acumulador = acumulador + nodo["valor"]

    # Construir la lista de hijos usando expresiones condicionales → sin mutación
    # Si el hijo existe lo incluye, si no, agrega lista vacía
    # El operador + crea una lista NUEVA, no modifica ninguna existente
    hijos = (
        ([nodo["izq"]] if nodo["izq"] is not None else []) +
        ([nodo["der"]] if nodo["der"] is not None else [])
    )

    # Combinar hijos + pendientes actuales → lista NUEVA sin modificar nada
    nuevos_pendientes = hijos + list(pendientes)

    # Llamada recursiva como ÚLTIMA instrucción → patrón TCO
    return suma_arbol_tco(None, nuevos_pendientes, nuevo_acumulador)


# ─────────────────────────────────────────────────────────
# ÁRBOL DE PRUEBA
#
#         10
#        /  \
#       5    15
#      / \     \
#     3   7    20
#
# Suma esperada: 10 + 5 + 15 + 3 + 7 + 20 = 60
# ─────────────────────────────────────────────────────────

arbol = {
    "valor": 10,
    "izq": {
        "valor": 5,
        "izq": {"valor": 3, "izq": None, "der": None},
        "der": {"valor": 7, "izq": None, "der": None}
    },
    "der": {
        "valor": 15,
        "izq": None,
        "der": {"valor": 20, "izq": None, "der": None}
    }
}

print("Version 1 (sin TCO):", suma_arbol(arbol))
print("Version 2 (con TCO):", suma_arbol_tco(arbol))
