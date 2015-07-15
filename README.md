brainfuck.py
============
Installation
---------------
```
$ git clone https://github.com/juiko/brainfuck.py
$ cd brainfuck.py
$ python setup.py install --user
```
Usage
-----
```
## to execute a file

bf.py -f 'file' 

## to eval code directly

bf.py -e 'brainfuck code' 

## To start a repl

bf.py -r 

### From python

from brainfuck import bf_eval, read_code, prepare_code

code = prepare_code(read_code(input_string))
bf_eval(code)
```