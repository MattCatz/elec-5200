import random

from pymtl import *
from pclib.test import run_test_vector_sim
from ALU import ALU

def alu_gen_random( o, f ):
	test_vector_table=[('op1 op2 operation result*')]
	last_result = 0x0
	for i in xrange(40):
		rand_1 = Bits(16, random.randint( -0x8000,0x7FFF ))
		rand_2 = Bits(16, random.randint( -0x8000,0x7FFF ))
		test_vector_table.append( [rand_1, rand_2, o, last_result] )
		last_result = Bits( 16, f( rand_1, rand_2 ))
	return test_vector_table

	

def test_add_fixed( dump_vcd ):
	run_test_vector_sim( ALU( 16 ), [ 
	('op1     op2 operation result*'),
	[ 0x1,    0x1,      0x1,     0x0],
	[ 0x3,    0x4,      0x1,     0x2],
	[ 0xFF00, 0x00FF,   0x1,     0x7],
	[ 0x2,    0xFFFE,   0x1,     0xFFFF],
	[ 0x2,    0xFFFF,   0x1,     0x0],
	[ 0x0,    0x0,      0x1,     0x1],
	] , dump_vcd)


def test_add_random(dump_vcd):
	f = lambda x,y: x+y
	test_vector_table = alu_gen_random(0x1,f)
	run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_sub_fixed( dump_vcd ):
	run_test_vector_sim( ALU( 16 ), [ 
	('op1     op2 operation result*'),
	[ 0x1,    0x1,      0x2,     0x0],
	[ 0x3,    0x4,      0x2,     0x0],
	[ 0xFF00, 0x00FF,   0x2,     0xFFFF],
	[ 0x2,    0xFFFE,   0x2,     0xFE01],
	[ 0x0,    0x0,      0x2,     0x4],
	] , dump_vcd)


def test_sub_random( dump_vcd ):
	f = lambda x,y: x-y
	test_vector_table = alu_gen_random( 0x2, f )
	run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_and_fixed( dump_vcd ):
	assert 0


def test_and_random( dump_vcd ):
	assert 0


def test_or_fixed( dump_vcd ):
	assert 0


def test_or_random( dump_vcd ):
	assert 0


def test_less_than_fixed( dump_vcd ):
	assert 0


def test_less_than_random( dump_vcd ):
	assert 0


def test_equal_fixed( dump_vcd ):
	assert 0


def test_equal_random( dump_vcd ):
	assert 0


def test_invalid_operation( dump_vcd ):
	assert 0
