#!/usr/bin/env python

import sys

def read_code():
    valid = [ '>', '<', '+', '-', '.', ',', '[', ']' ]
    return [ c for c in sys.stdin.read() if c in valid ]

data = [ 0 for i in range(50) ]
code = read_code()

code_pos = 0
data_pos = 0

while code_pos <= len(code):
    step = 1
    c = code[code_pos]

    if c == '>':
        data_pos = data_pos + 1
    elif c == '<':
        data_pos = data_pos - 1
    elif c == '+':
        data[data_pos] = data[data_pos] + 1  
    elif c == '-':
        data[data_pos] = data[data_pos] - 1
    elif c == '.':
        print( chr( data[data_pos] ) )
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

    print(data)
                
    code_pos = code_pos + step
            
