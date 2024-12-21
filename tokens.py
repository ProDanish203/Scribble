class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)


class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)


class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR", value)


class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOL", value)


class Comparison(Token):
    def __init__(self, value):
        super().__init__("COMP", value)


class Reserved(Token):
    def __init__(self, value):
        super().__init__("RSV", value)


class Emoji(Token):
    def __init__(self, value):
        super().__init__("EMOJI", value)


class String(Token):
    def __init__(self, value):
        super().__init__("STR", value)


class Keyword(Token):
    def __init__(self, value):
        super().__init__("KEY", value)


class Command(Token):
    def __init__(self, value):
        super().__init__("CMD", value)


# Alias tokens for user-defined keywords, i.e., when users define their own shorthand for commands
class Alias(Token):
    def __init__(self, value):
        super().__init__("ALIAS", value)
