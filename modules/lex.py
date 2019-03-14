import re
import os
import sys
from modules.wordlist import *
from modules.remove_comments import remove_comments


class Token:
    def __init__(self, type_, value):
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


    def tokenize(self):
        tokens = []

        while self.current_char != None:
            temp_str = ""
            #if self.current_char in ' ':
                #self._move_next()

            if self.current_char != ' ':
                temp_str += self.current_char

                if self.current_char in ' \'\"':
                    self._move_next()

            # This will recognise a variable and create a token for it
            if temp_str in keywords.keys():
                tokens.append(Token(keywords[temp_str], temp_str))
                #print(self.current_char)
                #self._move_next()

            #This will recognise a word and create an identifier token for it
            elif re.match('[a-z]', temp_str) or re.match('[A-Z]', temp_str):
                tokens.append(Token('IDENTIFIER', temp_str))
                #self._move_next()

            #This will recognise an integer and create an identifier token for it
            elif re.match('[0-9]', temp_str):
                tokens.append(Token('INTEGER ', temp_str))
                #self._move_next()

            #This will recognise operators
            elif temp_str in "%/*-+":
                tokens.append(Token('OPERATOR ', temp_str))
                #self._move_next()

            #elif self.current_char == "\"":
                #temp_str += self.current_char

            self._move_next()
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
    print(contents)
    lex = Lexer(contents)
    print(lex.tokenize())

