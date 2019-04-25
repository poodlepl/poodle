#!/usr/bin/python3
from docopt import docopt
from glob import glob
from modules.lex import lex
from modules.parser import *
from prettytable import PrettyTable
from modules.symbol import *
from modules.wordlist import *
from modules.remove_comments import remove_comments


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


args = docopt(usage)
if args['--version']:
    print("Poodle Programming Language V1.0")

elif args['--source']:
    source = args['<filename>']
    try:
        data = open_file(source)
        print("SYMBOL TABLE:")
        tokens = lex(data)
        
        table = PrettyTable()
        table.field_names = ["IDENTIFIER","VALUE", "POSITION", "LINE", "SIZE", "TOKEN TYPE"]
        for k,v in sym_tab.items():
                sym= [k]+v
                table.add_row(sym)
        print(table)
        parse(tokens)
        for k,v in ast.items():
            print(v)
        for k,v in sym_tab.items():
            sym= [k]+v
            table.add_row(sym)
        print(table)
    except AttributeError:
        print("ERROR: "+source+" is not a valid file. ")


