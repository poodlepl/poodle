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
    
    switch={
		"??" : "Comment",
		".5" : "For loop",
		"wrap" : "keyword",
		"as" : "keyword",
		"let" : "keyword",
		"pp" : "incrementer"
	}
	num=[0,1,2,3,4,5,6,7,8,9]
	data=switch.keys()
	words = filecontents.split('\n')
	print(words)
	for w in words:
		c=0
		tokens=w.split(" ")
		for tok in tokens:
			#print(tok)
			if c==1:
				continue
			elif tok in data:
				print("Token:",tok,"  Category:",switch[tok])
				if tok=='??':
					print("Comment : ",w[2:])
					c=1

    
    '''
    iterate through em all and process it.
    take raw string
    if there is extra char, check. isAlpha() and all.
    '''
		

#print(keywords)
#print(relop)
