from modules.lex import *
import pprint


pp = pprint.PrettyPrinter(indent = 4)

def parse(tokens):
    print("\nPARSING ... \n")
    pp.pprint(tokens)
