import re
from wordlist import switch


def lex(filecontents):
	#Lexer for FOR LOOP
	data=switch.keys()
	words = filecontents.split('\n')
	print(words)
	for w in words:
		c=0
		hyp=0
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
			elif tok.isdigit():
					print("Token: ",tok,"  Category: Numeral")
			elif tok=="--":
				if(hyp==0):
					print("Token:",tok,"  Category: Beginning of vomit")
					hyp=1
				else:
					print("Token:",tok,"  Category:End of vomit")	
			else:
				if tok.isalpha():
					print("Token:",tok,"  Category: Identifier")	

#print(keywords)
#print(relop)
