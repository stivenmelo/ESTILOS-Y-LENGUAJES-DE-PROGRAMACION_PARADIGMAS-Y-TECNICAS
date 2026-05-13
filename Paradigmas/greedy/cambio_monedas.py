# Algoritmo Greedy para el problema de cambio de monedas.
# La estrategia es siempre elegir la moneda de mayor valor posible
# que no supere el monto restante, repitiendo hasta llegar a 0.

def cambio_greedy(monto: int, monedas: list[int]) -> dict:
    # Ordenar de mayor a menor para aplicar la eleccion greedy
    monedas_ordenadas = sorted(monedas, reverse=True)

    resultado = {}   # {denominacion: cantidad_usada}
    restante = monto # cuanto falta por cubrir

    for moneda in monedas_ordenadas:
        if restante <= 0:
            break  # ya se cubrió el monto completo

        # Division entera: cuantas veces cabe esta moneda en el restante
        cantidad = restante // moneda

        if cantidad > 0:
            resultado[moneda] = cantidad
            # Restar el valor total aportado por esta moneda
            restante -= moneda * cantidad

    return resultado


def mostrar_solucion(monto: int, monedas: list[int]) -> None:
    print(f"Cambio para {monto} unidades")
    print(f"Monedas disponibles: {sorted(monedas, reverse=True)}")
    print("-" * 40)

    resultado = cambio_greedy(monto, monedas)
    total_monedas = 0

    # Recorrer el resultado ordenado de mayor a menor denominacion
    for moneda, cantidad in sorted(resultado.items(), reverse=True):
        print(f"  Moneda {moneda:>3}: {cantidad} unidad(es)  ->  subtotal {moneda * cantidad}")
        total_monedas += cantidad

    print("-" * 40)
    print(f"Total de monedas usadas: {total_monedas}")
    # Sumar todos los valores para verificar que dan exactamente el monto
    print(f"Verificacion: {sum(m * c for m, c in resultado.items())} == {monto}")


if __name__ == "__main__":
    MONEDAS = [50, 20, 10, 5, 2, 1]
    MONTO = 93
    mostrar_solucion(MONTO, MONEDAS)
