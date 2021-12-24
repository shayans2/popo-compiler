from lex import *


def main():
    input = "IF+-123 foo*THEN/"
    lexer = Lexer(input)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.text, token.kind)
        token = lexer.getToken()
        continue


main()
