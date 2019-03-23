import random

from pymtl import *
from pclib.test import run_test_vector_sim
from RegFile import regfile as RegFile_sv

from RegFile_test import (gen_data, gen_vector_table, static_test_vector)

def test_rw( dump_vcd ):
	run_test_vector_sim( RegFile_sv(dtype=16,nregs=16), static_test_vector, dump_vcd)

def test_rw_sequential( dump_vcd ):
	data = gen_data(16,8)
	test_vector_table = gen_vector_table(data)
	run_test_vector_sim( RegFile_sv(dtype=16,nregs=8), test_vector_table, dump_vcd )
