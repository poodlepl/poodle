import re
import pprint
from wordlist import keywords

pp = pprint.PrettyPrinter(indent = 4)

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
			elif word == "wrap": tokens.append([keywords[word], word])
			# This will recognise an assignment operator
			elif word == "as" : tokens.append(["ASSIGNMENT", word])

			#This will recognise a unary operator and create a unary operator token for it
			elif word == "pp" or word == "mm": 
				tokens.append([keywords[word], word])
				
			#This will recognise equality expression

			elif word == "eq" :  tokens.append([keywords[word], word])

			#This will recognise the not equal expression

			elif word == "neq": tokens.append([keywords[word], word])

			#This will recognise vomit keyword

			elif word == "vomit": 
				tokens.append([keywords[word], word])
				
			#This will recognise the relational operators

			elif word == "let" or word == "lete" or word == "get" or word == "gete":
				tokens.append([keywords[word], word])

			#This will recognise the jump statements

			elif word == "goto" or word =="continue" or word == "break" or word == "return" :
				tokens.append([keywords[word], word])

			#This will recognise logical OR operator

			elif word == "$$": tokens.append([keywords[word], word])

			#This will recognise logical AND operator
			elif word == "&&": tokens.append([keywords[word], word])

			#This is the equivalent of flower braces
			elif word == "--": tokens.append([keywords[word], word])

			elif word == "---": tokens.append([keywords[word], word])

			#This is equivalent of paranthesis 
			elif word == "|" : tokens.append([keywords[word], word])

			#This is for simple if condition
			elif word == ".2" : tokens.append([keywords[word], word])

			#this is for elseif condition
			elif word == ".3" : tokens.append([keywords[word], word])

			#This is for else condition
			elif word == ".4": tokens.append([keywords[word], word])

			#This is for seperator 

			elif word == ":": tokens.append([keywords[word], word])

			#This is for for loop
			elif word == ".5": tokens.append([keywords[word], word])

			#This is for while condition
			elif word == ".6": tokens.append([keywords[word], word])

			#This is for do condition
			elif word == ".7": tokens.append([keywords[word], word])

			#This will recognise a word and create an identifier token for it
			elif re.match('[a-z]', word) or re.match('[A-Z]', word):
				tokens.append(['IDENTIFIER', word])

			#This will recognise an integer and create an identifier token for it
			elif re.match('[0-9]', word):
				tokens.append(['INTEGER ', word])


			#This will recognise operators
			elif word in "%/*-+":
				tokens.append(['OPERATOR',word])




		#increases word index after checking it
			source_index += 1
		#pp.pprint(tokens)
		
		pp.pprint(strings)
		
		for line in tokens:
			print('\t'.join(line))

		#Return created tokens
		return tokens




 
