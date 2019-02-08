#!/usr/bin/python3
import sys
from sys import *
from docopt import docopt
from glob import glob
from lexer import *


usage = '''

Poodle Programming Language

Usage:
    ./poodle.py <filename>.poo

'''


def open_file(source):
    if source in glob("lang/*.lang"):
        source_code = open(source, 'r').read()
        return source_code
    else:
        return "ERROR: "+source+" is not a valid file. "


if(len(sys.argv) == 1):
    args = docopt(usage)
    print(args)

else:
    source = argv[1]
    data = open_file(source)
    #print(data)
    lex(data)


