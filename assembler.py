#!/usr/bin/python3

import re
import yaml
import copy

def get_isa(file_name):
	ISA = None
	with open(file_name, 'r') as stream:
		try:
			ISA = yaml.load(stream)
		except tam.YAMLError as e:
			print(e)
	return ISA

def enumerate_syntax(instruction, ISA, symbol_table):
	temp = copy.deepcopy(ISA['instructions'][instruction['memonic']])
	temp['rx'] = ISA['registers'][instruction['rx']]
	temp['rz'] = ISA['registers'][instruction['rz']]
	if instruction['ry'] is not None and instruction['ry'] in ISA['registers']:
		temp['ry'] = ISA['registers'][instruction['ry']]
	if instruction['ry'] is not None and instruction['ry'] in symbol_table:
		# This is a branch label
		temp['kk'] = int(instruction['ry'])
	if instruction['kk'] is not None:
		temp['kk'] = int(instruction['kk'])

	return temp


def format_instruction(instruction, ISA, symbol_table):
	tokens = enumerate_syntax(instruction, ISA, symbol_table)
	return tokens['format'].format(i=tokens)


def main():
	label_re = r'(?P<label>\w+)?\s*:?\s*'
	memonic_re = r'(?P<memonic>\w+)\s+'
	rz_re = r'(?P<rz>\w+)\s*,\s*'
	rx_re = r'(?P<rx>\w+)\s*,\s*'
	ry_or_kk_re = r'(?P<kk>\d+)?(?P<ry>\w+)?'
	offset = r'?\[?(?P<offset>\d+)?\]?'
	pattern = label_re + memonic_re + rz_re + rx_re + ry_or_kk_re
	prog = re.compile(pattern)

	pc = 0
	symbol_table = {}
	program = []
	dissassembly = ""
	hex_dump = ""

	ISA = get_isa("isa.yaml")

	# First Pass

	with open("test.asm", 'r') as fp:
		line = fp.readline()
		while line:
			match = prog.match(line).groupdict()
			if match["label"]: symbol_table[match["label"]] = pc
			program.append(match)
			pc = pc + 1
			line = fp.readline()

	# Second Pass

	for instruction in program:
		print(format_instruction(instruction, ISA, symbol_table))


if __name__ == "__main__" : main()