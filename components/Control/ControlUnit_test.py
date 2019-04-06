import random
import pytest
import copy
import collections

from pymtl import *
from pclib.test import run_test_vector_sim

class ControlUnit (VerilogModel):
	__init__(s):
		s.operation = InPort(2)
		s.funct = InPort(3)
		s.pc_s = OutPort(1)
		s.operand_s = OutPort(2)
		s.alu_s = OutPort(3)
		s.data_s = OutPort(4)
		s.data_w = OutPort(1)


non_ordered = {
	'operation': 0x0
	'funct': 0x0
	'pc_s*': 0x0
	'operand_s*': 0x0
	'alu_s*': 0x0
	'data_s*': 0x0
	'data_w*': 0x0
}

template_inputs = collections.OrderedDict(non_ordered)

def gen_table_header( inputs ):
   output = ""
   for key, value in inputs.iteritems():
      output = output + key + ' '
   return output


def gen_table_row( inputs ):
   output = []
   for key, value in inputs.iteritems():
      output.append(value)
   return output

def test_ctr_ADDI( dumpvcd ):
	# 11011110010 110 01 ADDI 6 6 27
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x1
	table_row['funct'] = 0x0
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x1
	table_row['alu_s*'] = 0x1
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

	test_vector = [gen_table_header(temp)]
	test_vector.append(gen_table_row(table_row)[:])

	model = ControlUnit()
	model._auto_init()

	run_test_vector_sim(model, test_vector, dump_vcd)

def test_ctr_LOAD( dumpvcd ):
	# 1000110000010001 LOAD 4 4 17
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x1
	table_row['funct'] = 0x1
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x1
	table_row['alu_s*'] = 0x1
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

	test_vector = [gen_table_header(temp)]
	test_vector.append(gen_table_row(table_row)[:])

	model = ControlUnit()
	model._auto_init()

	run_test_vector_sim(model, test_vector, dump_vcd)


def test_ctr_STOR( dumpvcd ):
	# 0000001100101101 STOR 3 3 0
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x1
	table_row['funct'] = 0x3
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x1
	table_row['alu_s*'] = 0x1
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

	test_vector = [gen_table_header(temp)]
	test_vector.append(gen_table_row(table_row)[:])

	model = ControlUnit()
	model._auto_init()

	run_test_vector_sim(model, test_vector, dump_vcd)


def test_ctr_LUI( dumpvcd ):
	# 0100001001101001 LUI 2 2 8
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x1
	table_row['funct'] = 0x7
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x2
	table_row['alu_s*'] = 0x0
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

	test_vector = [gen_table_header(temp)]
	test_vector.append(gen_table_row(table_row)[:])

	model = ControlUnit()
	model._auto_init()

	run_test_vector_sim(model, test_vector, dump_vcd)


def test_ctr_ADD( dumpvcd ):
	# 0000100100000100 ADD 1 1 1
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x0
	table_row['funct'] = 0x0
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x0
	table_row['alu_s*'] = 0x1
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

	test_vector = [gen_table_header(temp)]
	test_vector.append(gen_table_row(table_row)[:])

	model = ControlUnit()
	model._auto_init()

	run_test_vector_sim(model, test_vector, dump_vcd)


def test_ctr_SUB( dumpvcd ):
	# 0000000000100000 SUB 0 0 0
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x0
	table_row['funct'] = 0x1
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x0
	table_row['alu_s*'] = 0x2
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

def test_ctr_AND( dumpvcd ):
	# 0010110101010100 AND 5 5 5
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x0
	table_row['funct'] = 0x3
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x0
	table_row['alu_s*'] = 0x3
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

def test_ctr_OR( dumpvcd ):
	# 0011011001111000 OR 6 6 6
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x0
	table_row['funct'] = 0x7
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x0
	table_row['alu_s*'] = 0x4
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

def test_ctr_SLT( dumpvcd ):
	# 0010010010010000 SLT 4 4 4
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x0
	table_row['funct'] = 0x6
	table_row['pc_s*'] = 0x0
	table_row['operand_s*'] = 0x0
	table_row['alu_s*'] = 0x5
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

def test_ctr_JAL( dumpvcd ):
	# 1000010101001110 JAL 3 1066
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x2
	table_row['funct'] = '?'
	table_row['pc_s*'] = 0x1
	table_row['operand_s*'] = 0x1
	table_row['alu_s*'] = 0x5
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0

def test_ctr_BEQ( dumpvcd ):
	# 0001001000110111 BEQ 2 2 13
	table_row = copy.deepcopy(template_inputs)
	table_row['operation'] = 0x3
	table_row['funct'] = '?'
	table_row['pc_s*'] = 0x1
	table_row['operand_s*'] = 0x1
	table_row['alu_s*'] = 0x5
	table_row['data_s*'] = 0x1
	table_row['data_w*'] = 0x0
