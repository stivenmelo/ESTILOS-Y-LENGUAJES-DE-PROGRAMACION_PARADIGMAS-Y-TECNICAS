# ─────────────────────────────────────────────────────────
# LISTA FUNCIONAL INMUTABLE
#
# Representación: tuplas anidadas (cabeza, resto)
#   None          →  lista vacía        []
#   (1, None)     →  lista con un elem  [1]
#   (2, (1, None))→  lista con dos elem [2, 1]
#
# Las tuplas en Python son INMUTABLES: una vez creadas
# no se pueden cambiar. Esto garantiza que ninguna operación
# pueda modificar una lista existente.
# ─────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────
# OPERACIONES BÁSICAS
# ─────────────────────────────────────────────────────────

def cons(elemento, lista):
    # Crea una lista NUEVA poniendo elemento al frente de lista.
    # Es O(1) porque solo crea una tupla nueva con dos campos:
    # el elemento y una referencia a la lista existente.
    # NO copia ningún elemento de lista.
    #
    # cons(3, (2, (1, None)))  →  (3, (2, (1, None)))
    #                                    ↑ misma lista, solo referencia
    return (elemento, lista)


def head(lista):
    # Retorna el primer elemento de la lista.
    # head((3, (2, (1, None))))  →  3
    if lista is None:
        return None
    return lista[0]


def tail(lista):
    # Retorna la lista SIN el primer elemento.
    # tail((3, (2, (1, None))))  →  (2, (1, None))
    # NO copia nada, solo retorna la referencia al resto.
    if lista is None:
        return None
    return lista[1]


def to_python_list(lista):
    # Convierte la lista funcional a una lista Python normal.
    # Recorre la estructura con recursión pura (sin mutación).
    # to_python_list((3, (2, (1, None))))  →  [3, 2, 1]
    if lista is None:
        return []
    return [head(lista)] + to_python_list(tail(lista))


# ─────────────────────────────────────────────────────────
# DEMOSTRACIÓN: listas que comparten estructura
#
# lista1 = [1, 2, 3]
# lista2 = [0, 1, 2, 3]  ← comparte lista1 como su "cola"
#
# En memoria:
#   lista1 →  (1, → (2, → (3, None)))
#   lista2 →  (0, ↗)
#              ↑ apunta a lista1, no la copia
# ─────────────────────────────────────────────────────────

lista_vacia = None

lista1 = cons(3, cons(2, cons(1, lista_vacia)))   # [3, 2, 1]
lista2 = cons(4, lista1)                           # [4, 3, 2, 1] comparte lista1
lista3 = cons(5, lista1)                           # [5, 3, 2, 1] también comparte lista1

print("lista1:", to_python_list(lista1))   # [3, 2, 1]
print("lista2:", to_python_list(lista2))   # [4, 3, 2, 1]
print("lista3:", to_python_list(lista3))   # [5, 3, 2, 1]

# ─────────────────────────────────────────────────────────
# TEST: lista1 no fue modificada al crear lista2 y lista3
# ─────────────────────────────────────────────────────────

print("\n--- TEST: inmutabilidad ---")
print("lista1 sigue siendo:", to_python_list(lista1))   # [3, 2, 1] sin cambios

# Verificar que lista2 y lista3 comparten la misma estructura de lista1
# 'is' compara identidad de objeto en memoria (no copia)
print("tail(lista2) is lista1:", tail(lista2) is lista1)   # True → misma referencia
print("tail(lista3) is lista1:", tail(lista3) is lista1)   # True → misma referencia

print("\n--- TEST: operaciones ---")
print("head(lista1):", head(lista1))                   # 3
print("tail(lista1):", to_python_list(tail(lista1)))   # [2, 1]
