#!/usr/bin/python3
#import sys
#from sys import *
from docopt import docopt
from glob import glob
from lexer import *


usage = '''

Poodle Programming Language

Usage:
    ./poodle.py --version
    ./poodle.py --source <filename>

'''


flag = 2

def open_file(source):
    if source in glob("lang/*.lang"):
        source_code = open(source, 'r').read()
        return source_code
    else:
        flag = 1
        return flag

'''

#EARLIER

# used len(sys.argv) to check file name.
# shifted to docopts.args for better support

#if(len(sys.argv) == 1):
#    print(args)
'''


args = docopt(usage)
if args['--version']:
    print("Poodle Programming Language V1.0")

elif args['--source']:
    source = args['<filename>']
    try:
        data = open_file(source)
        lex(data)
    except AttributeError:
        print("ERROR: "+source+" is not a valid file. ")


