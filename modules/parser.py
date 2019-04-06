from modules.lex import *
import pprint
import operator
import sys
import tokenize
from modules.symbol import *


left_val = right_val = -1
cond = -1
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


def while_():
    global flag, left_val, right_val, cond
    next_, type_ = getNextToken()
    op_pipe = next_
    if op_pipe == '|':
        Condition()

        if (flag == 0):
            print('Condition Failed. But still need to check syntax.')
            afterCondition()

        else:
            # TODO
            # Check TODO.
            while flag != 1:
                afterCondition()
                if cond(left_val, right_val):
                    print("Continue while loop because left is " + left_val)
                else:
                    print("Left value does not satisfy the condition on the right value. Append in the symbol table now.")
                    # TODO
                    # exit while loop

    else:
        print("ERROR: Missing opening bracket.")

def afterCondition():
    next_, type_ = getNextToken()
    cl_pipe = next_
    if cl_pipe == '|':

        next_, type_ = getNextToken()
        op_par = next_

        if op_par == '--' :
            next_, type_ = getNextToken()
            stat = next_

            if stat == 'vomit':
                #print_()
                next_, type_ = getNextToken()
                right_stat = type_

                if right_stat == 'IDENTIFIER':
                    next_, type_ = getNextToken()
                    exit_val = type_

                    # TODO
                    # Check TODO
                    if exit_val == 'EXIT LOOP':
                        next_, type_ = getNextToken()
                        clos_par = next_

                        if clos_par == '---':
                            print('WHILE ENDED SUCCESSFULLY')

                        else:
                            print('SYNTAX ERROR: Invalid SYNTAX: Expected \'---\'')
                            # TODO
                            # exit the while loop only
                    else:
                        print('SYNTAX ERROR: Invalid SYNTAX: Expected \'exit()\'')
                        # TODO
                        # exit the while loop only
                else:
                    print('SYNTAX ERROR: Invalid SYNTAX: Expected \'IDENTIFIER\'')
                    # TODO
                    # exit the while loop only
            else:
                print('SYNTAX ERROR: \'Invalid SYNTAX\'')
                # TODO
                # exit the while loop only
        else:
            print('SYNTAX ERROR: Expected \'--\'')
            # TODO
            # exit the while loop only

    else:
        print("SYNTAX ERROR: Expected \'|\'")
        # TODO
        # exit the while loop only

def Condition():
    global flag, left_val, right_val, cond
    left, l_type_ = getNextToken()
    left_id = left
    l_val = int(sym_tab[left_id][0])
    if l_type_ == 'IDENTIFIER':
        oper, op_type_ = getNextToken()

        code.append([oper])
        #print(code)
        if oper == 'eq':
            cond = operator.eq
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val == r_val:
                        print("CONDITION PASSED: Equality")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val == r_val:
                        print("CONDITION PASSED: Equality")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0

        elif oper == 'neq':
            cond = operator.ne
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val != r_val:
                        print("CONDITION PASSED: Not Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val != r_val:
                        print("CONDITION PASSED: Not Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'let':
            cond = operator.lt
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val < r_val:
                        print("CONDITION PASSED: Less than")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val < r_val:
                        print("CONDITION PASSED: Less than")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'lete':
            cond = operator.le
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val <= r_val:
                        print("CONDITION PASSED: Less than Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val <= r_val:
                        print("CONDITION PASSED: Less than Equal")
                        flag = 1
                    else:
                        #print("Not Equal")
                        flag = 0
        elif oper == 'get':
            cond = operator.gt
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])
                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val > r_val:
                        print("CONDITION PASSED: Greater")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val > r_val:
                        print("CONDITION PASSED: Greater")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
        elif oper == 'gete':
            cond = operator.ge
            right, r_type_ = getNextToken()
            if r_type_ == 'IDENTIFIER':
                r_val = int(sym_tab[right][0])

                if r_val == -1:
                    print('ERROR: Invalid types. Equality cannot be done on ' + type(l_type_)+' and ' + type(r_type_))
                else:
                    r_val = int(r_val)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val >= r_val:
                        print("CONDITION PASSED: Greater than Equal")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0
            else:
                if r_type_ == 'INTEGER':
                    r_val = int(right)
                    left_val = l_val
                    right_val = r_val
                    code.append([[left] + [right]])
                    if l_val >= r_val:
                        print("CONDITION PASSED: Greater than Equal")
                        flag = 1
                    else:
                        #print("FAIL")
                        flag = 0

        else:
            print("ERROR: Invalid operator")

    else:
        print("ERROR: Expected identifier")
