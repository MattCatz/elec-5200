from pymtl import *

class Reg( Model ):

	def __init__(s, dtype=Bits(16)):

		s.in_ = InPort( dtype )
		s.out = Outport( dtype )

		@s.posedge_tick
		def logic():
			s.out.next = in_


	def line_trace( s ):
		return ""


class Shifter( Model ):

	def __init__(s, dtype=Bits(16), amount=8):
		s.in_ = InPort( dtype )
		s.out = OutPort( dtype )

		@s.combinational
		def logic():
			s.out.value = s.in_ << amount


	def line_trace( s ):
		return ""
