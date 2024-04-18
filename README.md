brainfuck.py
============
Installation
---------------
```
$ git clone https://github.com/horellana/brainfuck.py
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

import brainfuck

code = brainfuck.read(input_string)
brainfuck.eval(code)
```
