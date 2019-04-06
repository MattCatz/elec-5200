import random
import pytest
import copy
import collections

from pymtl import *
from pclib.test import run_test_vector_sim

class Decoder( VerilogModel ):
	def __init__(s):
	    s.word = InPort(16)
		s.opcode = OutPort(2)
		s.rX = OutPort(3)
		s.rY = OutPort(3)
		s.rZ = OutPort(3)
		s.func = OutPort(3)
		s.kk = OutPort(2)

		s.set_ports({
			'word': s.word,
			'opcode': s.opcode,
			'rX': s.rX,
			'rY': s.rY,
			'rZ': s.rZ,
			'func': s.func,
			'kk': s.kk
		})


non_sorted = {'word': 0x0,
			  'opcode*': 0x0,
			  'rX*': 0x0,
			  'rY*': 0x0,
			  'rZ*': 0x0,
			  'func*': 0x0,
			  'kk*': 0x0}

template_inputs = collections.OrderedDict(non_sorted)

def test_word( row ):
   output = ["", []]
   for key, value in inputs.iteritems():
      output[0] = output[0] + key + ' '
      output[1].append(value)
   
	run_test_vector_sim(Decoder(), output, dump_vcd)


def test_decode_ADDI( dump_vcd ):
	# 1101111001011001 ADDI 6 6 27
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b1101111001011001
	row['opcode*'] = 0b01
	row['rX*']     = 6
	row['rY*']     = '?'
	row['rZ*']     = 6
	row['func*']   = 0
	row['kk*']     = 27
	test_word(row)


def test_decode_LOAD( dump_vcd ):
	# 1000110000010001 LOAD 4 4 17
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b1000110000010001
	row['opcode*'] = 0b01
	row['rX*']     = 4
	row['rY*']     = '?'
	row['rZ*']     = 4
	row['func*']   = 1
	row['kk*']     = 17
	test_word(row)

def test_decode_STOR( dump_vcd ):
	# 0000001100101101 STOR 3 3 0
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_LUI( dump_vcd ):
	# 0100001001101001 LUI 2 2 8
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_ADD( dump_vcd ):
	# 0000100100000100 ADD 1 1 1
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_SUB( dump_vcd ):
	# 0000000000100000 SUB 0 0 0
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_AND( dump_vcd ):
	# 0010110101010100 AND 5 5 5
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_OR( dump_vcd ):
	# 0011011001111000 OR 6 6 6
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_SLT( dump_vcd ):
	# 0010010010010000 SLT 4 4 4
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_JAL( dump_vcd ):
	# 1000010101001110 JAL 3 1066
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)

def test_decode_BEQ( dump_vcd ):
	# 0001001000110111 BEQ 2 2 13
	row = copy.deepcopy(template_inputs)
	row['word'] = 0b0000001100101101
	row['opcode*'] = 0b01
	row['rX*']     = 3
	row['rY*']     = '?'
	row['rZ*']     = 3
	row['func*']   = 4
	row['kk*']     = 0
	test_word(row)
