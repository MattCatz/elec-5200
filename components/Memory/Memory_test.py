import random

from pymtl import *
from pclib.test import run_test_vector_sim
from Memory import Memory as Memory_sv

test_vector_header = ("clk_en write_A Address_A Data_A Out_A* write_B Address_B Data_B Out_B*")

def gen_data( width, length ):
   upper = 2**(width-1)-1
   lower = -2**(width-1)-1
   test_data = [None] * length
   for i in xrange( length ):
      test_data[i] = Bits(width, random.randint(lower,upper))
   return test_data

def gen_vector_table(data):
   test_vector_table = [] * (len(data) + 1)
   test_vector_table.append(test_vector_header)
   for idx, val in enumerate(data):
      test_vector_table.append( [1, 1, idx, val,   0, 0, 0, 0, '?'] )
      test_vector_table.append( [0, 0, idx,   0, val, 0, 0, 0, '?'] )
   return test_vector_table


def test_simple( dump_vcd ):
   model = Memory_sv(dtype=16, lines=1024)
   data_A = gen_data(16, 1024)
   test_vector_table = gen_vector_table(data_A)
   run_test_vector_sim(model, test_vector_table, dump_vcd)
