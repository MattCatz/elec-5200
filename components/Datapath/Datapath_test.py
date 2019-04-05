import random
import pytest

from pymtl import *
from pclib.test import run_test_vector_sim

class Datapath( VerilogModel ):

   def __init__( s ):
      s.regfile_w = InPort(1)
      s.rX_address = InPort(3)
      s.rY_address = InPort(3)
      s.rZ_address = InPort(3)
      s.alu_s = InPort(3)
      s.data_s = InPort(4)
      s.operand_s = InPort(2)
      s.pc_s = InPort(1)
      s.word_r = InPort(16)
      s.immediate = InPort(8)
      s.pc = OutPort(12)
      s.word_w = OutPort(16)
      s.word_a = OutPort(10)


def test_simple( dump_vcd ):
   model = Datapath()
   model._auto_init()
