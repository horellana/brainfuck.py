#!/usr/bin/env python3

import sys

def check_code(code):
    if len( [ c for c in code if c in ['[', ']'] ] ) % 2 != 0:
        sys.stderr.write("There is a syntax error somewhere\n")
        sys.exit(-1)

    a = []
    for c in code:
        if c == '[':
            a.append(c)
        elif c == ']':
            try:
                a.pop()
            except IndexError:
                sys.stderr.write("Misplaced `]` in position\n")
                sys.exit(-1)

def read_code():
    valid = [ '>', '<', '+', '-', '.', ',', '[', ']' ]
    return [ c for c in sys.stdin.read() if c in valid ]

data = [ 0 for i in range(30000) ]

code = read_code()
check_code(code)

code_pos = 0
data_pos = 0

while code_pos < len(code):
    step = 1
    c = code[code_pos]

    if c == '>':
        data_pos = data_pos + 1
        if data_pos > len(data):
            data_pos = 0
    elif c == '<':
        if data_pos != 0:
            data_pos = data_pos - 1
    elif c == '+':
        if data[data_pos] == 255:
            data[data_pos] = 0
        else:
            data[data_pos] = data[data_pos] + 1
    elif c == '-':
        if data[data_pos] == 0:
            data[data_pos] = 255
        else:
            data[data_pos] = data[data_pos] - 1
    elif c == '.':
        sys.stdout.write( chr( data[data_pos] ) )
    elif c == ',':
        data[data_pos] = ord( sys.stdin.read() )
    elif c == '[':
        if data[data_pos] == 0:
            step = 0
            while code[code_pos - 1] != ']':
                code_pos = code_pos + 1
    else:
        if data[data_pos] != 0:
            step = 0
            while code[code_pos - 1] != '[':
                code_pos = code_pos - 1

    code_pos = code_pos + step
            
