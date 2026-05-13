# Respuestas — Cambio de Monedas (Algoritmo Greedy)

**Problema:** entregar cambio por **93 unidades** usando monedas de 50, 20, 10, 5, 2 y 1.

---

## 1. ¿Qué monedas selecciona el algoritmo greedy?

El algoritmo toma siempre la moneda de mayor valor posible sin superar el restante:

| Paso | Moneda | Cantidad | Restante |
|------|--------|----------|----------|
| 1    | 50     | 1        | 43       |
| 2    | 20     | 2        | 3        |
| 3    | 10     | 0        | 3        |
| 4    | 5      | 0        | 3        |
| 5    | 2      | 1        | 1        |
| 6    | 1      | 1        | 0        |

**Monedas seleccionadas:** 1×50, 2×20, 1×2, 1×1

Verificación: `50 + 20 + 20 + 2 + 1 = 93` ✓

---

## 2. ¿Cuántas monedas se usan en total?

**5 monedas** (1 + 2 + 0 + 0 + 1 + 1).

---

## 3. ¿Por qué el algoritmo toma esa decisión en cada paso?

El algoritmo greedy aplica la heurística de **elección local óptima**: en cada paso selecciona la moneda de mayor denominación que no exceda el monto restante, con el objetivo de reducir el residuo lo más rápido posible.

- **Paso 1 — moneda de 50:** es la mayor que cabe en 93, reduce el problema a 43.
- **Paso 2 — moneda de 20 (×2):** es la mayor que cabe en 43; se toma dos veces (43→23→3).
- **Pasos 3 y 4 — monedas de 10 y 5:** no caben en 3, se descartan.
- **Paso 5 — moneda de 2:** la mayor que cabe en 3, queda residuo 1.
- **Paso 6 — moneda de 1:** cubre el último residuo exactamente.

La decisión en cada paso es **irrevocable**: una vez elegida una moneda no se reconsidera.

---

## 4. ¿Siempre garantiza la solución óptima? Justifique.

**No siempre**, aunque para este sistema de monedas canónico (1, 2, 5, 10, 20, 50) sí lo hace.

El algoritmo greedy garantiza la solución óptima únicamente cuando el sistema de monedas es **canónico**, es decir, cuando cada denominación es múltiplo o complemento de las anteriores de forma que la elección local nunca bloquea una solución global mejor.

**Contraejemplo** con monedas no canónicas `{1, 3, 4}` para cambio de **6**:
- Greedy: 4 + 1 + 1 → **3 monedas**
- Óptimo: 3 + 3 → **2 monedas**

Para el sistema `{1, 2, 5, 10, 20, 50}` el greedy siempre produce la solución óptima porque las denominaciones están diseñadas para ello.
