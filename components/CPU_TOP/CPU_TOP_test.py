import random
import pytest
import copy
import collections

from pymtl import *
from pclib.test import run_test_vector_sim

class CPU_TOP(VerilogModel):
	def __init__(s):
		s.debug = InPort(1)
		s.inr = InPort(3)
		s.outvalue = OutPort(16)
		s.pc = OutPort(10)
		s.memory_address = OutPort(10)
		s.outvale = OutPort(16)
		s.set_ports({
			'clock': s.clk,
			'reset': s.reset,
			'debug': s.debug,
			'inr': s.inr,
			'pc': s.pc,
			'memory_address': s.memory_address,
			'outvalue': s.outvalue
			})

	def line_trace( s ):
		return '{} {} {}'.format(s.pc,s.memory_address,s.outvalue)


vector_header = ['reset debug inr pc* memory_address* outvalue*']

expected_pc = [0,1,2,3,4,5,6,7,8,9,10,11,12,5,6,7,8,9,10,11,12,5,6,7,8,9,10,11,12,5,6,7,8,9,10,11,12,5,6,7,8,9,10,11,12,13]
expected_load_address = [263,264,265,266,267,268]
expected_store_address = [269,270,271,272,273,274]
expected_outvalue = [6,8,9,10,11,12]

def gen_test_vector():
	test_vector = []
	for pc in expected_pc:
		row = [0,0,0,'?','?','?'];
		if pc == 7:
			row[4] = expected_load_address.pop(0)
		if pc == 10:
			row[4] = expected_store_address.pop(0)
			row[5] = expected_outvalue.pop(0)
		test_vector.append(row)
	return test_vector

def test_sample_program( dump_vcd ):
	test_vector = copy.deepcopy(vector_header)
	test_vector = test_vector + gen_test_vector()
	run_test_vector_sim(CPU_TOP(), test_vector, dump_vcd)
	
