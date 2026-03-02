from functools import reduce

ventas = [
    {
        "producto": "Laptop Pro 14",
        "categoria": "Electrónica",
        "precio": 1200.50,
        "cantidad": 15,
        "vendedor": "TechStore Central"
    },
    {
        "producto": "Monitor 4K 27\"",
        "categoria": "Periféricos",
        "precio": 350.00,
        "cantidad": 22,
        "vendedor": "Vision Digital"    
    },
    {
        "producto": "Teclado Mecánico RGB",
        "categoria": "Accesorios",
        "precio": 85.99,
        "cantidad": 50,
        "vendedor": "Vision Digital"
    },
    {
        "producto": "Silla Ergonómica",
        "categoria": "Muebles",
        "precio": 210.00,
        "cantidad": 10,
        "vendedor": "Office Solutions"
    },
    {
        "producto": "Smartphone Alpha",
        "categoria": "Telefonía",
        "precio": 799.00,
        "cantidad": 30,
        "vendedor": "TechStore Central"
    },
    {
        "producto": "Mouse Inalámbrico",
        "categoria": "Accesorios",
        "precio": 25.50,
        "cantidad": 100,
        "vendedor": "Vision Digital"
    },
    {
        "producto": "Escritorio Elevable",
        "categoria": "Muebles",
        "precio": 450.75,
        "cantidad": 5,
        "vendedor": "Office Solutions"
    },
    {
        "producto": "Auriculares Noise Cancelling",
        "categoria": "Audio",
        "precio": 180.00,
        "cantidad": 40,
        "vendedor": "Audio Master"
    },
    {
        "producto": "Cámara Web 1080p",
        "categoria": "Periféricos",
        "precio": 55.00,
        "cantidad": 25,
        "vendedor": "TechStore Central"
    },
    {
        "producto": "Tableta Gráfica",
        "categoria": "Electrónica",
        "precio": 299.99,
        "cantidad": 12,
        "vendedor": "Creative Shop"
    }
]

calcularTotal = lambda venta : venta['precio'] * venta['cantidad']
listaTotales = list(map(calcularTotal, ventas))
totalVenta = reduce(lambda contador, venta : contador + venta['precio'] * venta['cantidad'],ventas,0)
ventasMayoresa1000 = list(filter(lambda venta: venta['precio'] * venta['cantidad'] > 1000, ventas))

print(f"totales por venta : {listaTotales} \n")
print(f"Total acomulado de las ventas: {totalVenta}\n")
print(f"ventas mayores a 1000: {ventasMayoresa1000}\n")


# 1. Tu función de cálculo base
calcularTotal = lambda x : x['precio'] * x['cantidad']

# 2. Diccionario acumulador
ventas_vendedores = {}

# 3. Función de acumulación
def acumular(p):
    vendedor = p['vendedor']
    total = calcularTotal(p)
    ventas_vendedores[vendedor] = ventas_vendedores.get(vendedor, 0) + total

list(map(acumular, ventas))

# 5. Resultado
print("--- Reporte de Ventas por Vendedor ---")
list(map(lambda item: print(f"{item[0]}: ${item[1]}"), ventas_vendedores.items()))
