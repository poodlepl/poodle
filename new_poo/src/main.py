from lexer import Lexer

def main():
	#Read the current poodle source code in test.lang and store it in variable
	content =""
	with open('lang/test.lang', 'r') as file:
		content = file.read()
	#
	#lexer
	#
	# We call the lexer class and initialize it with
	lex = Lexer(content)
	lex.tokenize()
	# We now call the tokenize method
	
if __name__ == "__main__":
	main()