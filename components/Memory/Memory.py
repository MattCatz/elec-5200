from pymtl import *

class Memory (VerilogModel):
   def __init__(s, dtype=16, lines=1024):
      addr_len = clog2(lines)

      s.clk_en = InPort(1)
      s.write_A = InPort(1)
      s.write_B = InPort(1)

      s.Address_A = InPort(addr_len)
      s.Address_B = InPort(addr_len)

      s.Data_A = InPort(dtype)
      s.Data_B = InPort(dtype)

      s.Out_A = OutPort(dtype)
      s.Out_B = OutPort(dtype)

      s.set_params({
         "dtype"   : dtype,
         "lines"   : lines,
         "addr_len": addr_len
      })

      s.set_ports({
         "clock"    : s.clk,
         "clk_en"   : s.clk_en,
         "write_A"  : s.write_A,
         "write_B"  : s.write_B,
         "Address_A": s.Address_A,
         "Address_B": s.Address_B,
         "Data_A"   : s.Data_A,
         "Data_B"   : s.Data_B,
         "Out_A"    : s.Out_A,
         "Out_B"    : s.Out_B
      })
