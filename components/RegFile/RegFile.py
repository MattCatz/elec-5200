import os
import inspect

from pymtl import *
 
class RegFile( Model ):
 
   def __init__( s, dtype = Bits(16), nregs=16 ):
      addr_len = clog2( nregs )

      s.rX_address = InPort ( Bits(addr_len) )
      s.rY_address = InPort ( Bits(addr_len) )
      s.rZ_address = InPort ( Bits(addr_len) )
 
      s.rX = OutPort ( dtype )
      s.rY = OutPort ( dtype )

      s.rZ = InPort ( dtype )

      s.clk_en = InPort (1)

      s.regs = [ Wire( dtype ) for _ in range(nregs) ]

      @s.posedge_clk
      def write():
         if s.clk_en and s.rZ_address != 0:
            s.regs[s.rZ_address].next = s.rZ
   
      @s.combinational
      def read():
         s.rX.value = s.regs[s.rX_address]
         s.rY.value = s.regs[s.rY_address]
 
 
   def line_trace( s ):
      return [x.hex() for x in s.regs]



class regfile (VerilogModel):

   def __init__( s, dtype = 16, nregs = 8 ):
      addr_len = clog2( nregs )
      
      s.rX_address = InPort ( Bits(addr_len) )
      s.rY_address = InPort ( Bits(addr_len) )
      s.rZ_address = InPort ( Bits(addr_len) )

      s.rX = OutPort ( dtype )
      s.rY = OutPort ( dtype )

      s.rZ = InPort ( dtype )

      s.clk_en = InPort (1)

      s.regs = [ Wire( dtype ) for _ in range(nregs) ]
      
      s.set_params({
         "dtype"    : dtype,
         "nregs"    : nregs,
         "addr_len" : addr_len
      })

      s.set_ports({
         'clock'       : s.clk,
         'clk_en'      : s.clk_en,
         'reset'       : s.reset,
         'rX_address'  : s.rX_address,
         'rY_address'  : s.rY_address,
         'rZ_address'  : s.rZ_address,
         'rX'          : s.rX,
         'rY'          : s.rY,
         'rZ'          : s.rZ,
      })

      @s.posedge_clk
      def write():
         if s.rZ_address != 0:
            s.regs[s.rZ_address].next = s.rZ


   def line_trace( s ):
      return ""#[x.hex() for x in s.regs]

