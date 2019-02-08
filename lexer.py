import re
from wordlist import keywords, relop


def lex(filecontents):
    '''
    tok = ""
    state = 0
    string = ""
    identifier = []
    content = list(filecontents)
    for char in content:
        tok += char
        print(tok)

    tok = ""
    '''
    words = filecontents.split()
    print(words)
    '''
    iterate through em all and process it.
    take raw string
    if there is extra char, check. isAlpha() and all.
    '''


#print(keywords)
#print(relop)
