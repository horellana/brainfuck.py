#!python

import sys
import argparse
import brainfuck

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--eval', help='eval a string of code')
parser.add_argument('-f', '--file', help='execute a file')
parser.add_argument('-r', '--repl', help='enter a really simple repl',
                    action='store_true')

args = parser.parse_args()

if args.eval:
    code = brainfuck.read(args.eval)
    brainfuck.eval(code)
elif args.file:
    with open(args.file, 'r') as infile:
        code = brainfuck.read(''.join(infile.readlines()))
        brainfuck.eval(code)
elif args.repl:
    data = [0 for i in range(9999)]
    while True:
        sys.stdout.write("bf> ")
        sys.stdout.flush()
        line = sys.stdin.readline()
        code = brainfuck.read(line)
        brainfuck.eval(code, data)
