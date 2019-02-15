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
			elif word in keywords.keys():
				 tokens.append([keywords[word], word])
				 print(word)
			
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




 
