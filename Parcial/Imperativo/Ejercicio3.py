import heapq

# Un min-heap de tamaño k guarda los k mayores vistos.
# La raíz siempre es el MENOR de esos k elementos.
#
# Por cada número nuevo:
#   - Si es mayor que la raíz → entra al heap, saca la raíz
#   - Si no → se descarta
#
# Costo por elemento: O(log k)  ← solo log del tamaño del heap, no de n
# Total: O(n log k)             ← mucho mejor que O(n log n) de sorted()

def top_k(lista, k):
    if k <= 0 or not lista:
        return []

    # Construye el heap con los primeros k elementos → O(k)
    heap = lista[:k]
    heapq.heapify(heap)                      # O(k)

    # Recorre el resto → O((n-k) * log k)
    for numero in lista[k:]:
        if numero > heap[0]:                 # heap[0] = el menor del heap
            heapq.heapreplace(heap, numero)  # saca el menor, mete el nuevo → O(log k)

    # Ordena los k elementos de mayor a menor → O(k log k), despreciable si k << n
    return sorted(heap, reverse=True)
lista = [45, 12, 87, 3, 56, 99, 23, 74, 8, 61, 34, 91, 17, 68, 42, 5, 83, 29, 76, 50]
k = 5

print(top_k(lista,k))
