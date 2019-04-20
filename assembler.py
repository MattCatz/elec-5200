#!/usr/bin/env python

import re
import yaml
import copy

from parser import *

lexer = lex.lex()
parser = yacc.yacc()

def get_isa(file_name):
	ISA = None
	with open(file_name, 'r') as stream:
		try:
			ISA = yaml.load(stream, Loader=yaml.FullLoader)
		except tam.YAMLError as e:
			print(e)
	return ISA


def pop_bits(value, splits):
	for position, length in splits:
		shift = value.bit_length() - length
		next_yield = value
		if shift >= 0:
			mask = ((1 << length) - 1) << shift
			next_yield = (value & mask) >> shift
			value = value & ~mask
		yield next_yield << (position - length + 1)


def enumerate_syntax(instruction, ISA, symbol_table):
	temp = copy.deepcopy(ISA['instructions'][instruction['memonic']])
	temp['memonic'] = instruction['memonic']
	print(instruction)
	print(type(instruction['kk']))
	for key, value in instruction.items():
		temp[key] = symbol_table[value]
	return temp


def encode_instruction(tokens, ISA, symbol_table):
	temp = 0
	for fields in tokens['format']:
		field_name = fields.pop(0)
		value = tokens[field_name]
		for split in pop_bits(value, fields):
			temp += split
	return format(temp, '016b')

def main():
	program = []

	ISA = get_isa("isa.yaml")
	symbol_table = ISA['registers']

	# First Pass
	with open("test.asm", 'r') as fp:
		line = fp.readline()
		while line:
			#match = parser.parse(line)
			match = parser.parse(line)
			print(match)
			line = fp.readline()

	# Second Pass
	for instruction in program:
		tokens = enumerate_syntax(instruction, ISA, symbol_table)
		binary = encode_instruction(tokens, ISA, symbol_table)
		pretty_print = tokens['print'].format(i=tokens)
		print("{0} {1}".format(binary, pretty_print))


if __name__ == "__main__" : main()
