import random
import pytest

from pymtl import *
from pclib.test import run_test_vector_sim
from ALU import alu as ALU_SV

from ALU_test import (fixed_add_vector, random_add_vector)
from ALU_test import (fixed_sub_vector, random_sub_vector)
from ALU_test import (fixed_and_vector, random_and_vector)
from ALU_test import (fixed_or_vector, random_or_vector)
from ALU_test import (fixed_LT_vector, random_LT_vector)
from ALU_test import (fixed_ET_vector, random_ET_vector)

def test_add_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_add_vector , dump_vcd)


def test_add_random(dump_vcd):
   run_test_vector_sim( ALU_SV(16), random_add_vector, dump_vcd )


def test_sub_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_sub_vector , dump_vcd)


def test_sub_random( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


def test_and_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_and_vector , dump_vcd)


def test_and_random( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


def test_or_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_or_vector , dump_vcd)


def test_or_random( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


def test_less_than_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_LT_vector , dump_vcd)


def test_less_than_random( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


def test_equal_fixed( dump_vcd ):
   run_test_vector_sim( ALU_SV( 16 ), fixed_ET_vector , dump_vcd)


def test_equal_random( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


def test_invalid_operation( dump_vcd ):
   run_test_vector_sim( ALU_SV(16), test_vector_table, dump_vcd )


