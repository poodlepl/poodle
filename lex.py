import re
import os
import sys
from wordlist import switch
from ll1 import Lexer
from remove_comments import remove_comments


tokens = []
comments = []

# all the tokens are stored here
def nocomments(filename):
    filename = sys.argv[2]
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments)
    #code_wo_comments = single(code_w_comments)
    filename = os.path.basename(filename)
    fh = open("nocomments/" + filename + ".nocomments", "w")
    fh.write(str(code_wo_comments))
    fh.close()

    newfile = open("nocomments/" + filename + ".nocomments", 'r')
    newfilecont = newfile.read()
    newfile.close()
    #print(newfilecont)

    return code_wo_comments


def lex(filename):

    contents = nocomments(filename)
    print(contents)
    lex = Lexer(contents)
    lex.tokenize()

    data=switch.keys()


