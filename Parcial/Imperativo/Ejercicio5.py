def max_suma_ruta(grid):
    # ─────────────────────────────────────────────
    # PASO 1: Obtener dimensiones de la cuadrícula
    # ─────────────────────────────────────────────
    M = len(grid)       # número de filas
    N = len(grid[0])    # número de columnas

    # ─────────────────────────────────────────────
    # PASO 2: Crear tabla DP vacía de M×N
    # ─────────────────────────────────────────────
    # dp[i][j] = mayor suma posible para llegar a la celda [i][j]
    dp = []
    for i in range(M):
        fila = []
        for j in range(N):
            fila.append(0)
        dp.append(fila)

    # ─────────────────────────────────────────────
    # PASO 3: Inicializar punto de partida y bordes
    # ─────────────────────────────────────────────
    dp[0][0] = grid[0][0]

    # Primera columna: solo se puede llegar bajando
    for i in range(1, M):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Primera fila: solo se puede llegar yendo a la derecha
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # ─────────────────────────────────────────────
    # PASO 4: Llenar la tabla DP
    # ─────────────────────────────────────────────
    # Para cada celda interior, elegir el mejor camino:
    # ¿vengo de arriba dp[i-1][j] o de la izquierda dp[i][j-1]?
    for i in range(1, M):
        for j in range(1, N):
            desde_arriba    = dp[i-1][j]
            desde_izquierda = dp[i][j-1]

            if desde_arriba > desde_izquierda:
                dp[i][j] = desde_arriba + grid[i][j]
            else:
                dp[i][j] = desde_izquierda + grid[i][j]

    # ─────────────────────────────────────────────
    # PASO 5: Reconstruir la ruta (backtracking)
    # ─────────────────────────────────────────────
    # Partimos desde [M-1][N-1] y vamos hacia [0][0]
    # En cada paso preguntamos: ¿de dónde vine?
    ruta = []
    i = M - 1
    j = N - 1

    while i > 0 or j > 0:
        ruta.append((i, j))

        if i == 0:
            j -= 1          # solo puedo venir de la izquierda
        elif j == 0:
            i -= 1          # solo puedo venir de arriba
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1          # vine de arriba
        else:
            j -= 1          # vine de la izquierda

    ruta.append((0, 0))     # agregar punto de inicio
    ruta.reverse()          # invertir: de [0][0] a [M-1][N-1]

    return dp[M-1][N-1], ruta


# ─────────────────────────────────────────────────
# PRUEBA
# ─────────────────────────────────────────────────
grid = [
    [ 1, -2,  3,  4],
    [ 5,  6, -7,  8],
    [-1,  2,  9, -3],
    [ 4, -5,  1,  2]
]

suma, ruta = max_suma_ruta(grid)

print(f"Suma máxima: {suma}")
print(f"Ruta: {ruta}")
print("\nCuadrícula con ruta marcada (*):")
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in ruta:
            print(f"[{grid[i][j]:3}*]", end="")
        else:
            print(f"[{grid[i][j]:4}]", end="")
    print()
