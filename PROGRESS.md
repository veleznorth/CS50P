# Progreso CS50P

## Estado actual
- **Set activo:** Set 3
- **Ultimo ejercicio completado:** Outdated
- **Siguiente ejercicio:** Set 4

---

## Set 3 — Exceptions

| Ejercicio     | Estado     | Nota  | Archivo              |
|---------------|------------|-------|----------------------|
| Fuel Gauge    | Completado | 9/10  | `set3/fuel.py`       |
| Taqueria      | Completado | 10/10 | `set3/taqueria.py`   |
| Grocery List  | Completado | 9.5/10 | `set3/grocery.py`  |
| Outdated      | Completado | 8.5/10 | `set3/outdated.py` |

---

## Set 2 — Loops

| Ejercicio     | Estado     | Nota | Archivo           |
|---------------|------------|------|-------------------|
| Camel Case    | Completado | 9    | `set2/camel.py`   |
| Coke Machine  | Completado | 9    | `set2/coke.py`    |
| Twttr         | Completado | 9.5  | `set2/twttr.py`   |
| Vanity Plates | Completado | 9.5  | `set2/plates.py`  |
| Nutrition     | Completado | 9    | `set2/nutrition.py` |

---

## Set 1 — Conditionals

| Ejercicio            | Estado    | Nota | Archivo |
|----------------------|-----------|------|---------|
| Deep Thought         | Completado | 9    | `set1/deep.py`        |
| Home Federal Savings | Completado | 10   | `set1/bank.py`        |
| File Extensions      | Completado | 10   | `set1/extensions.py`  |
| Math Interpreter     | Completado | 10   | `set1/interpreter.py` |
| Meal Time            | Completado | 9.5  | `set1/meal.py`        |

---

## Set 0 — Functions, Variables

| Ejercicio       | Estado      | Nota  | Archivo               |
|-----------------|-------------|-------|-----------------------|
| Indoor Voice    | Completado  | 8.5   | `set0/indoor.py`      |
| Playback Speed  | Completado  | 10    | `set0/playback.py`    |
| Making Faces    | Completado  | 10    | `set0/faces.py`       |
| Einstein        | Completado  | 10    | `set0/einstein.py`    |
| Tip Calculator  | Completado  | 10    | `set0/tip.py`         |

---

## Notas de aprendizaje

- `input()` siempre devuelve `str`, no hace falta envolverlo en `str()`.
- Los metodos built-in de `str` (como `.replace()`) solo aceptan argumentos posicionales, no keyword arguments.
- `check50` importa el archivo y llama las funciones por nombre exacto — respetar los nombres que pide el enunciado.
- Para problemas simples de Set 0, preferir soluciones de 1-2 lineas sin funciones auxiliares innecesarias.

---

## Historial de sesiones

### 2026-04-14
- Creado entorno del curso y `CLAUDE.md`.
- Revisado y calificado `indoor.py` (8.5/10) — correcto pero sobre-engineered.
- Revisado y calificado `playback.py` (10/10) — solucion perfecta de una linea.
- Aprendido: diferencia entre keyword args y positional args en metodos built-in.

### 2026-04-14 (continuacion)
- Completado `faces.py` (10/10) tras corregir emoticon `:(` y nombre de funcion `convert`.
- Aprendido: respetar nombres de funciones exactos que pide el enunciado porque `check50` los llama directamente.

### 2026-04-17
- Completado Set 1 completo (Conditionals).
- `deep.py` (9/10) — `match` bien usado, prompt tenia texto en español.
- `bank.py` (10/10) — limpio, `startswith` bien aplicado.
- `extensions.py` (10/10) — case-insensitive con `.lower()`, `or` para multiples extensiones.
- `interpreter.py` (10/10) — `match` para operadores, formato `:.1f`, validacion extra division/0.
- `meal.py` (9.5/10) — `convert` con aritmetica de tiempo, `__name__` guard bien usado, comentarios obvios restan.
- Aprendido: `endswith` acepta tupla para multiples sufijos (aunque no se uso aun — se usara en Set 2+).
- Aprendido: `__name__ == "__main__"` guard es buena practica profesional.

### 2026-04-29 (continuacion)
- Completado `outdated.py` (8.5/10) — dos formatos de fecha (slash y texto), try/except anidado, re-prompt con while True.
- Bug inicial: variable `day` usada fuera de su scope — UnboundLocalError.
- Aprendido: `except A, B, C:` es sintaxis valida en Python 3 (se parsea como tuple).
- Aprendido: trazar mentalmente con valor concreto antes de correr — detecta bugs de scope sin ejecutar.
- Aprendido: papel para problemas complejos, traza mental para problemas simples. Umbral sube con practica.
- Pendiente mejorar: `except:` desnudo oculta bugs reales, usar `except Exception:`.

### 2026-04-29
- Completado `grocery.py` (9.5/10) — sorted(set()) para orden alfabetico sin duplicados, .count() para frecuencia.
- Completado `taqueria.py` (10/10) — dict lookup con KeyError, EOFError para Ctrl+D, .title() para normalizar.
- Re-implementado `fuel.py` (9/10) usando try/except — enfoque mas pythónico que version anterior.
- Primera version usaba DFA con 4 estados; esta version usa try/except con else.
- Pendiente: espacios PEP 8 alrededor de operadores de asignacion.

### 2026-04-28
- Completado Set 3 primer ejercicio: `fuel.py` (9.5/10) — primera version.
- DFA implementado desde cero con 4 estados (-1, 1, 2, 3) para validar formato X/Y.
- Maneja edge cases sin try/except — validacion por construccion del automata.

### 2026-04-25
- Completado Set 2 primeros dos ejercicios.
- `camel.py` (9/10) — logica correcta, loop + isupper() bien usados.
- `coke.py` (9/10) — `match` para monedas, balance acumulado, cambio correcto.
- Configurado Black formatter en VS Code para formateo automatico PEP 8 al guardar.
