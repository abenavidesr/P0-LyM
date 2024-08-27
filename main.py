# **** P0 LENGUAJE Y MAQUINAS 2024-2 ****

### Felipe Sanchez - 202214630

import re
from tabulate import tabulate

# TOKENS
token_patterns = [
    ('DEF', r'\bNEW\b'),             
    ('VAR', r'\bVAR\b'),
    ('MOVE FORWARD', R'\bM\b'),
    ('TURN RIGHT', R'\bR\b'),
    ('DROP CHIP', R'\bC\b'),
    ('PLACE BALLOON', R'\bB\b'),
    ('PICK UP CHIP', R'\bc\b'),
    ('GRAB BALLOON', R'\bb\b'),
    ('POP BALLOON', R'\bP\b'),
    ('JUMP N STEPS', r'J\(\d+\)'),
    ('GO TO POS', r'G\(\d+,\d+\)'),
    ('NUMBER', r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
    ('EQUALS', r'[=]'),
    ('WHITESPACE', r'\s+'), 
    ('SEPARATOR', r'[;]'),
    ('UNKNOWN', r'.')
]

# FUNCIÓN DE ANALISIS DE TEXTO
def lexer(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                if token_type != 'WHITESPACE':  # Ignorar espacios en blanco
                    tokens.append((token_type, match.group(0)))
                code = code[match.end():]  # Mover el puntero del código
                break
        if not match:
            raise SyntaxError(f'Error léxico: {code[0]}')
    return tokens