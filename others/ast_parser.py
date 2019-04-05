from modules.lex import *
import pprint
import sys
import tokenize
from modules.symbol import *


symbolTable, inp_list = None, None
temp_count = -1
label_count = 0
in_if=0
i = 0
code = []

def getNextToken():
    global i
    if i==len(inp_list):
        #print(i,-1)
        return -1
    i+=1
    return [inp_list[i-1].value,inp_list[i-1].type_]

def token_exists():
    global i
    if i==len(inp_list):
        #print(i,-1)
        return 0
    else:
        return 1    
    
def parse(tokens):
    
    
    global symbolTable, inp_list,code,temp_count,in_if
    inp_list=tokens
    symbolTable=sym_tab
    
    while(token_exists()):
        lis=getNextToken()
        if(in_if==0):
            temp_count=-1
            code=[]
        #print("\n\n\n",lis)
        next_=lis[0]
        type_=lis[1]   
        try:
            if next_ =="wrap":
                Statement()
                print(code)
            elif next_=="vomit":
                print_()
                print(code)
            elif type_=="IDENTIFIER":
                identifier_()
                print(code)
            elif next_==".2":
                if_loop()
                print(code)
            elif next_=="---":
                in_if=0
            else:
                continue
        except:
            continue
        
        
        


def Statement():
    global i, temp_count, label_count, code
    i=i-1
    next_,type_=getNextToken()
    code.append([next_])
    temp_count+=1
    next_,type_=getNextToken()
    #print("fff\n\n",next_)
    if type_ == 'IDENTIFIER':
        identi=next_
        next_,type_=getNextToken()
        if next_=='as':
            code.append([next_])
            temp_count=temp_count+1
            next_,type_=getNextToken()
            if type_=='INTEGER' or type_ =='FLOAT':
                code[temp_count].append([identi,next_])
                size=sys.getsizeof(identi)
                symbol_(identi,value=next_,size=size)
        else:
            i=i-1
                
    else:
        return

def  identifier_():
    global i,temp_count
    i=i-1
    next_,type_=getNextToken()
    identi=next_
    next_,type_=getNextToken()
    if next_=='pp':
        code.append([next_])
        temp_count+=1
        code[temp_count].append([identi])
        size=sys.getsizeof(identi)
        symbol_(identi,value=str(int(sym_tab[identi][0])+1),size=size)
        print(sym_tab)
    else:
        i=i-1
def print_():
    global code,i,temp_count,in_if
    i=i-1
    next_,type_=getNextToken()
    code.append([next_])
    temp_count+=1
    next_,type_=getNextToken()
    code[temp_count].append([next_])
    
def if_loop():
    print("IN IF LOOP")
    global code,i,temp_count,in_if
    i=i-1
    next_,type_=getNextToken()
    code.append([next_])
    temp_count+=1
    next_,type_=getNextToken()
    if(next_=='|'):
        next_,type_=getNextToken()
        if(type_=="IDENTIFIER"):
            identi=next_
            next_,type_=getNextToken()
            if(type_=="REL_OPERATORS"):
                code.append([next_])
                temp_count=temp_count+1
                next_,type_=getNextToken()
                if(type_=="IDENTIFIER" or type_=="INTEGER"):
                    code[temp_count].append([identi,next_])
                    next_,type_=getNextToken()
                    if(next_=='|'):
                        next_,type_=getNextToken()
                        if(next_=='--'):
                            code.append("(then)")
                            temp_count=temp_count+1
                            in_if=1
