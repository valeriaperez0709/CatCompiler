# CatCompiler (versión Python)

## Estructura

* `compipy/tokens.py` — tipos de token (`TokenType`), clase `Token`, palabras reservadas y `lookup_ident`.
* `compipy/lexer.py` — analizador léxico (`Lexer.next_token()`).
* `compipy/repl.py` — consola interactiva.
* `main.py` — punto de entrada con el banner de Limón.
* `tests/test_lexer.py` — pruebas unitarias (mismas que `lexer_test.go`).

Requiere Python 3.10+ y no usa librerías externas.

## Cómo probarlo

```bash
python main.py
```

Escribe `salir` o `exit` para terminar.

## Pruebas

```bash
python -m unittest -v
```
# catcompiler-py
