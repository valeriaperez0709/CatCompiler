"""Consola interactiva (Read-Eval-Print Loop) para probar el Lexer."""
import sys
from typing import TextIO

from compipy.lexer import Lexer
from compipy.tokens import TokenType

PROMPT = ">> "


def start(inp: TextIO = sys.stdin, out: TextIO = sys.stdout) -> None:
    while True:
        out.write(PROMPT)
        out.flush()
        line = inp.readline()
        if not line:  # EOF (Ctrl+D / Ctrl+Z)
            return

        line = line.rstrip("\n")
        if line.strip().lower() in ("exit", "salir"):
            out.write("¡Miau! Nos vemos. Saliendo de CatCompiler...\n")
            return

        lexer = Lexer(line)
        tok = lexer.next_token()
        while tok.type != TokenType.EOF:
            out.write(f"{tok}\n")
            tok = lexer.next_token()
