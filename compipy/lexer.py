"""Analizador léxico: transforma el código fuente en una secuencia de tokens."""
from compipy.tokens import Token, TokenType, lookup_ident

# Operadores de un carácter que no tienen variante de dos caracteres
SINGLE_CHAR_TOKENS: dict[str, TokenType] = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "/": TokenType.SLASH,
    ";": TokenType.SEMICOLON,
    ",": TokenType.COMMA,
    "{": TokenType.LBRACE,
    "}": TokenType.RBRACE,
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN,
    "[": TokenType.LBRACKET,
    "]": TokenType.RBRACKET,
}

# Operadores que pueden ser de uno o dos caracteres:
# carácter -> (tipo simple, segundo carácter esperado, tipo doble)
TWO_CHAR_TOKENS: dict[str, tuple[TokenType, str, TokenType]] = {
    "=": (TokenType.ASSIGN, "=", TokenType.EQ),
    "!": (TokenType.BANG, "=", TokenType.NOT_EQ),
    "*": (TokenType.ASTERISK, "*", TokenType.POW),
    "<": (TokenType.LT, "=", TokenType.LTE),
    ">": (TokenType.GT, "=", TokenType.GTE),
}

NUL = ""  # equivalente al byte 0 de Go: indica fin de la entrada


class Lexer:
    """Mantiene el estado del código fuente que se está analizando."""

    def __init__(self, source: str) -> None:
        self.input = source
        self.position = 0       # posición actual (apunta al carácter actual)
        self.read_position = 0  # siguiente posición de lectura
        self.ch = NUL           # carácter actual bajo examen
        self._read_char()

    def _read_char(self) -> None:
        """Avanza los punteros y actualiza el carácter actual."""
        if self.read_position >= len(self.input):
            self.ch = NUL
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def _peek_char(self) -> str:
        """Mira el siguiente carácter sin avanzar los punteros."""
        if self.read_position >= len(self.input):
            return NUL
        return self.input[self.read_position]

    def next_token(self) -> Token:
        """Evalúa el carácter actual y retorna el token correspondiente."""
        self._skip_whitespace()
        ch = self.ch

        if ch in TWO_CHAR_TOKENS:
            single, second, double = TWO_CHAR_TOKENS[ch]
            if self._peek_char() == second:
                self._read_char()
                tok = Token(double, ch + self.ch)
            else:
                tok = Token(single, ch)
        elif ch in SINGLE_CHAR_TOKENS:
            tok = Token(SINGLE_CHAR_TOKENS[ch], ch)
        elif ch == NUL:
            tok = Token(TokenType.EOF, "")
        elif _is_letter(ch):
            literal = self._read_identifier()
            return Token(lookup_ident(literal), literal)
        elif _is_digit(ch):
            return Token(TokenType.INT, self._read_number())
        else:
            tok = Token(TokenType.ILLEGAL, ch)

        self._read_char()
        return tok

    def _skip_whitespace(self) -> None:
        while self.ch in (" ", "\t", "\n", "\r"):
            self._read_char()

    def _read_identifier(self) -> str:
        start = self.position
        while _is_letter(self.ch):
            self._read_char()
        return self.input[start:self.position]

    def _read_number(self) -> str:
        start = self.position
        while _is_digit(self.ch):
            self._read_char()
        return self.input[start:self.position]

    def __iter__(self):
        """Permite recorrer los tokens con un for (sin incluir EOF)."""
        tok = self.next_token()
        while tok.type != TokenType.EOF:
            yield tok
            tok = self.next_token()


def _is_letter(ch: str) -> bool:
    """Letras ASCII o guion bajo (permite identificadores como mi_variable)."""
    return ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ch == "_"


def _is_digit(ch: str) -> bool:
    return "0" <= ch <= "9"
