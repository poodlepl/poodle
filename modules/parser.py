from modules.lex import *
import pprint
import sys
import tokenize
from modules.symbol import *


flag = -1
symbolTable, inp_list = None, None
in_if=0
temp_count = -1
label_count = 0
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
            elif next_==".6":
                while_()
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


def while_():
    global flag
    next_, type_ = getNextToken()
    op_pipe = next_
    if op_pipe == '|':
        Condition()

        if (flag == 0):
            print('Condition Failed. Exit Loop')
            pass

        elif (flag == 1):
            next_, type_ = getNextToken()
            cl_pipe = next_
            if cl_pipe == '|':
                print("While condition passed")
            else:
                print("SYNTAX ERROR: Expected \'|\'")

        #TODO
        # add end here
    else:
        print("ERROR: Missing opening bracket.")

def Condition():
    global flag
    left, l_type_ = getNextToken()
    left_id = left
    l_val = int(sym_tab[left_id][0])
    if l_type_ == 'IDENTIFIER':
        oper, op_type_ = getNextToken()

        if oper == 'eq':
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val == r_val:
                        print("Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val == r_val:
                        print("Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0

        elif oper == 'neq':

            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val != r_val:
                        print("Not Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val != r_val:
                        print("Not Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'let':

            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val < r_val:
                        print("Less than")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val < r_val:
                        print("Less than")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'lete':

            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val <= r_val:
                        print("Less than Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val <= r_val:
                        print("Less than Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'get':

            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val > r_val:
                        print("Greater")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val > r_val:
                        print("Greater")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
        elif oper == 'gete':

            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    if l_val >= r_val:
                        print("Greater than Equal")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    if l_val >= r_val:
                        print("Greater than Equal")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0

        else:
            print("ERROR: Invalid operator")

    else:
        print("ERROR: Expected identifier")
