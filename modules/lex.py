import re
import os
import sys
import pprint
from modules.wordlist import *
from modules.remove_comments import remove_comments


pp = pprint.PrettyPrinter(indent = 4)
DIGITS = '0123456789'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self._move_next()

    def _move_next(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self._move_next()

        if dot_count == 0:
            print(num_str)
            return Token('INTEGER', num_str)
        else:
            return Token('FLOAT', num_str)

    def tokenize(self):
        tokens = []

        temp_str = ""
        while self.current_char != None:
            if self.current_char == '\n' or self.current_char == ' ':
                # This will recognise a variable and create a token for it
                if temp_str in keywords.keys():
                    tokens.append([keywords[temp_str], temp_str])
                    self._move_next()
                    temp_str = ""

                #This will recognise a word and create an identifier token for it
                elif re.match('[a-z]', temp_str) or re.match('[A-Z]', temp_str):
                    tokens.append(['IDENTIFIER', temp_str])
                    self._move_next()
                    temp_str = ""

                #This will recognise an integer and create an identifier token for it
                elif re.match('[0-9]', temp_str):
                    tokens.append(['INTEGER', temp_str])
                    self._move_next()
                    temp_str = ""

                #This will recognise operators
                elif temp_str in "%/*-+" and temp_str != ' ':
                    tokens.append(['OPERATOR', temp_str])
                    self._move_next()
                    temp_str = ""

            else:
                temp_str += self.current_char
                self._move_next()
        tokens.append([keywords[temp_str], temp_str])
        return tokens

def nocomments(filename):
    filename = sys.argv[2]
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments)
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
    print("Code without comments\n")
    print(contents+'\n')
    lex = Lexer(contents)
    pp.pprint(lex.tokenize())

