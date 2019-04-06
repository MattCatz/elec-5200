import random
import pytest
import copy
import collections

from pymtl import *
from pclib.test import run_test_vector_sim

class CPU_TOP(VerilogModel):
	def __init__(s):
		s.set_ports({
			'clock': s.clk,
			'reset': s.reset
			})


def simple_test( dump_vcd ):
	CPU_TOP()