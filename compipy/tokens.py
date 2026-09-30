"""Definición de los tipos de tokens que reconoce el Lexer."""
from dataclasses import dataclass
from enum import Enum


class TokenType(str, Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identificadores + literales
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"      # 1343456

    # Operadores
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="

    EQ = "=="
    NOT_EQ = "!="

    POW = "**"

    # Delimitadores
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    LBRACKET = "["
    RBRACKET = "]"

    # Palabras reservadas
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    ELIF = "ELIF"
    RETURN = "RETURN"
    FOR = "FOR"
    WHILE = "WHILE"
    BREAK = "BREAK"

    def __str__(self) -> str:
        return self.value


@dataclass
class Token:
    type: TokenType
    literal: str

    def __str__(self) -> str:
        # Mismo formato de Go: {Type:LET Literal:let}
        return f"{{Type:{self.type.value} Literal:{self.literal}}}"


KEYWORDS: dict[str, TokenType] = {
    "function": TokenType.FUNCTION,
    "let": TokenType.LET,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "elif": TokenType.ELIF,
    "return": TokenType.RETURN,
    "for": TokenType.FOR,
    "while": TokenType.WHILE,
    "break": TokenType.BREAK,
}


def lookup_ident(ident: str) -> TokenType:
    """Retorna el tipo de palabra reservada o IDENT si no lo es."""
    return KEYWORDS.get(ident, TokenType.IDENT)
