import random
import pytest
import copy

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




template_inputs = {
   "reset": 0x0,
   "regfile_w": 0x0,
   "rX_address": 0x0,
   "rY_address": 0x0,
   "rZ_address": 0x0,
   "alu_s": 0x0,
   "data_s": 0x0,
   "operand_s": 0x0,
   "pc_s": 0x0,
   "word_r": 0x0,
   "immediate": 0x0,
   "pc*": 0x0,
   "word_w*": 0x0,
   "word_a*": 0x0,
}

def gen_table_header( inputs ):
   output = ""
   for key, value in inputs:
      output = output + key + ' '
   return output

def gen_table_row( inputs ):
   output = []
   for key, value in inputs:
      output.append(value)
   return output

top_signals = " reset regfile_w "
control_signals = " alu_s data_s operand_s pc_s "
decoder_signals = " rX_address rY_address rZ_address immediate "
external_memory_signals = " word_r "

signals_to_external_memory = " pc* word_w* word_a* "

def test_simple( dump_vcd ):
   model = Datapath()
   model._auto_init()


def test_gen_inputs():
   print gen_table_header(template_inputs)


def test_LW( dump_vcd ):
   fixed_top_signals = [0x0, 0x1]
   # Because the sim does a cycle for us we are at pc 2
   RR_control = [0x0, 0x2, 0x3, 0x0]
   RR_decoder = [0x1, 0x1, 0x1, 0x0]
   RR_memory  = [0xFF]
   RR_outputs = [0x2, 0x0, 0x0]

   model = Datapath()
   model._auto_init()

   test_vector = [(top_signals + control_signals + decoder_signals + external_memory_signals + signals_to_external_memory)]
   test_vector.append(fixed_top_signals + RR_control + RR_decoder + RR_memory + RR_outputs)
   test_vector.append([0x0, 0x0] + RR_control + RR_decoder + [0x0] + [0x3, 0xFF, '?'])
   run_test_vector_sim(model, test_vector, dump_vcd)


def test_RR_type( dump_vcd ):
   # Lets try a basic Add instruction
   fixed_top_signals = [0x0, 0x1]
   # Because the sim does a cycle for us we are at pc 2
   RR_control = [0x1, 0x1, 0x0, 0x0]
   RR_decoder = [0x1, 0x2, 0x3, 0x0]
   RR_memory  = [0x0]
   RR_outputs = [0x2, 0x0, 0x0]

   temp = copy.deepcopy(template_inputs)

   temp['regfile_w'] = 0x1
   temp['alu_s'] = 0x1
   temp['data_s'] = 0x1

   temp['rX_address'] = 0x1
   temp['rY_address'] = 0x2
   temp['rZ_address'] = 0x3

   temp['pc*'] = 0x2

   model = Datapath()
   model._auto_init()

   test_vector = [gen_table_header(temp)]
   test_vector.append(gen_table_row(temp))

   run_test_vector_sim(model, test_vector, dump_vcd)


def test_RI_type( dump_vcd ):
   # Lets try a basic Add immedate
   fixed_top_signals = [0x0, 0x1]
   # Because the sim does a cycle for us we are at pc 2
   RR_control = [0x1, 0x1, 0x1, 0x0]
   RR_decoder = [0x1, 0x2, 0x3, 0xFF]
   RR_memory  = [0x0]
   RR_outputs = [0x2, 0x0, '?']

   model = Datapath()
   model._auto_init()

   test_vector = [(top_signals + control_signals + decoder_signals + external_memory_signals + signals_to_external_memory)]
   test_vector.append(fixed_top_signals + RR_control + RR_decoder + RR_memory + RR_outputs)

   run_test_vector_sim(model, test_vector, dump_vcd)
