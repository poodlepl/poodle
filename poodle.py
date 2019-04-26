#!/usr/bin/python3
from docopt import docopt
from glob import glob
from modules.lex import lex
from modules.parser import *
from prettytable import PrettyTable
from modules.symbol import *
from modules.wordlist import *
from modules.remove_comments import remove_comments
from pptree import *
c=0

usage = '''

Poodle Programming Language

Usage:
    ./poodle.py --version
    ./poodle.py --source <filename>

'''
def make_node(branch, r):
    global c
    if(type(branch)==str):
        return(Node(branch,r))
    elif(len(branch)>=2):
        if(type(branch[1])==list):
            root = Node(branch[0], r)
            leaf1 = make_node(branch[1],root)
            leaf2 = make_node(branch[1],root)
            return root
        if c==0:
            c=c+1
            return(Node(branch[0], r))
        
        else:
            c=0
            return(Node(branch[1], r))
    
    else:
        return(Node(branch[0],r))

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
        leaf={}
        for k,v in ast.items():
            r=[]
            print(v)
            root = Node(v[0])
            for i in range(1,len(v)):
                if(type(v[i])==str):
                    r.append(Node(v[i],root))
                else:
                    if(len(r)>0):
                        leaf[i] = make_node(v[i],r[len(r)-1])
                    else:
                        leaf[i] = make_node(v[i],root)
            # print('\n')
            # print('\n')

            # for i in v:  
            #     print(i)


            #     root = Node(v[i])
            # # leaf1 = Node(v[1][0], root)
            # # leaf2 = Node(v[1][1][0], leaf1)
            # # leaf3 = Node(v[1][1][1], leaf1)
            # # leaf4 = Node(v[2], root)
            # # leaf5 = Node(v[3][0], root)
            # # leaf6 = Node(v[3][1][0], leaf5)
            # # leaf7 = Node(v[4][0], root)
            # # leaf8 = Node(v[4][1][0], leaf7)
            print_tree(root)
            # print('\n')
            # print('\n')

        table = PrettyTable()
        table.field_names = ["IDENTIFIER","VALUE", "POSITION", "LINE", "SIZE", "TOKEN TYPE"]
        for k,v in sym_tab.items():
            sym= [k]+v
            table.add_row(sym)
        print(table)
    except AttributeError:
        print("ERROR: "+source+" is not a valid file. ")


