#!/usr/bin/env python3

import sys
import argparse


def find_bracket(code, pos, bracket):
    cont = 0
    pair = '[' if bracket == ']' else ']'
    for a, i in zip(code[pos:], range(pos, len(code))):
        if a == bracket:
            cont = cont + 1
        if a == pair:
            if cont == 0:
                return i
            else:
                cont = cont - 1

    raise Exception("Could not find `{}``bracket\nPosition: {}"
                    .format(pair, pos))


def prepare_code(code):
    def map_left_bracket(b, p):
        return (b, find_bracket(code, p + 1, b))

    def map_right_bracket(b, p):
        offset = find_bracket(list(reversed(code[:p])), 0, ']')
        return (b, p - offset)

    def map_bracket(b, p):
        if b == '[':
            return map_left_bracket(b, p)
        else:
            return map_right_bracket(b, p)

    return [map_bracket(c, i) if c in ('[', ']') else c
            for c, i in zip(code, range(len(code)))]


def read_code(string):
    valid = ['>', '<', '+', '-', '.', ',', '[', ']']
    return [c for c in string if c in valid]


def eval(code, data=[0 for i in range(9999)], code_pos=0, data_pos=0):
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
            sys.stdout.write(chr(data[data_pos]))
        elif c == ',':
            data[data_pos] = ord(sys.stdin.read(1))
        else:
            bracket, jmp = c
            if bracket == '[' and data[data_pos] == 0:
                step = 0
                code_pos = jmp
            elif bracket == ']' and data[data_pos] != 0:
                step = 0
                code_pos = jmp

        code_pos = code_pos + step


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--eval', help='eval a string of code')
    parser.add_argument('-f', '--file', help='execute a file')
    parser.add_argument('-r', '--repl', help='enter a really simple repl',
                        action='store_true')

    args = parser.parse_args()

    if args.eval:
        code = prepare_code(read_code(args.eval))
        eval(code)
    elif args.file:
        with open(args.file, 'r') as infile:
            code = prepare_code(read_code(''.join(infile.readlines())))
            eval(code)
    elif args.repl:
        data = [0 for i in range(9999)]
        while True:
            sys.stdout.write("bf> ")
            sys.stdout.flush()
            line = sys.stdin.readline()
            code = read_code(line)
            eval(code, data)


if __name__ == '__main__':
    main()
