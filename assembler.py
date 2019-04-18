#!/usr/bin/env python

import re
import yaml
import copy

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
	label_re = r'(?P<label>\w+)?\s*:?\s*'
	memonic_re = r'(?P<memonic>\w+)\s+'
	rz_re = r'(?P<rz>\w+)\s*,\s*'
	rx_re = r'(?P<rx>\w+)\s*,\s*'
	ry_or_kk_re = r'(?P<kk>\d+)?(?P<ry>\w+)?'
	offset = r'?\[?(?P<offset>\d+)?\]?'
	prog = re.compile(label_re + memonic_re + rz_re + rx_re + ry_or_kk_re)
	pc = 0
	program = []

	ISA = get_isa("isa.yaml")
	symbol_table = ISA['registers']

	# First Pass
	with open("test.asm", 'r') as fp:
		line = fp.readline()
		while line:
			match = prog.match(line).groupdict()
			if match["label"]: 
				symbol_table[match["label"]] = pc
			program.append(match)
			pc = pc + 1
			line = fp.readline()

	# Second Pass
	for instruction in program:
		tokens = enumerate_syntax(instruction, ISA, symbol_table)
		binary = encode_instruction(tokens, ISA, symbol_table)
		pretty_print = tokens['print'].format(i=tokens)
		print("{0} {1}".format(binary, pretty_print))


if __name__ == "__main__" : main()
