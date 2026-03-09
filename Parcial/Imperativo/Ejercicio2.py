def pares_cero(lista):
    if not lista:
        return []

    vistos = set()
    pares = []

    for numero in lista:
        negativo = -numero
        if negativo in vistos:
            par = (min(numero, negativo), max(numero, negativo))
            if par not in pares:
                pares.append(par)
        else:
            vistos.add(numero)

    return pares


numeros = [-20, -15, -9, -7, -4, -3, -1, 0, 0, 1, 3, 4, 6, 7, 9, 12, 15, 18, 20, 25]

print(pares_cero(numeros)) 
