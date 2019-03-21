from pymtl import *

class Reg( Model ):

   def __init__(s, dtype=Bits(16)):

      s.in_ = InPort( dtype )
      s.w_en = InPort( dtype )
      s.out = OutPort( dtype )

      @s.tick
      def logic():
         if s.reset:
            s.out.next = 0
         elif s.w_en:
            s.out.next = s.in_
         else:
            s.out.next = s.out


   def line_trace( s ):
      return "In: {} W_EN: {} Out: {}".format(s.in_,s.w_en,s.out)


class Shifter( Model ):

   def __init__(s, dtype=Bits(16), amount=8):
      s.in_ = InPort( dtype )
      s.out = OutPort( dtype )

      @s.combinational
      def logic():
         s.out.value = s.in_ << amount


   def line_trace( s ):
      return "In: {} Out: {}".format(s.in_,s.out)
