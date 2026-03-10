productos = [
 {"nombre": "Audifonos", "precio": 35000, "categoria": "electronico"},
 {"nombre": "Camisa", "precio": 80000, "categoria": "ropa"},
 {"nombre": "Laptop", "precio": 250000, "categoria": "electronico"},
 {"nombre": "Zapatos", "precio": 45000, "categoria": "ropa"},
 {"nombre": "Teclado", "precio": 60000, "categoria": "electronico"},
 ]

def procesar_catalogo(productos:dict):
    retorno:dict = {}
    getProductosCaros = lambda producto: producto["precio"]> 50000
    getNombresProductos = lambda producto: producto["nombre"]
    getProductosElectronicos = lambda producto: producto["categoria"] == "electronico"
    getPrecioIva = lambda producto: producto["precio"]*1.19

    retorno["caros"] = list(map(getNombresProductos, list(filter(getProductosCaros, productos )))) 
    
    retorno["electronicos"] = list(map(getNombresProductos, list(filter(getProductosElectronicos,productos))))
    
    retorno["con_iva"] = list(map(lambda p: {**p, "precio_con_iva": p["precio"] * 1.19}, productos))

    
    print(retorno)



procesar_catalogo(productos) 