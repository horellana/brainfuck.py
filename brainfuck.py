#!/usr/bin/env python3

import sys
import argparse


def find_matching_end_bracket(code, code_pos):
    a = []
    for i in range(code_pos + 1, len(code)):
        c = code[i]
        if c == '[':
            a.append(c)
        if c == ']':
            if len(a) == 0:
                return i
            else:
                a.pop()

    raise Exception("Could not find matching `]` bracket")


def find_matching_start_bracket(code, code_pos):
    a = []
    for i in range(code_pos - 1, -1, -1):
        c = code[i]
        if c == ']':
            a.append(c)
        if c == '[':
            if len(a) == 0:
                return i
            else:
                a.pop()

    raise Exception("Could not find matching `[` bracket")


def read(string):
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
        elif c == '[':
            if data[data_pos] == 0:
                step = 0
                code_pos = find_matching_end_bracket(code, code_pos) + 1
        else:
            if data[data_pos] != 0:
                step = 0
                code_pos = find_matching_start_bracket(code, code_pos) + 1
        code_pos = code_pos + step


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--eval', help='eval a string of code')
    parser.add_argument('-f', '--file', help='execute a file')
    parser.add_argument('-r', '--repl', help='enter a really simple repl',
                        action='store_true')

    args = parser.parse_args()

    if args.eval:
        code = read(args.eval)
        eval(code)
    elif args.file:
        with open(args.file, 'r') as infile:
            code = read(''.join(infile.readlines()))
            eval(code)
    elif args.repl:
        data = [0 for i in range(9999)]
        while True:
            sys.stdout.write("bf> ")
            sys.stdout.flush()
            line = sys.stdin.readline()
            code = read(line)
            eval(code, data)


if __name__ == '__main__':
    main()
