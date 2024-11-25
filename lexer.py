from tokens import (
    Declaration,
    Float,
    Integer,
    Boolean,
    Operator,
    Variable,
    Comparison,
    Keyword,
)


class Lexer:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    operators = "+-*/()="
    ws = [" ", "\n", "\t"]  # whitespace
    boolean = [
        "and",
        "or",
        "not",
    ]
    decalrations = ["create"]
    comparsion = ["?=", "<>", "<", ">", "<=", ">="]
    special_characters = "><=?"
    # keywords = ["if", "elseif", "else", "repeat", "do"]

    def __init__(self, text):
        self.text = text  # input string
        self.idx = 0  # current position in input
        self.tokens = []  # list of tokens
        self.current_char = self.text[self.idx]  # current character
        self.token = None  # current token

    def advance(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.current_char = self.text[self.idx]

    def tokenize(self):
        while self.idx < len(self.text):
            # Handle Whitespace
            if self.current_char in self.ws:
                self.advance()
                continue
            # Handle Digits
            elif self.current_char in self.digits:
                self.token = self.extract_number()

            # Handle Operators
            elif self.current_char in self.operators:
                self.token = self.extract_operator()

            # Handle Letters
            elif self.current_char in self.letters:
                word = self.extract_word()
                if word in Lexer.decalrations:
                    self.token = Declaration(word)
                elif word in Lexer.boolean:
                    self.token = Boolean(word)
                else:
                    self.token = Variable(word)

            # Handle Special Characters
            elif self.current_char in Lexer.special_characters:
                comparisonOpeartor = ""
                while self.current_char in Lexer.special_characters and self.idx < len(
                    self.text
                ):
                    comparisonOpeartor += self.current_char
                    self.advance()

                self.token = Comparison(comparisonOpeartor)

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self):
        number = ""
        is_float = False
        while (self.current_char in Lexer.digits or self.current_char == ".") and (
            self.idx < len(self.text)
        ):
            if self.current_char == ".":
                is_float = True
            number += self.current_char
            self.advance()

        return Integer(number) if not is_float else Float(number)

    def extract_operator(self):
        operator = self.current_char
        self.advance()
        return Operator(operator)

    def extract_word(self):
        word = ""
        while self.current_char in Lexer.letters and self.idx < len(self.text):
            word += self.current_char
            self.advance()

        return word
