IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
ADD = 'ADD'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'
POWER = 'POWER'
LEFT_PAREN = 'LEFT_PAREN'
RIGHT_PAREN = 'RIGHT_PAREN'
ASSIGN = 'ASSIGN'
EQUAL = 'EQUAL'
NOT_EQUAL = 'NOT_EQUAL'
GREATER = 'GREATER'
GREATER_EQUAL = 'GREATER_EQUAL'
LESS_EQUAL = 'LESS_EQUAL'
LESS = 'LESS'
OR = 'OR'
AND = 'AND'
LEFT_BRACKET = 'LEFT_BRACKET'
RIGHT_BRACKET = 'RIGHT_BRACKET'
LEFT_BRACE = 'LEFT_BRACE'
RIGHT_BRACE = 'RIGHT_BRACE'
WHILE = 'WHILE'
FOR = 'FOR'
IF = 'IF'
ELSE = 'ELSE'
SEMICOLON = 'SEMICOLON'
END = 'END'
STRING = 'STRING'
PRINTF = 'PRINTF'
MIN = 'MIN'
MAX = 'MAX'
SQUARE = 'SQUARE'
ISUPPER = 'ISUPPER'
ISLOWER = 'ISLOWER'
CONCAT = 'CONCAT'
COMMA = 'COMMA'
ARRAY = 'ARRAY'
TUPLE = 'TUPLE'
LEN = 'LEN'
REMOVE = 'REMOVE'
APPEND = 'APPEND'
ADD_TUPLE = 'ADD_TUPLE'
SORT_TUPLE = 'SORT_TUPLE'
SPLIT = 'SPLIT'
REPLACE = 'REPLACE'


class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        if self.code:
            self.current_char = self.code[self.pos]

    def increase(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.current_char = self.code[self.pos]
        else:
            self.current_char = None

    def identifier(self):
        result = ''
        #reading chars and _
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char == '_'):
            result += self.current_char
            self.increase()
        if result == 'if':
            return (IF, result)
        elif result == 'else':
            return (ELSE, result)
        elif result == 'while':
            return (WHILE, result)
        elif result == 'for':
            return (FOR, result)
        elif result == 'printf':
            return (PRINTF, result)
        elif result == 'MIN':
            return (MIN, result)
        elif result == 'MAX':
            return (MAX, result)
        elif result == 'ISUPPER':
            return (ISUPPER, result)
        elif result == 'ISLOWER':
            return (ISLOWER, result)
        elif result == 'CONCAT':
            return (CONCAT, result)
        elif result == 'SQUARE':
            return (SQUARE, result)
        elif result == 'ARRAY':
            return (ARRAY, result)
        elif result == 'TUPLE':
            return (TUPLE, result)
        elif result == 'ADD_TUPLE':
            return ('ADD_TUPLE', result)
        elif result == 'SORT_TUPLE':
            return ('SORT_TUPLE', result)
        elif result == 'LEN':
            return (LEN, 'LEN')
        elif result == 'REMOVE':
            return (REMOVE, 'REMOVE')
        elif result == 'APPEND':
            return (APPEND, 'APPEND')
        elif result == 'SPLIT':
            return (SPLIT, 'SPLIT')
        elif result == 'REPLACE':
            return (REPLACE, 'REPLACE')
        else:
            return (IDENTIFIER, result)

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.increase()

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.increase()
        return (NUMBER, result)

    def string(self):
        result = ''
        self.increase()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.increase()
        self.increase()
        return (STRING, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char == '+':
                self.increase()
                return (ADD, '+')

            if self.current_char == '-':
                self.increase()
                return (SUB, '-')

            if self.current_char == '*':
                self.increase()
                if self.current_char == '*':
                    self.increase()
                    return (POWER, '**')
                return (MUL, '*')

            if self.current_char == '/':
                self.increase()
                return (DIV, '/')

            if self.current_char == '(':
                self.increase()
                return (LEFT_PAREN, '(')

            if self.current_char == ')':
                self.increase()
                return (RIGHT_PAREN, ')')

            if self.current_char == '=':
                self.increase()
                if self.current_char == '=':
                    self.increase()
                    return (EQUAL, '==')
                return (ASSIGN, '=')

            if self.current_char == '>':
                self.increase()
                if self.current_char == '=':
                    self.increase()
                    return (GREATER_EQUAL, '>=')
                return (GREATER, '>')

            if self.current_char == '<':
                self.increase()
                if self.current_char == '=':
                    self.increase()
                    return (LESS_EQUAL, '<=')
                return (LESS, '<')

            if self.current_char == '!':
                self.increase()
                if self.current_char == '=':
                    self.increase()
                    return (NOT_EQUAL, '!=')
                raise SyntaxError(f'Illegal character: {self.current_char}')

            if self.current_char == '&':
                self.increase()
                if self.current_char == '&':
                    self.increase()
                    return (AND, '&&')
                raise SyntaxError(f'Illegal character: {self.current_char}')

            if self.current_char == '|':
                self.increase()
                if self.current_char == '|':
                    self.increase()
                    return (OR, '||')
                raise SyntaxError(f'Illegal character: {self.current_char}')

            if self.current_char == '[':
                self.increase()
                return (LEFT_BRACKET, '[')

            if self.current_char == ']':
                self.increase()
                return (RIGHT_BRACKET, ']')

            if self.current_char == '{':
                self.increase()
                return (LEFT_BRACE, '{')

            if self.current_char == '}':
                self.increase()
                return (RIGHT_BRACE, '}')

            if self.current_char == '"':
                return self.string()

            if self.current_char == ';':
                self.increase()
                return (SEMICOLON, ';')

            if self.current_char == ',':
                self.increase()
                return (COMMA, ',')

            raise SyntaxError(f'Illegal character: {self.current_char}')

        return (END, None)

    def split(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token[0] == END:
                break
        return tokens


#############################
# AST node classes
class ASTNode:
    """Base class for all AST nodes."""
    pass


class IndexAccess(ASTNode):
    """Represents accessing an element by index (e.g., a[2])."""

    def __init__(self, name, index):
        self.name = name
        self.index = index


class Program(ASTNode):
    """Represents the entire program consisting of multiple statements."""

    def __init__(self, statements):
        self.statements = statements


class ExpressionStatement(ASTNode):
    """Represents a statement consisting of a single expression."""

    def __init__(self, expression):
        self.expression = expression


class Assign(ASTNode):
    """Represents a variable assignment."""

    def __init__(self, name, value):
        self.name = name
        self.value = value


class BinaryExpression(ASTNode):
    """Represents a binary expression (e.g., a + b)."""

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryExpression(ASTNode):
    """Represents a unary expression (e.g., -a)."""

    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class Literal(ASTNode):
    """Represents a literal value."""

    def __init__(self, value):
        self.value = value


class Variable(ASTNode):
    """Represents a variable."""

    def __init__(self, name):
        self.name = name


class IfStatement(ASTNode):
    """Represents an if statement."""

    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class WhileStatement(ASTNode):
    """Represents a while loop."""

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForStatement(ASTNode):
    """Represents a for loop."""

    def __init__(self, initializer, condition, increment, body):
        self.initializer = initializer
        self.condition = condition
        self.increment = increment
        self.body = body


class PrintfStatement(ASTNode):
    """Represents a printf statement."""

    def __init__(self, expression):
        self.expression = expression


class Block(ASTNode):
    """Represents a block of statements."""

    def __init__(self, statements):
        self.statements = statements


class FunctionCall(ASTNode):
    """Represents a function call (e.g., MIN(a, b))."""

    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class Parser:
    """
    The parser class is responsible for converting a list of tokens into an abstract syntax tree (AST).
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def advance(self):
        """Move to the next token."""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def peek(self):
        """Look at the current token without advancing."""
        return self.tokens[self.current]

    def previous(self):
        """Get the previous token."""
        return self.tokens[self.current - 1]

    def is_at_end(self):
        """Check if we have reached the end of the token list."""
        return self.peek()[0] == END

    def parse(self):
        """Parse the token list into an AST."""
        statements = []
        if self.is_at_end():  # Handle empty code
            print("Empty code detected.")
            return Program(statements)
        while not self.is_at_end():
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        """Parse a single statement."""
        if self.check(IDENTIFIER) and self.peek_ahead(1)[0] == ASSIGN:
            return self.assignment_statement()
        if self.check(IF):
            return self.if_statement()
        if self.check(WHILE):
            return self.while_statement()
        if self.check(FOR):
            return self.for_statement()
        if self.check(PRINTF):
            return self.printf_statement()
        return self.expression_statement()

    def if_statement(self):
        """Parse an if statement."""
        self.consume(IF, "Expect 'if' keyword.")
        self.consume(LEFT_PAREN, "Expect '(' after 'if'.")
        condition = self.expression()
        self.consume(RIGHT_PAREN, "Expect ')' after condition.")
        self.consume(LEFT_BRACE, "Expect '{' after condition.")
        then_branch = self.block()
        self.consume(RIGHT_BRACE, "Expect '}' after 'if' block.")

        else_branch = None
        if self.check(ELSE):
            self.advance()
            self.consume(LEFT_BRACE, "Expect '{' after 'else'.")
            else_branch = self.block()
            self.consume(RIGHT_BRACE, "Expect '}' after 'else' block.")

        return IfStatement(condition, then_branch, else_branch)

    def while_statement(self):
        """Parse a while loop."""
        self.consume(WHILE, "Expect 'while' keyword.")
        self.consume(LEFT_PAREN, "Expect '(' after 'while'.")
        condition = self.expression()
        self.consume(RIGHT_PAREN, "Expect ')' after condition.")
        self.consume(LEFT_BRACE, "Expect '{' after condition.")
        body = self.block()
        self.consume(RIGHT_BRACE, "Expect '}' after while block.")
        return WhileStatement(condition, body)

    def for_statement(self):
        """Parse a for loop."""
        self.consume(FOR, "Expect 'for' keyword.")
        self.consume(LEFT_PAREN, "Expect '(' after 'for'.")

        # Parse initializer (can be empty)
        if not self.check(SEMICOLON):
            initializer = self.assignment_statement()
        else:
            initializer = None
            self.consume(SEMICOLON, "Expect ';' after initializer.")

        # Parse condition (can be empty)
        if not self.check(SEMICOLON):
            condition = self.expression()
        else:
            condition = Literal(True)  # Default condition to True if none is provided
        self.consume(SEMICOLON, "Expect ';' after condition.")

        # Parse increment (can be empty)
        if not self.check(RIGHT_PAREN):
            increment = self.assignment_statement()
        else:
            increment = None

        # Consume the closing parenthesis
        self.consume(RIGHT_PAREN, "Expect ')' after increment.")

        # Parse the loop body
        self.consume(LEFT_BRACE, "Expect '{' after 'for'.")
        body = self.block()
        self.consume(RIGHT_BRACE, "Expect '}' after 'for' block.")

        return ForStatement(initializer, condition, increment, body)

    def printf_statement(self):
        """Parse a printf statement."""
        self.consume(PRINTF, "Expect 'printf' keyword.")
        self.consume(LEFT_PAREN, "Expect '(' after 'printf'.")
        expr = self.expression()
        self.consume(RIGHT_PAREN, "Expect ')' after expression.")
        self.consume(SEMICOLON, "Expect ';' after 'printf' statement.")
        return PrintfStatement(expr)

    def assignment_statement(self):
        """Parse an assignment statement."""
        name = self.advance()[1]
        self.consume(ASSIGN, "Expect '=' after identifier.")
        value = self.expression()
        self.consume(SEMICOLON, "Expect ';' after expression.")
        return Assign(name, value)

    def expression_statement(self):
        """Parse an expression statement."""
        expr = self.expression()
        self.consume(SEMICOLON, "Expect ';' after expression.")
        return ExpressionStatement(expr)

    def expression(self):
        """Parse an expression."""
        return self.logical_or()

    def logical_or(self):
        """Parse logical OR operations."""
        expr = self.logical_and()

        while self.match(OR):
            operator = self.previous()
            right = self.logical_and()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def logical_and(self):
        """Parse logical AND operations."""
        expr = self.equality()

        while self.match(AND):
            operator = self.previous()
            right = self.equality()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def equality(self):
        """Parse an equality expression."""
        expr = self.comparison()

        while self.match(EQUAL, NOT_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def comparison(self):
        """Parse a comparison expression."""
        expr = self.term()

        while self.match(GREATER, GREATER_EQUAL, LESS, LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = BinaryExpression(expr, operator, right)

        return expr

    def term(self):
        """Parse a term (addition and subtraction)."""
        expr = self.factor()
        while self.match(ADD, SUB):
            operator = self.previous()
            right = self.factor()
            expr = BinaryExpression(expr, operator, right)
        return expr

    def factor(self):
        """Parse a factor (multiplication, division, and power)."""
        expr = self.unary()
        while self.match(MUL, DIV, POWER):
            operator = self.previous()
            right = self.unary()
            expr = BinaryExpression(expr, operator, right)
        return expr

    def unary(self):
        """Parse a unary expression (e.g., -a)."""
        if self.match(SUB):
            operator = self.previous()
            operand = self.unary()
            return UnaryExpression(operator, operand)
        return self.primary()

    def primary(self):
        """Parse a primary expression (literals, variables, and function calls)."""
        if self.match(NUMBER):
            return Literal(self.previous()[1])
        if self.match(STRING):
            return Literal(self.previous()[1])
        if self.match(MIN, MAX, ISUPPER, ISLOWER, CONCAT, SQUARE, ARRAY, TUPLE, LEN, APPEND, REMOVE, 'ADD_TUPLE',
                      'SORT_TUPLE', 'SPLIT', 'REPLACE'):
            function_name = self.previous()[1]
            self.consume(LEFT_PAREN, "Expect '(' after function name.")
            args = []
            while not self.check(RIGHT_PAREN):
                args.append(self.expression())
                if not self.check(RIGHT_PAREN):
                    self.consume(COMMA, "Expect ',' between arguments.")
            self.consume(RIGHT_PAREN, "Expect ')' after arguments.")
            return FunctionCall(function_name, args)
        if self.match(IDENTIFIER):
            name = self.previous()[1]
            if self.check(LEFT_BRACKET):  # Handling array/tuple indexing
                self.consume(LEFT_BRACKET, "Expect '[' after variable name.")
                index = self.expression()
                self.consume(RIGHT_BRACKET, "Expect ']' after index.")
                return IndexAccess(name, index)
            return Variable(name)
        if self.match(LEFT_PAREN):
            expr = self.expression()
            self.consume(RIGHT_PAREN, "Expect ')' after expression.")
            return expr
        unexpected_token = self.peek()
        raise SyntaxError(f"Unexpected token: {unexpected_token}")

    def match(self, *types):
        """Check if the current token matches any of the given types."""
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def check(self, token_type):
        """Check if the current token is of the given type."""
        if self.is_at_end():
            return False
        return self.peek()[0] == token_type

    def consume(self, token_type, message):
        """Consume a token of the given type, or raise an error."""
        if self.check(token_type):
            return self.advance()
        print(f"Error: Expected {token_type}, but got {self.peek()}")  # Debugging output
        raise SyntaxError(message)

    def peek_ahead(self, distance):
        """Look ahead at a token a certain distance away."""
        if self.current + distance < len(self.tokens):
            return self.tokens[self.current + distance]
        return (END, None)

    def block(self):
        """Parse a block of statements."""
        statements = []
        while not self.check(RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.statement())
        return Block(statements)


class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit_if_statement(self, statement):
        condition = self.visit(statement.condition)
        if condition:
            self.execute(statement.then_branch.statements)
        elif statement.else_branch:
            self.execute(statement.else_branch.statements)

    def visit_while_statement(self, statement):
        while self.visit(statement.condition):
            self.execute(statement.body.statements)

    def visit_for_statement(self, statement):
        # Execute the initializer (if it exists)
        if statement.initializer:
            self.visit(statement.initializer)

        # Loop as long as the condition is true
        while self.visit(statement.condition):
            # Execute the loop body
            self.execute(statement.body.statements)

            # Execute the increment (if it exists)
            if statement.increment:
                self.visit(statement.increment)

    def visit_printf_statement(self, statement):
        value = self.visit(statement.expression)
        if isinstance(value, list) or isinstance(value, tuple):
            print(value)
        else:
            print(value)

    def execute(self, statements):
        for statement in statements:
            self.visit(statement)

    def visit(self, node):
        if isinstance(node, IfStatement):
            return self.visit_if_statement(node)
        elif isinstance(node, WhileStatement):
            return self.visit_while_statement(node)
        elif isinstance(node, ForStatement):
            return self.visit_for_statement(node)
        elif isinstance(node, PrintfStatement):
            return self.visit_printf_statement(node)
        elif isinstance(node, Assign):
            value = self.visit(node.value)
            self.variables[node.name] = value
        elif isinstance(node, BinaryExpression):
            left = self.visit(node.left)
            right = self.visit(node.right)
            return self.apply_operator(node.operator, left, right)
        elif isinstance(node, UnaryExpression):
            operand = self.visit(node.operand)
            return self.apply_unary_operator(node.operator, operand)
        elif isinstance(node, Literal):
            try:
                return int(node.value)
            except ValueError:
                return node.value  # Return the string value if it's not an integer
        elif isinstance(node, Variable):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                raise ValueError(f"Variable '{node.name}' is not defined.")
        elif isinstance(node, IndexAccess):
            collection = self.visit(Variable(node.name))
            index = self.visit(node.index)
            if not isinstance(index, int):
                raise TypeError("Index must be an integer.")
            if not isinstance(collection, (list, tuple)):
                raise TypeError(f"Variable '{node.name}' is not a list or tuple.")
            if index < 0 or index >= len(collection):
                raise IndexError("Index out of range.")
            return collection[index]
        elif isinstance(node, ExpressionStatement):
            return self.visit(node.expression)
        elif isinstance(node, Block):
            return self.execute(node.statements)
        elif isinstance(node, FunctionCall):
            return self.visit_function_call(node.name, node.arguments)
        else:
            raise TypeError(f"Unknown node type: {type(node)}")

    def visit_function_call(self, function_name, arguments):
        if function_name == 'MIN':
            arg1, arg2 = self.visit(arguments[0]), self.visit(arguments[1])
            if not (isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))):
                raise TypeError(f"Arguments for MIN must be numbers, your types are {type(arg1)} and {type(arg2)}")
            return min(arg1, arg2)
        elif function_name == 'MAX':
            arg1, arg2 = self.visit(arguments[0]), self.visit(arguments[1])
            if not (isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))):
                raise TypeError(f"Arguments for MAX must be numbers, your types are {type(arg1)} and {type(arg2)}")
            return max(arg1, arg2)
        elif function_name == 'ISUPPER':
            arg = self.visit(arguments[0])
            if not isinstance(arg, str):
                raise TypeError(f"Argument for ISUPPER must be a string, your type is {type(arg)}")
            return arg.isupper()
        elif function_name == 'ISLOWER':
            arg = self.visit(arguments[0])
            if not isinstance(arg, str):
                raise TypeError(f"Argument for ISLOWER must be a string, your type is {type(arg)}")
            return arg.islower()
        elif function_name == 'CONCAT':
            arg1, arg2 = self.visit(arguments[0]), self.visit(arguments[1])
            # Convert both arguments to strings to handle any type
            return str(arg1) + str(arg2)
        elif function_name == 'SQUARE':
            arg = self.visit(arguments[0])
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argument for SQUARE must be a number, your type is {type(arg)}")
            return arg ** 0.5
        elif function_name == 'ARRAY':
            return [self.visit(arg) for arg in arguments]
        elif function_name == 'TUPLE':
            return tuple(self.visit(arg) for arg in arguments)
        elif function_name == 'ADD_TUPLE':
            tuple1 = self.visit(arguments[0])
            tuple2 = self.visit(arguments[1])
            if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
                raise TypeError("ADD_TUPLE can only be used with tuples.")
            return tuple1 + tuple2
        elif function_name == 'SORT_TUPLE':
            tuple_to_sort = self.visit(arguments[0])
            if not isinstance(tuple_to_sort, tuple):
                raise TypeError("SORT_TUPLE can only be used with tuples.")
            return tuple(sorted(tuple_to_sort))
        elif function_name == 'LEN':
            collection = self.visit(arguments[0])
            if not isinstance(collection, (list, tuple)):
                raise TypeError("Argument to LEN must be an array or tuple.")
            return len(collection)
        elif function_name == 'APPEND':
            collection = self.visit(arguments[0])
            value = self.visit(arguments[1])
            if not isinstance(collection, list):
                raise TypeError("APPEND can only be used with arrays.")
            collection.append(value)
            return collection
        elif function_name == 'REMOVE':
            collection = self.visit(arguments[0])
            index = self.visit(arguments[1])
            if not isinstance(collection, list):
                raise TypeError("REMOVE can only be used with arrays.")
            if not isinstance(index, int):
                raise TypeError("Index for REMOVE must be an integer.")
            if index < 0 or index >= len(collection):
                raise IndexError("Index out of range for REMOVE.")
            collection.pop(index)
            return collection
        elif function_name == 'SPLIT':
            string_value = self.visit(arguments[0])
            delimiter = self.visit(arguments[1])
            if not isinstance(string_value, str):
                raise TypeError("SPLIT can only be used with strings.")
            if not isinstance(delimiter, str):
                raise TypeError("Delimiter in SPLIT must be a string.")
            return string_value.split(delimiter)
        elif function_name == 'REPLACE':
            string_value = self.visit(arguments[0])
            old_substring = self.visit(arguments[1])
            new_substring = self.visit(arguments[2])
            if not isinstance(string_value, str):
                raise TypeError("REPLACE can only be used with strings.")
            if not isinstance(old_substring, str) or not isinstance(new_substring, str):
                raise TypeError("Substrings in REPLACE must be strings.")
            return string_value.replace(old_substring, new_substring)
        else:
            raise ValueError(f"Function '{function_name}' is not defined.")

    def apply_operator(self, operator, left, right):
        if operator[0] == ADD:
            return self.ADD(left, right)
        elif operator[0] == SUB:
            return self.SUB(left, right)
        elif operator[0] == MUL:
            return self.MUL(left, right)
        elif operator[0] == DIV:
            return self.DIV(left, right)
        elif operator[0] == POWER:
            return self.POWER(left, right)
        elif operator[0] == EQUAL:
            return self.EQUAL(left, right)
        elif operator[0] == NOT_EQUAL:
            return self.NOT_EQUAL(left, right)
        elif operator[0] == GREATER:
            return self.GREATER(left, right)
        elif operator[0] == LESS:
            return self.LESS(left, right)
        elif operator[0] == GREATER_EQUAL:
            return self.GREATER_EQUAL(left, right)
        elif operator[0] == LESS_EQUAL:
            return self.LESS_EQUAL(left, right)
        elif operator[0] == OR:
            return self.OR(left, right)
        elif operator[0] == AND:
            return self.AND(left, right)
        else:
            raise TypeError(f"Unknown operator: {operator[0]}")

    def apply_unary_operator(self, operator, operand):
        if operator[0] == SUB:
            return -operand
        else:
            raise TypeError(f"Unknown unary operator: {operator}")

    def ADD(self, x, y):
        return x + y

    def MIN(self, x, y):
        if x > y:
            return y
        if x < y:
            return x
        else:
            return x or y

    def SUB(self, x, y):
        return x - y

    def MUL(self, x, y):
        return x * y

    def DIV(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y

    def POWER(self, x, y):
        return x ** y

    def EQUAL(self, x, y):
        return x == y

    def NOT_EQUAL(self, x, y):
        return x != y

    def GREATER(self, x, y):
        return x > y

    def LESS(self, x, y):
        return x < y

    def GREATER_EQUAL(self, x, y):
        return x >= y

    def LESS_EQUAL(self, x, y):
        return x <= y

    def OR(self, x, y):
        return x or y

    def AND(self, x, y):
        return x and y

    def CONCAT(self, string1, string2):
        return str(string1) + str(string2)


class Arrays:
    def __init__(self, arr):
        if not isinstance(arr, list):
            raise TypeError("The input should be a sequence or a collection")
        self.arr = arr

    def length_of_arr(self):
        return len(self.arr)

    def get_index_of_array(self, element, start=0, end=None):
        if end is None:
            end = len(self.arr)
        if start < 0 or end > len(self.arr) or start > end:
            raise IndexError("Invalid start or end index")
        for i in range(start, end):
            if self.arr[i] == element:
                return i
        raise ValueError(f"{element} is not in the list")

    def get_value_in_array(self, index):
        if not isinstance(index, int):
            raise TypeError("The index should be an integer")
        if index >= len(self.arr) or index < 0:
            raise IndexError("Index out of range")
        return self.arr[index]

    def add_to_array(self, element):
        self.arr.append(element)

    def remove_from_array(self, element):
        if element not in self.arr:
            raise ValueError("The value is not found in the list")
        self.arr.remove(element)


class TupleUtils:
    def __init__(self, tup):
        if not isinstance(tup, tuple):
            raise TypeError("The input should be a tuple")
        self.tup = tup

    def length_of_tuple(self):
        return len(self.tup)

    def get_index_of_tuple(self, element, start=0, end=None):
        if end is None:
            end = len(self.tup)
        if start < 0 or end > len(self.tup) or start > end:
            raise IndexError("Invalid start or end index")
        for i in range(start, end):
            if self.tup[i] == element:
                return i
        raise ValueError(f"{element} is not in the tuple")

    def get_item_in_tuple(self, index):
        if not isinstance(index, int):
            raise TypeError("The index should be an integer")
        if index >= len(self.tup) or index < 0:
            raise IndexError("Index out of range")
        return self.tup[index]

    def add_2_tuple(t1, t2):
        if not isinstance(t1, tuple) or not isinstance(t2, tuple):
            raise TypeError("Both inputs should be tuples")
        return t1 + t2

    def tuple_sort(t1):
        if not isinstance(t1, tuple):
            raise TypeError("The input should be a tuple")
        if len(t1) <= 1:
            return t1
        pivot = t1[len(t1) // 2]
        small = []
        middle = []
        big = []
        for i in t1:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                big.append(i)
            else:
                middle.append(i)
        return tuple(TupleUtils.tuple_sort(tuple(small)) + tuple(middle) + TupleUtils.tuple_sort(tuple(big)))


### TEST ####
def main():
    # Test 1: Simple String Assignment and Print
    code1 = '''
    a = "Hello, World!";
    printf(a);
    '''
    print("Test 1: Simple String Assignment and Print")
    lexer = Lexer(code1)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast.statements)
    print("Needed to be: Hello, World!\n")

    # Test 2: Basic Arithmetic Operations
    code2 = '''
    a = 10 + 5;
    b = a * 2;
    c = b - 3 / 1;
    printf(c);
    '''
    print("Test 2: Basic Arithmetic Operations")
    lexer = Lexer(code2)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 27\n")

    # Test 3: String Concatenation
    code3 = '''
    a = "Hello2 ";
    b = "World!";
    c = CONCAT(a, b);
    printf(c);  
    '''
    print("Test 3: String Concatenation")
    lexer = Lexer(code3)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Hello World!\n")

    # Test 4: If-Else Conditional Logic
    code4 = '''
    a = 10;
    if (a > 5) {
        printf("Greater than 5");
    } else {
        printf("Less than or equal to 5");
    }
    '''
    print("Test 4: If-Else Conditional Logic")
    lexer = Lexer(code4)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Greater than 5\n")

    # Test 5: While Loop
    code5 = '''
    a = 0;
    while (a < 3) {
        printf(a);
        a = a + 1;
    }
    '''
    print("Test 5: While Loop")
    lexer = Lexer(code5)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 0 1 2\n")

    # Test 6: For Loop with Increment
    code6 = '''
    for (i = 0; i < 5; i = i + 1;) {
        printf(i);
    }
    '''
    print("Test 6: For Loop with Increment")
    lexer = Lexer(code6)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 0 1 2 3 4\n")

    # Test 7: String and Arithmetic Operations Combined
    code7 = '''
    a = "Result: ";
    b = "8";
    c = CONCAT(a, b);
    printf(c);
    '''
    print("Test 7: String and Arithmetic Operations Combined")
    lexer = Lexer(code7)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Result: 8\n")

    # Test 8: Logical Conditions in If Statement
    code8 = '''
    a = 10;
    if (a > 5 && a < 15) {
        printf("Within range");
    } else {
        printf("Out of range");
    }
    '''
    print("Test 8: Logical Conditions in If Statement")
    lexer = Lexer(code8)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Within range\n")

    # Test 9: Nested If-Else Statements
    code9 = '''
    a = 20;
    if (a > 10) {
        if (a < 30) {
            printf("Between 10 and 30");
        } else {
            printf("30 or more");
        }
    } else {
        printf("10 or less");
    }
    '''
    print("Test 9: Nested If-Else Statements")
    lexer = Lexer(code9)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Between 10 and 30\n")

    # Test 10: String Comparison with Functions
    code10 = '''
    a = "hello";
    b = "HELLO";
    if (ISUPPER(b)) {
        printf("Uppercase check passed");
    } else {
        printf("Uppercase check failed");
    }
    if (ISLOWER(a)) {
        printf("Lowercase check passed");
    } else {
        printf("Lowercase check failed");
    }
    '''
    print("Test 10: String Comparison with Functions")
    lexer = Lexer(code10)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Uppercase check passed\nLowercase check passed\n")

    # Test 11: Function Call Inside If Statement
    code11 = '''
    a = 5;
    b = 10;
    if (MAX(a, b) == b) {
        printf("Max is b");
    } else {
        printf("Max is a");
    }
    '''
    print("Test 11: Function Call Inside If Statement")
    lexer = Lexer(code11)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Max is b\n")

    # Test 12: Nested For Loops
    code12 = '''
    result = 0;
    for (i = 1; i <= 3; i = i + 1;) {
        for (j = 1; j <= 2; j = j + 1;) {
            result = result + i * j;
        }
    }
    printf(result);
    '''
    print("Test 12: Nested For Loops")
    lexer = Lexer(code12)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 18\n")

    # Test 13: Logical Conditions in For Loop
    code13 = '''
    count = 0;
    for (i = 1; i <= 5; i = i + 1;) {
        if (i > 2 && i < 5) {
            count = count + 1;
        }
    }
    printf(count);
    '''
    print("Test 13: Logical Conditions in For Loop")
    lexer = Lexer(code13)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 2\n")

    # Test 14: Complex Expressions in Conditionals
    code14 = '''
    a = 5;
    b = 3;
    if ((a > b && a < 10) || (b == 3)) {
        printf("Condition met");
    } else {
        printf("Condition failed");
    }
    '''
    print("Test 14: Complex Expressions in Conditionals")
    lexer = Lexer(code14)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Condition met\n")

    # Test 15: Function Calls with Multiple Arguments
    code15 = '''
    a = MIN(3, 7);
    b = MAX(2, 5);
    c = SQUARE(4);
    printf(a);
    printf(b);
    printf(c);
    '''
    print("Test 15: Function Calls with Multiple Arguments")
    lexer = Lexer(code15)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 3\n5\n2.0\n")

    # Test 16: Complex For Loop with String Operations
    code16 = '''
    a = "Result: ";
    for (i = 0; i < 3; i = i + 1;) {
        a = CONCAT(a, i);
    }
    printf(a);
    '''
    print("Test 16: Complex For Loop with String Operations")
    lexer = Lexer(code16)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Result: 012\n")

    # Test 17: Arithmetic Operations with String Concatenation
    code17 = '''
    a = "Sum is ";
    b = 5 + 3;
    result = CONCAT(a, b);
    printf(result);
    '''
    print("Test 17: Arithmetic Operations with String Concatenation")
    lexer = Lexer(code17)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Sum is 8\n")

    # Test 18: If-Else with Function Calls
    code18 = '''
    a = SQUARE(9);
    if (a == 3) {
        printf("Perfect square");
    } else {
        printf("Not a perfect square");
    }
    '''
    print("Test 18: If-Else with Function Calls")
    lexer = Lexer(code18)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: Perfect square\n")

    # Test 19: Division by Zero Error Handling
    code19 = '''
    a = 10;
    b = 0;
    c = a / b;
    printf(c);
    '''
    print("Test 19: Division by Zero Error Handling")
    try:
        lexer = Lexer(code19)
        tokens = lexer.split()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        interpreter.execute(ast.statements)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    print("Needed to be: Error: Division by zero is not allowed\n")

    # Test 20: Empty Code Handling
    code20 = '''
    '''
    print("Test 20: Empty Code Handling")
    lexer = Lexer(code20)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast.statements)
    print("Needed to be: (No output expected for empty code)\n")

    code21 = '''
        a = 0;
        while (a < 3) {
            printf(a);
            a = a + 1;
        }
        '''
    print("Test 21: Simple While Loop with Condition")
    lexer = Lexer(code21)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be: 0 1 2\n")

    code22 = '''
        a = 0;
        while (a < 10) {
            if (a == 5) {
                printf("Hello im 5");
            }
            a=a+1;
        }
        '''
    print("Test 22: While Loop with a print 5")
    lexer = Lexer(code22)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be:Hello im 5\n")

    # Test 23: Array and Tuple Creation
    code23 = '''
    a = ARRAY(1, 2, 3, 4);
      REMOVE(a,1); 
      APPEND(a,2);

       printf(a);   
    '''
    print("Test 23: Array and Tuple Creation")
    lexer = Lexer(code23)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)
    print("Needed to be:4")

    code24 = '''
    a = TUPLE(5, 3, 8, 1);
    printf(a);  

    sorted_a = SORT_TUPLE(a);
    printf(sorted_a); 

    b = TUPLE(7, 2);
    combined = ADD_TUPLE(sorted_a, b);
    printf(combined);  

    index_item = combined[3];
    printf(index_item);  

    length = LEN(combined);
    printf(length);  
    '''
    print("Test 24: Tuple Operations")
    lexer = Lexer(code24)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter.execute(ast.statements)

    code27 = '''
    a = "Hello World Test";
    split_result = SPLIT(a, " ");
    printf(split_result);

    b = "I love Python!";
    replace_result = REPLACE(b, "Python", "Shemaython");
    printf(replace_result);
    '''
    print("Test 27: String SPLIT and REPLACE Operations")
    lexer = Lexer(code27)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast.statements)
    print("Expected output:\n['Hello', 'World', 'Test']\nI love Shemaython!")
    code88 = '''
    a = 5;
    b = 6;
    if (a <= b) {
        printf("less")
    }
    '''
    lexer = Lexer(code88)
    tokens = lexer.split()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast.statements)


if __name__ == "__main__":
    main()
