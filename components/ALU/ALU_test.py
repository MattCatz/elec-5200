import random

from pymtl import *
from pclib.test import run_test_vector_sim
from ALU import ALU

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


def test_add_random( dump_vcd ):
	assert 0


def test_sub_fixed( dump_vcd ):
	assert 0


def test_sub_random( dump_vcd ):
	assert 0


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
