!#/use/bin/python

import re

pc = 0
symbol_table = {}

class Instruction (Object):
	__init__(s, memonic, rZ, rX, rY, kk, label):
		s.memonic = memonic
		s.rZ = rZ
		s.rX = rX
		s.rZ = rZ
		s.kk = kk
		s.label = label


	__str__(s):
		

def main():
	pattern = "(\w+\s*:\s*)?\w+\s*\w+\s*,\s*\w+\s*,\s*\w+"
	prog = re.compile(pattern)

	try:
		with open("test.asm") as fp:
			line = fp.readline()
			pc = pc + 1
			while line:
				match = prog.match(line)
				if match[1]: symbol_table.append(match[1], pc)



if __name__ "__main__" : main()