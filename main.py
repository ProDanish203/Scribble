from data import Data
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

base = Data()

while True:
    try:
        text = input("Scribble> ")

        lexer = Lexer(text)
        tokens = lexer.tokenize()

        print(tokens)

        parser = Parser(tokens)
        tree = parser.parse()

        print(tree)

        interpreter = Interpreter(tree, base)
        result = interpreter.interpret()

        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

    #if 2 greater than 1 do make x = 5