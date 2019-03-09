from pymtl import *

class Mux( Model ):

	def __init__(s, dtype = Bits(16), nports=4):
		sel_len = clog2( nregs )

		s.sel = InPort( Bits(sel_len) )
		s.val = OutPort( dtype )
		s.ports = [ Wire(dtype) for _ in range(nports) ]

		@s.combinational
		def logic():
			assert s.sel < nports
			s.val.value = s.ports[ s.sel ]


	def line_trace( s ):
		return "Sel: {1} Val: {2}".format(s.sel, s.val)
			
