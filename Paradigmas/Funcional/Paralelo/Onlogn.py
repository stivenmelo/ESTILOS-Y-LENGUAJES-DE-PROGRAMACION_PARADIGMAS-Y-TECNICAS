import random
import math

comparaciones = [0]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return merge(L,R)

def merge(L,R):
    result, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        comparaciones[0] += 1
        if L[i] <= R[j]:
            result.append(L[i]); i += 1
        else:
            result.append(R[j]); j += 1
    return result + L[i:] + R[j:]   

arr = [38, 27, 43, 3, 9, 82, 10]
ordenado = merge_sort(arr)

print("7 Elementos")
print("Ordenado:", ordenado)
print("Comparaciones:", comparaciones[0])
print("aproximando comparaciones aplicando O(nlogn):", 7 * math.log2(7))
print("\n")

comparaciones = [0]
arr_100 = [random.randint(1, 1000) for _ in range(100)]

ordenado100 = merge_sort(arr_100)
print("100 Elementos")
#print("Ordenado:", ordenado100)
print("Comparaciones:", comparaciones[0])
print("aproximando comparaciones aplicando O(nlogn):", 100 * math.log2(100))
print("\n")


comparaciones = [0]
arr_1000 = [random.randint(1, 10000) for _ in range(1000)]

ordenado1000 = merge_sort(arr_1000)

print("1000 Elementos")
#print("Ordenado:", ordenado1000)
print("Comparaciones:", comparaciones[0])
print("aproximando comparaciones aplicando O(nlogn):", 1000 * math.log2(1000))



