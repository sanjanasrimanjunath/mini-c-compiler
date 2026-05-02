import ply.yacc as yacc
from lexer import tokens

# 🔹 AST Node (simple structure)
class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children else []
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value if self.value else ''}, {self.children})"


# 🔹 Grammar Rules

def p_program(p):
    '''program : statements'''
    p[0] = Node("program", [p[1]])


def p_statements(p):
    '''statements : statement statements
                  | statement'''
    if len(p) == 3:
        p[0] = Node("statements", [p[1], p[2]])
    else:
        p[0] = Node("statements", [p[1]])


def p_statement_decl(p):
    '''statement : INT IDENTIFIER SEMICOLON
                 | FLOAT IDENTIFIER SEMICOLON'''
    p[0] = Node("declaration", value=(p[1], p[2]))


def p_statement_assign(p):
    '''statement : IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = Node("assign", [p[3]], p[1])


def p_statement_print(p):
    '''statement : PRINT LPAREN IDENTIFIER RPAREN SEMICOLON'''
    p[0] = Node("print", value=p[3])


# 🔹 Expressions

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = Node("binop", [p[1], p[3]], p[2])


def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]


def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = Node("binop", [p[1], p[3]], p[2])


def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]


def p_factor_num(p):
    '''factor : NUMBER'''
    p[0] = Node("number", value=p[1])


def p_factor_id(p):
    '''factor : IDENTIFIER'''
    p[0] = Node("identifier", value=p[1])


def p_factor_expr(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[2]


# 🔹 Error handling
def p_error(p):
    print("Syntax error at", p)


# 🔹 Build parser
parser = yacc.yacc()