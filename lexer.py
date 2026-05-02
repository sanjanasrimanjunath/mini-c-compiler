import ply.lex as lex

# 🔹 List of token names
tokens = [
    'IDENTIFIER',
    'NUMBER',

    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',

    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',

    'ASSIGN',

    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',

    'SEMICOLON', 'COMMA'
]

# 🔹 Reserved keywords
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT'
}

tokens = tokens + list(reserved.values())

# 🔹 Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

t_ASSIGN = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

t_SEMICOLON = r';'
t_COMMA = r','

# 🔹 Ignore spaces and tabs
t_ignore = ' \t'

# 🔹 Identifier (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for keywords
    return t

# 🔹 Numbers (int + float)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# 🔹 Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 🔹 Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# 🔹 Build lexer
lexer = lex.lex()