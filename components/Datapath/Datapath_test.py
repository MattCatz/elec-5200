import random
import pytest
import copy
import collections

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
      s.immediate = InPort(11)
      s.pc = OutPort(10)
      s.word_w = OutPort(16)
      s.word_a = OutPort(10)


regular = {
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

template_inputs = collections.OrderedDict(regular)


def gen_table_header( inputs ):
   output = ""
   for key, value in inputs.iteritems():
      output = output + key + ' '
   return output


def gen_table_row( inputs ):
   output = []
   for key, value in inputs.iteritems():
      output.append(value)
   return output


def fill_registers(template):
   output = []
   for index in xrange(8):
      temp = copy.deepcopy(template)
      temp['regfile_w'] = 0x1
      temp['data_s'] = 0x2
      temp['rZ_address'] = index
      temp['word_r'] = 0x01
      temp['pc*'] = index + 2
      output.append(gen_table_row(temp)[:])
   return output


def test_branch_type( dump_vcd ):
   temp = copy.deepcopy(template_inputs)
   test_vector = [gen_table_header(temp)]
   test_vector = test_vector + fill_registers(temp)

   temp['data_s'] = 0x4
   temp['pc_s'] = 0x1
   temp['immediate'] = 0x0F
   temp['pc*'] = 0xA 
   test_vector.append(gen_table_row(temp)[:])

   temp = copy.deepcopy(template_inputs)
   temp['pc*'] = 0xA + 0xF
   test_vector.append(gen_table_row(temp)[:])

   model = Datapath()
   model._auto_init()

   run_test_vector_sim(model, test_vector, dump_vcd)


def test_jump_type( dump_vcd ):
   temp = copy.deepcopy(template_inputs)
   test_vector = [gen_table_header(temp)]
   test_vector = test_vector + fill_registers(temp)

   temp['rX_address'] = 0x1
   temp['rY_address'] = 0x1

   temp['data_s'] = 0x4
   temp['pc_s'] = 0x1
   temp['immediate'] = 0x0F
   temp['pc*'] = 0xA
   temp['word_a*'] = '?'
   temp['word_w*'] = '?'
   temp['alu_s'] = 0x6
   test_vector.append(gen_table_row(temp)[:])

   temp = copy.deepcopy(template_inputs)
   temp['pc*'] = 0xA + 0xF
   test_vector.append(gen_table_row(temp)[:])

   print test_vector

   model = Datapath()
   model._auto_init()

   run_test_vector_sim(model, test_vector, dump_vcd)


def test_LW_SW( dump_vcd ):
   temp = copy.deepcopy(template_inputs)

   temp['regfile_w'] = 0x1

   temp['data_s'] = 0x2
   temp['operand_s'] = 0x3

   temp['rX_address'] = 0x1
   temp['rY_address'] = 0x1
   temp['rZ_address'] = 0x1

   temp['word_r'] = 0xFF

   temp['pc*'] = 0x2

   model = Datapath()
   model._auto_init()

   test_vector = [gen_table_header(temp)]
   test_vector.append(gen_table_row(temp)[:])

   temp['regfile_w'] = 0x0
   temp['word_r'] = 0x0
   temp['pc*'] = 0x3
   temp['word_w*'] = 0xFF
   temp['word_a*'] = '?'

   test_vector.append(gen_table_row(temp)[:])
   run_test_vector_sim(model, test_vector, dump_vcd)


def test_RR_type( dump_vcd ):
   # Lets try a basic Add instruction
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
   temp = copy.deepcopy(template_inputs)

   temp['regfile_w'] = 0x1
   temp['alu_s'] = 0x1
   temp['data_s'] = 0x1
   temp['operand_s'] = 0x1

   temp['rX_address'] = 0x1
   temp['rY_address'] = 0x2
   temp['rZ_address'] = 0x3
   temp['immediate'] = 0xFF

   temp['pc*'] = 0x2
   temp['word_a*'] = '?'

   model = Datapath()
   model._auto_init()

   test_vector = [gen_table_header(temp)]
   test_vector.append(gen_table_row(temp))
   run_test_vector_sim(model, test_vector, dump_vcd)

