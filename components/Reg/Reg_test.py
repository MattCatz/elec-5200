import random

from pymtl import *
from pclib.test import run_test_vector_sim
from Reg import Reg,Shifter

def test_register_fixed( dump_vcd ):
	run_test_vector_sim( Reg( 8 ), [
		('in_ w_en out*'),
		[0x00, 1,  '?' ],
		[0xf0, 1,  0x00],
		[0x0f, 0,  0xf0],
		[0x00, 0,  0xf0],
		[0x00, 1,  0xf0],
		[0x00, 0,  0x00],
	], dump_vcd )

def test_register_priority( dump_vcd ):
	run_test_vector_sim( Reg( 8 ), [
		('reset  in_  w_en out*'),
		[    1, 0x00,   1,  '?' ],
		[    1, 0xff,   1,  0x00],
		[    1, 0xff,   0,  0x00],
		[    1, 0x00,   0,  0x00],
	], dump_vcd )

def test_shifter( dump_vcd ):
	run_test_vector_sim( Shifter( dtype=16, amount=4 ), [
		('in_     out*'),
		[0x0000,   '?' ],
		[0x00ff, 0x0ff0],
		[0xf0f0, 0x0f00],
		[0x0ff0, 0xff00],
		[0xffff, 0xfff0],
	], dump_vcd )
