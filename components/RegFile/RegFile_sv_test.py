import random

from pymtl import *
from pclib.test import run_test_vector_sim
from RegFile import regfile as RegFile_sv

from RegFile_test import (gen_data, gen_vector_table, static_test_vector)

def test_rw( dump_vcd ):
	run_test_vector_sim( RegFile_sv(dtype=16,nregs=16), static_test_vector, dump_vcd)
