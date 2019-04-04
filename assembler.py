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


def pop_bits(value, split):
	if value.bit_length() <= split:
		return (value, 0)
	mask = ((1 << split) - 1) << (value.bit_length() - split)
	return ((value & mask) >> (value.bit_length() - split), value & ~mask)


def enumerate_syntax(instruction, ISA, symbol_table):
	temp = copy.deepcopy(ISA['instructions'][instruction['memonic']])
	temp['memonic'] = instruction['memonic']
	temp['rx'] = ISA['registers'][instruction['rx']]
	temp['rz'] = ISA['registers'][instruction['rz']]
	if instruction['ry'] is not None and instruction['ry'] in ISA['registers']:
		temp['ry'] = ISA['registers'][instruction['ry']]
	if instruction['memonic'] == 'BEQ' and instruction['ry'] in symbol_table:
		# This is a branch label
		temp['kk'] = symbol_table[instruction['ry']]
		temp['rx'] = temp['rz']
		temp['ry'] = temp['rx']
	if instruction['memonic'] == 'BEQ' and instruction['ry'] not in symbol_table:
		# This is a branch address
		temp['kk'] = instruction['ry']
		temp['rx'] = temp['rz']
		temp['ry'] = temp['rx']
	if instruction['kk'] is not None:
		temp['kk'] = int(instruction['kk'])
	return temp


def encode_instruction(tokens, ISA, symbol_table):
	temp = 0
	for fields in tokens['format']:
		field_name = fields.pop(0)
		value = tokens[field_name]
		for start, length in fields:
			section, value = pop_bits(value, length)
			temp = temp + ((section << (start - length + 1)))
		if value != 0:
			raise ValueError('Value larger than field: {} {}'.format(value,length))
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
		tokens = enumerate_syntax(instruction, ISA, symbol_table)
		binary = encode_instruction(tokens, ISA, symbol_table)
		pretty_print = tokens['print'].format(i=tokens)
		print("{0} {1}".format(binary, pretty_print))


if __name__ == "__main__" : main()