import re

# Part 1: Arithmetic Tokenizer

# Token types (Arithmetic only)
TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+'),
    ('ADD',      r'\+'),
    ('SUB',      r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

TOKEN_REGEX = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)

def tokenize(expression):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, expression):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value)))
        elif kind in ('ADD', 'SUB', 'MUL', 'DIV', 'LPAREN', 'RPAREN'):
            tokens.append((kind, value))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected token: {value}')
    return tokens
