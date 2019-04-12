import ply.lex as lex

tokens = ['LABEL', 'MEMONIC', 'IMMEDIATE', 'COLON', 'COMMA']

t_LABEL = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_MEMONIC = r'[a-zA-Z]*'
t_COLON = r':'
t_COMMA = r','
t_IGNORE = r' \t'

def t_IMMEDIATE(t):
	r'\d+'
	t.value = int(t.value)
	return t
	

def p_branch(p):
	'''branch : LABEL COLON instruction'''
	
def p_instruction(p):
	'''instruction: MEMONIC registers IMMEDIATE
				  | MEMONIC registers LABEL
				  | MEMONIC registers'''
				  
def p_registers(p):
	'''registers : LABEL COMMA LABEL COMMA LABEL
				 | LABEL COMMA LABEL
				 | LABEL '''
