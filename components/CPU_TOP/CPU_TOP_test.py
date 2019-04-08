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
		s.instruction = InPort(16)
		s.memory_fetch = InPort(16)
		s.pc = OutPort(10)
		s.memory_address = OutPort(10)
		s.set_ports({
			'clock': s.clk,
			'reset': s.reset,
			'debug': s.debug,
			'inr': s.inr,
			'outvalue': s.outvalue,
			'instruction': s.instruction,
			'memory_fetch': s.memory_fetch,
			'pc': s.pc,
			'memory_address': s.memory_address
			})


def test_simple( dump_vcd ):
	CPU_TOP()


