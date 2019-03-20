import random

from pymtl import *
from pclib.test import run_test_vector_sim
from Reg import Reg

def test_mux_fixed( dump_vcd ):
	run_test_vector_sim( Reg( dtype=8, nports=2 ), [
		('sel  [ports]         *val'),
		[ 1,   [0x00, 0x00],    '?' ],
		[ 1,   [0xff, 0x00],    0x00],
		[ 0,   [0xff, 0x00],    0xff],
		[ 0,   [0x33, 0x00],    0x33],
		[ 1,   [0x00, 0xaa],    0xaa],
	], dump_vcd )