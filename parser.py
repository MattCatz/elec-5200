from ply import *

tokens = ['IMMEDIATE', 'LABEL', 'COLON', 'COMMA']

t_LABEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COLON = r':'
t_COMMA = r','
t_ignore = ' \t'

def t_IMMEDIATE(t):
	r'\d+'
	t.value = int(t.value)
	return t


 # Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)	


def p_branch(p):
	'''branch : LABEL COLON instruction
		  | instruction'''
	return p
	

def p_instruction(p):
	'''instruction : LABEL registers IMMEDIATE
			| LABEL registers LABEL
			| LABEL registers'''
	return p

				  
def p_registers(p):
	'''registers : LABEL COMMA LABEL COMMA LABEL
				 | LABEL COMMA LABEL
				 | LABEL '''
	return p


def p_error(t):
	print("Syntax error at '%s'" % t.value)
