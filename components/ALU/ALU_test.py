import random
import pytest


from pymtl import *
from pclib.test import run_test_vector_sim
from ALU import ALU

def alu_gen_random( o, f ):
   test_vector_table=[('op1 op2 operation result*')]
   last_result = 0x0
   for i in xrange(40):
      rand_1 = Bits(16, random.randint( -0x8000,0x7FFF ))
      rand_2 = Bits(16, random.randint( -0x8000,0x7FFF ))
      test_vector_table.append( [rand_1, rand_2, o, last_result] )
      last_result = Bits( 16, f( rand_1, rand_2 ))
   return test_vector_table

   

def test_add_fixed( dump_vcd ):
   print "Testing Add with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x1,     0x0],
   [ 0x3,    0x4,      0x1,     0x2],
   [ 0xFF00, 0x00FF,   0x1,     0x7],
   [ 0x2,    0xFFFE,   0x1,     0xFFFF],
   [ 0x2,    0xFFFF,   0x1,     0x0],
   [ 0x0,    0x0,      0x1,     0x1],
   ] , dump_vcd)


def test_add_random(dump_vcd):
   print "Testing Add with random imput"
   f = lambda x,y: x+y
   test_vector_table = alu_gen_random(0x1,f)
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_sub_fixed( dump_vcd ):
   print "Testing Subtract with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x2,     0x0],
   [ 0x3,    0x4,      0x2,     0x0],
   [ 0xFF00, 0x00FF,   0x2,     0xFFFF],
   [ 0x2,    0xFFFE,   0x2,     0xFE01],
   [ 0x0,    0x0,      0x2,     0x4],
   ] , dump_vcd)


def test_sub_random( dump_vcd ):
   print "Testing Subtract with random imput"
   f = lambda x,y: x-y
   test_vector_table = alu_gen_random( 0x2, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_and_fixed( dump_vcd ):
   print "Testing And with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x3,     0x0],
   [ 0x3,    0x4,      0x3,     0x1],
   [ 0xFF00, 0x00FF,   0x3,     0x0],
   [ 0x2,    0xFFFE,   0x3,     0x0],
   [ 0xA,    0xA,      0x3,     0x2],
   [ 0x0,    0x0,      0x0,     0xA],
   ] , dump_vcd)


def test_and_random( dump_vcd ):
   print "Testing Logical And with random imput"
   f = lambda x,y: x & y
   test_vector_table = alu_gen_random( 0x3, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_or_fixed( dump_vcd ):
   print "Testing Or with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x4,     0x0],
   [ 0x3,    0x4,      0x4,     0x1],
   [ 0xFF00, 0x00FF,   0x4,     0x7],
   [ 0x2,    0xFFFE,   0x4,     0xFFFF],
   [ 0xA,    0x5,      0x4,     0xFFFE],
   [ 0x0,    0x0,      0x0,     0xF],
   ] , dump_vcd)


def test_or_random( dump_vcd ):
   print "Testing Logical Or with random imput"
   f = lambda x,y: x | y
   test_vector_table = alu_gen_random( 0x4, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_less_than_fixed( dump_vcd ):
   print "Testing Less than with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x5,     0x0],
   [ 0x3,    0x4,      0x5,     0x0],
   [ 0xFF00, 0x00FF,   0x5,     0x1],
   [ 0x2,    0xFFFE,   0x5,     0x0],
   [ 0xA,    0x5,      0x5,     0x1],
   [ 0x0,    0x0,      0x0,     0x0],
   ] , dump_vcd)


def test_less_than_random( dump_vcd ):
   print "Testing Less Than with random imput"
   f = lambda x,y: x<y
   test_vector_table = alu_gen_random( 0x5, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_equal_fixed( dump_vcd ):
   print "Testing Equals with fixed imput"
   run_test_vector_sim( ALU( 16 ), [ 
   ('op1     op2 operation result*'),
   [ 0x1,    0x1,      0x6,     0x0],
   [ 0x3,    0x4,      0x6,     0x1],
   [ 0xFF00, 0x00FF,   0x6,     0x0],
   [ 0x2,    0xFFFE,   0x6,     0x0],
   [ 0xA,    0xA,      0x6,     0x0],
   [ 0x0,    0x0,      0x0,     0x1],
   ] , dump_vcd)


def test_equal_random( dump_vcd ):
   print "Testing Equivalence with random imput"
   f = lambda x,y: x == y
   test_vector_table = alu_gen_random( 0x6, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


def test_invalid_operation( dump_vcd ):
   print "Testing invalid input"
   f = lambda x,y: 0
   test_vector_table = alu_gen_random( 0x7, f )
   run_test_vector_sim( ALU(16), test_vector_table, dump_vcd )


