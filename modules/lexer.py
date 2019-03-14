import re
import os
import sys
import pprint
from modules.wordlist import keywords
from modules.remove_comments import remove_comments

pp = pprint.PrettyPrinter(indent = 4)

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


class Lexer(object):
    """docstring for Lexer"""
    def __init__(self, source_code):
        self.source_code = source_code
    
    def tokenize(self):
    
        #where all the tokens created by the lexer will be stored
        tokens =[]
    
        #create a word list of the source code
        source_code = self.source_code.split()

        #where all the strings 
        strings =[]
    
        #Basically this will keep track if undex numberswe are at in the source code
        source_index =0
        c=0
    
        #loop through each word in source code to generate tokens
        while source_index<len(source_code):
                word = source_code[source_index]
                    
                if word.startswith('"') or c==1:
                    c=1
                    strings.append(word)
                    if word.endswith('"'):
                        c=0	

                # This will recognise a variable and create a token for it
                elif word in keywords.keys():
                     tokens.append(Token(keywords[word], word))
                     print(word)
                
                #This will recognise a word and create an identifier token for it
                elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                    tokens.append(Token('IDENTIFIER', word))

                #This will recognise an integer and create an identifier token for it
                elif re.match('[0-9]', word):
                    tokens.append(Token('INTEGER ', word))


                #This will recognise operators
                elif word in "%/*-+":
                    tokens.append(Token('OPERATOR',word))


                #increases word index after checking it
                source_index += 1
        
        #pp.pprint(tokens)    
        pp.pprint(strings)
        
        for line in tokens:
            print('\t'.join(line))

        #Return created tokens
        return tokens

tokens = []
comments = []


def lex(filename):

    contents = nocomments(filename)
    print("Code without comments\n")
    print(contents)
    lex = Lexer(contents)
    lex.tokenize()
 
