import random
import pytest


from pymtl import *
from pclib.test import run_test_vector_sim
from ALU import ALU

def alu_gen_random( o, f ):
   test_vector_table=[('op1 op2 operation result*')]
   for i in xrange(40):
      rand_1 = Bits(16, random.randint( -0x8000,0x7FFF ))
      rand_2 = Bits(16, random.randint( -0x8000,0x7FFF ))
      result = Bits( 16, f( rand_1, rand_2 ))
      test_vector_table.append( [rand_1, rand_2, o, result] )
      
   return test_vector_table


fixed_add_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x1,     0x2],
   [ 0x3,    0x4,      0x1,     0x7],
   [ 0xFF00, 0x00FF,   0x1,     0xFFFF],
   [ 0x2,    0xFFFE,   0x1,     0x0],
   [ 0x2,    0xFFFF,   0x1,     0x1]
   ]

fixed_sub_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x2,     0x0],
   [ 0x3,    0x4,      0x2,     0xFFFF],
   [ 0xFF00, 0x00FF,   0x2,     0xFE01],
   [ 0x2,    0xFFFE,   0x2,     0x4]
   ]

fixed_and_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x3,     0x1],
   [ 0x3,    0x4,      0x3,     0x0],
   [ 0xFF00, 0x00FF,   0x3,     0x0],
   [ 0x2,    0xFFFE,   0x3,     0x2],
   [ 0xA,    0xA,      0x3,     0xA],
   ]

fixed_or_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x4,     0x1],
   [ 0x3,    0x4,      0x4,     0x7],
   [ 0xFF00, 0x00FF,   0x4,     0xFFFF],
   [ 0x2,    0xFFFE,   0x4,     0xFFFE],
   [ 0xA,    0x5,      0x4,     0xF],
   ]

fixed_LT_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x5,     0x0],
   [ 0x3,    0x4,      0x5,     0x1],
   [ 0xFF00, 0x00FF,   0x5,     0x0],
   [ 0x2,    0xFFFE,   0x5,     0x1],
   [ 0xA,    0x5,      0x5,     0x0],
   ]

fixed_ET_vector = [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x6,     0x1],
   [ 0x3,    0x4,      0x6,     0x0],
   [ 0xFF00, 0x00FF,   0x6,     0x0],
   [ 0x2,    0xFFFE,   0x6,     0x0],
   [ 0xA,    0xA,      0x6,     0x1],
   ]

random_add_vector = alu_gen_random(0x1, lambda x,y: x+y)
random_sub_vector = alu_gen_random(0x2, lambda x,y: x-y)
random_and_vector = alu_gen_random(0x3, lambda x,y: x&y)
random_or_vector  = alu_gen_random(0x4, lambda x,y: x|y)
random_LT_vector  = alu_gen_random(0x5, lambda x,y: x<y)
random_ET_vector  = alu_gen_random(0x6, lambda x,y: x==y)


def test_add_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_add_vector, dump_vcd)


def test_add_random(dump_vcd):
   run_test_vector_sim( ALU(16), random_add_vector, dump_vcd )


def test_sub_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_sub_vector, dump_vcd)


def test_sub_random( dump_vcd ):
   run_test_vector_sim( ALU(16), random_sub_vector, dump_vcd )


def test_and_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_and_vector, dump_vcd)


def test_and_random( dump_vcd ):
   run_test_vector_sim( ALU(16), random_and_vector, dump_vcd )


def test_or_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_or_vector, dump_vcd)


def test_or_random( dump_vcd ):
   run_test_vector_sim( ALU(16), random_or_vector, dump_vcd )


def test_less_than_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_LT_vector, dump_vcd)


def test_less_than_random( dump_vcd ):
   run_test_vector_sim( ALU(16), random_LT_vector, dump_vcd )


def test_equal_fixed( dump_vcd ):
   run_test_vector_sim( ALU( 16 ), fixed_ET_vector, dump_vcd)


def test_equal_random( dump_vcd ):
   run_test_vector_sim( ALU(16), random_ET_vector, dump_vcd )


def test_invalid_operation( dump_vcd ):
   print "Testing invalid input"
   f = lambda x,y: 0
   test_vector_table = alu_gen_random( 0x7, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


