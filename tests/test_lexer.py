import unittest

from compipy.lexer import Lexer
from compipy.tokens import TokenType as T


class TestLexer(unittest.TestCase):
    def test_next_token(self):
        source = """let five = 5;
let ten = 10;

function add(x, y) {
  return x + y;
}

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) {
	return true;
} else {
	return false;
}

elif {
	break;
}

for while

10 == 10;
10 != 9;
10 <= 10;
10 >= 9;
2 ** 3;
"""
        expected = [
            (T.LET, "let"), (T.IDENT, "five"), (T.ASSIGN, "="), (T.INT, "5"), (T.SEMICOLON, ";"),
            (T.LET, "let"), (T.IDENT, "ten"), (T.ASSIGN, "="), (T.INT, "10"), (T.SEMICOLON, ";"),
            (T.FUNCTION, "function"), (T.IDENT, "add"), (T.LPAREN, "("), (T.IDENT, "x"),
            (T.COMMA, ","), (T.IDENT, "y"), (T.RPAREN, ")"), (T.LBRACE, "{"),
            (T.RETURN, "return"), (T.IDENT, "x"), (T.PLUS, "+"), (T.IDENT, "y"),
            (T.SEMICOLON, ";"), (T.RBRACE, "}"),
            (T.LET, "let"), (T.IDENT, "result"), (T.ASSIGN, "="), (T.IDENT, "add"),
            (T.LPAREN, "("), (T.IDENT, "five"), (T.COMMA, ","), (T.IDENT, "ten"),
            (T.RPAREN, ")"), (T.SEMICOLON, ";"),
            (T.BANG, "!"), (T.MINUS, "-"), (T.SLASH, "/"), (T.ASTERISK, "*"), (T.INT, "5"),
            (T.SEMICOLON, ";"),
            (T.INT, "5"), (T.LT, "<"), (T.INT, "10"), (T.GT, ">"), (T.INT, "5"), (T.SEMICOLON, ";"),
            (T.IF, "if"), (T.LPAREN, "("), (T.INT, "5"), (T.LT, "<"), (T.INT, "10"),
            (T.RPAREN, ")"), (T.LBRACE, "{"), (T.RETURN, "return"), (T.TRUE, "true"),
            (T.SEMICOLON, ";"), (T.RBRACE, "}"), (T.ELSE, "else"), (T.LBRACE, "{"),
            (T.RETURN, "return"), (T.FALSE, "false"), (T.SEMICOLON, ";"), (T.RBRACE, "}"),
            (T.ELIF, "elif"), (T.LBRACE, "{"), (T.BREAK, "break"), (T.SEMICOLON, ";"),
            (T.RBRACE, "}"),
            (T.FOR, "for"), (T.WHILE, "while"),
            (T.INT, "10"), (T.EQ, "=="), (T.INT, "10"), (T.SEMICOLON, ";"),
            (T.INT, "10"), (T.NOT_EQ, "!="), (T.INT, "9"), (T.SEMICOLON, ";"),
            (T.INT, "10"), (T.LTE, "<="), (T.INT, "10"), (T.SEMICOLON, ";"),
            (T.INT, "10"), (T.GTE, ">="), (T.INT, "9"), (T.SEMICOLON, ";"),
            (T.INT, "2"), (T.POW, "**"), (T.INT, "3"), (T.SEMICOLON, ";"),
            (T.EOF, ""),
        ]

        lexer = Lexer(source)
        for i, (exp_type, exp_literal) in enumerate(expected):
            tok = lexer.next_token()
            self.assertEqual(tok.type, exp_type,
                             f"tests[{i}] - tokentype wrong. expected={exp_type!r}, got={tok.type!r}")
            self.assertEqual(tok.literal, exp_literal,
                             f"tests[{i}] - literal wrong. expected={exp_literal!r}, got={tok.literal!r}")

    def test_illegal(self):
        tok = Lexer("@").next_token()
        self.assertEqual(tok.type, T.ILLEGAL)
        self.assertEqual(tok.literal, "@")


if __name__ == "__main__":
    unittest.main()
