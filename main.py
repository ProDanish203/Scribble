
from data import Data
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def run_scribble():
    base = Data()
    interpreter = Interpreter(None, base)

    while True:
        try:
            text = input("Scribble> ")

            lexer = Lexer(text)
            tokens = lexer.tokenize()
            print(tokens)

            parser = Parser(tokens)
            tree = parser.parse()
            print(tree)

            interpreter.tree = tree
            result = interpreter.interpret()
            print(result)

            if result and result.type.startswith('VAR'):
                print(f"Current value: {base.read(result.value)}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_scribble()