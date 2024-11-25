class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

    def parse(self):
        return self.statement()

    def factor(self):
        token = self.token
        if token.type in ["INT", "FLOAT"]:
            return self.token
        # Parentheses
        elif token.value == "(":
            self.advance()
            expression = self.boolean_expr()
            return expression

        # Variable
        elif token.type.startswith("VAR"):
            return self.token

        # Not Operator
        elif token.value == "not":
            operator = self.token
            self.advance()
            operand = self.boolean_expr()

            return [operator, operand]

        # Unary Operator
        elif self.token.value in ["+", "-"]:
            operator = self.token
            self.advance()
            operand = self.boolean_expr()

            return [operator, operand]

    # e.g 2 * 3 -> [2, *, 3]
    def term(self):
        left_node = self.factor()
        if left_node is None:
            return None
        self.advance()
        while self.token.value in ["*", "/"]:
            operation = self.token
            self.advance()
            right_node = self.factor()
            if right_node is None:
                return None
            self.advance()
            left_node = [left_node, operation, right_node]

        return left_node

    def expr(self):
        left_node = self.term()
        if left_node is None:
            return None
        while self.token.value in ["+", "-"]:
            operation = self.token
            self.advance()
            right_node = self.term()
            if right_node is None:
                return None
            left_node = [left_node, operation, right_node]

        return left_node

    def statement(self):
        if self.token.type == "DECL":
            # Variable Assignment
            self.advance()
            left_node = self.variable()
            self.advance()
            if self.token.value == "=":

                operation = self.token
                self.advance()
                right_node = self.boolean_expr()

                return [left_node, operation, right_node]

        elif self.token.type in ["INT", "FLOAT", "OP"] or self.token.value == "not":
            return self.boolean_expr()

    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token

    def comp_expr(self):
        left_node = self.expr()
        while self.token.type == "COMP":
            operator = self.token
            self.advance()
            right_node = self.expr()
            left_node = [left_node, operator, right_node]
        return left_node

    def boolean_expr(self):
        left_node = self.comp_expr()
        while self.token.value == "and" or self.token.value == "or":
            operation = self.token
            self.advance()
            right_node = self.comp_expr()
            left_node = [left_node, operation, right_node]

        return left_node
