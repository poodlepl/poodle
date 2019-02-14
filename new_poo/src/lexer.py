import re
import pprint


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

	#Basically this will keep track if undex numberswe are at in the source code

		source_index =0

	#loop through each word in source code to generate tokens
		while source_index<len(source_code):
			word = source_code[source_index]
			# This will recognise a variable and create a token for it
			if word == "wrap": tokens.append(["VAR_DECLARATION", word])
			# This will recognise an assignment operator
			elif word == "as" : tokens.append(["ASSIGNMENT",		 word])

			#This will recognise a unary operator and create a unary operator token for it
			elif word == "pp" or word == "mm": tokens.append(["UNARY_OPERATOR", 	word])

			#This will recognise equality expression

			elif word == "eq" :  tokens.append(["EQ_OPERATOR", word])

			#This will recognise the not equal expression

			elif word == "neq": tokens.append(["NOT_EQ_OPERATOR", word])

			#This will recognise vomit keyword

			elif word == "vomit": tokens.append(["PRINT_KEYWORD", word])
			#This will recognise the relational operators

			elif word == "let" or word == "lete" or word == "get" or word == "gete":
				tokens.append(["REL_OPERATORS", word])

			#This will recognise the jump statements

			elif word == "goto" or word =="continue" or word == "break" or word == "return" :
				tokens.append(["JUMP_STATEMENTS", word])

			#This will recognise logical OR operator

			elif word == "$$": tokens.append(["OR_OPERATOR", word])

			#This will recognise logical AND operator
			elif word == "&&": tokens.append(["AND_OPERATOR", word])

			#This is the equivalent of flower braces
			elif word == "--": tokens.append(["OPEN CONDITION", word])

			elif word == "---": tokens.append(["CLOSE CONDITION", word])

			#This is equivalent of paranthesis 
			elif word == "|" : tokens.append(["PARANTHESIS", word])

			#This is for simple if condition
			elif word == ".2" : tokens.append(["IF_CONDITION", word])

			#this is for elseif condition
			elif word == ".3" : tokens.append(["ELSE-IF_COND", word])

			#This is for else condition
			elif word == ".4": tokens.append(["ELSE CONDITION", word])

			#This is for seperator 

			elif word == ":": tokens.append(["SEPERATOR", word])

			#This is for for loop
			elif word == ".5": tokens.append(["FOR LOOP", word])

			#This is for while condition
			elif word == ".6": tokens.append(["WHILE CONDITION", word])

			#This is for do condition
			elif word == ".7": tokens.append(["DO CONDITION", word])

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
		
		for line in tokens:
			print('\t\t'.join(line))

		#Return created tokens
		return tokens




 