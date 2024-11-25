class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", value)


class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOL", value)


class Operator(Token):
    def __init__(self, value):
        super().__init__("OP", value)


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)


class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR(?)", value)


class Comparison(Token):
    def __init__(self, value):
        super().__init__("COMP", value)


class Keyword(Token):
    def __init__(self, value):
        super().__init__("KEYWORD", value)