from pymtl import *
from pclib.test import run_test_vector_sim
from PC_Adder import PC_Adder


def test_add_fixed( dump_vcd ):
	run_test_vector_sim( PC_Adder( 8 ), [ 
	('op1   op2 result*'),
	[ 0x01, 0x01, 0x02],
	[ 0x03, 0x04, 0x07],
	[ 0xFF, 0x00, 0xFF],
	[ 0x02, 0xFF, 0x01],
	] , dump_vcd)
