import heapq    # Para encontrar el top 10 sin ordenar todo
import string   # Para obtener todos los signos de puntuación


def analizar_texto(texto):
    # ─────────────────────────────────────────────
    # PASO 1: Limpiar el texto
    # ─────────────────────────────────────────────
    # str.maketrans crea una "tabla de traducción"
    # que le dice a Python: "elimina estos caracteres"
    # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    tabla = str.maketrans("", "", string.punctuation)

    # .lower()        → convierte todo a minúsculas  "Hola" → "hola"
    # .translate()    → elimina la puntuación usando la tabla de arriba
    texto_limpio = texto.lower().translate(tabla)


    # ─────────────────────────────────────────────
    # PASO 2: Contar cuántas veces aparece cada palabra
    # ─────────────────────────────────────────────
    # Usamos un diccionario como tabla hash → buscar/insertar cuesta O(1)
    # Recorrer todas las palabras cuesta O(n) → total O(n)
    conteo = {}

    # .split() separa el texto por espacios → ["hola", "mundo", "hola", ...]
    for palabra in texto_limpio.split():
        if palabra in conteo:
            conteo[palabra] += 1   # ya existe → sumar 1
        else:
            conteo[palabra] = 1    # nueva palabra → iniciar en 1

    # Ejemplo del diccionario resultante:
    # { "de": 15, "el": 8, "y": 12, "la": 6, ... }


    # ─────────────────────────────────────────────
    # PASO 3: Calcular totales
    # ─────────────────────────────────────────────
    # sum de todos los valores del diccionario = total de palabras contadas
    total_palabras = sum(conteo.values())

    # len del diccionario = cuántas palabras distintas hay
    palabras_unicas = len(conteo)


    # ─────────────────────────────────────────────
    # PASO 4: Obtener el top 10 más frecuente
    # ─────────────────────────────────────────────
    # heapq.nlargest no ordena todo, usa un heap de tamaño 10
    # → mucho más eficiente que sorted() completo
    # conteo.items() devuelve pares: [("de", 15), ("el", 8), ...]
    # Usamos una función explícita en lugar de lambda (estilo imperativo)
    def obtener_frecuencia(par):
        return par[1]   # par = ("palabra", frecuencia) → retorna solo la frecuencia

    top_10 = heapq.nlargest(10, conteo.items(), key=obtener_frecuencia)


    # ─────────────────────────────────────────────
    # PASO 5: Construir la lista de resultados
    # ─────────────────────────────────────────────
    # Por cada palabra del top 10, calculamos su porcentaje sobre el total
    # Ejemplo: "de" apareció 15 veces de 100 → 15%
    resultado = []
    for palabra, frecuencia in top_10:
        porcentaje = round((frecuencia / total_palabras) * 100, 2)
        resultado.append((palabra, frecuencia, porcentaje))

    # Retorna un diccionario con los tres datos pedidos
    return {
        "top_10": resultado,           # lista de tuplas (palabra, frecuencia, %)
        "palabras_unicas": palabras_unicas,
        "total_palabras": total_palabras
    }


# ─────────────────────────────────────────────────
# TEXTO DE PRUEBA
# ─────────────────────────────────────────────────
texto = """
En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo
de los de lanza en astillero adarga antigua rocín flaco y galgo corredor una olla de algo más vaca que
carnero salpicón las más noches duelos y quebrantos los sábados lantejas los viernes algún palomino de
añadidura los domingos consumían las tres partes de su hacienda el resto della concluían sayo de velarte
calzas de velludo para las fiestas con sus pantuflos de lo mesmo y los días de entresemana se honraba con
su vellorí de lo más fino con sus calzas de velludo y sus babuchas de terciopelo pero el hidalgo andaba
siempre a caballo con su lanza en ristre y su adarga al brazo recorriendo los campos de la Mancha en busca
de aventuras que le diesen nombre y fama en el mundo y también buscaba siempre justicia para los más débiles
y para los que no tenían voz ni poder en aquel tiempo y en aquel lugar donde todo era posible para el que
tenía valor y coraje y determinación y fe en sus propias fuerzas y en la bondad del mundo que le rodeaba
"""

datos = analizar_texto(texto)

print(f"Total palabras : {datos['total_palabras']}")
print(f"Palabras únicas: {datos['palabras_unicas']}")
print("\nTop 10 palabras:")
for palabra, freq, pct in datos["top_10"]:
    print(f"  {palabra:15} → {freq} veces  ({pct}%)")
