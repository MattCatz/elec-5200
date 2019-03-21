from pymtl import *

class PC_Adder( Model ):

   def __init__( s, width=16 ):
      s.op1 = InPort ( Bits(width) )
      s.op2 = InPort ( Bits(width) )
      s.result = OutPort ( Bits(width) )


      @s.combinational
      def block2():
         s.result.value = s.op1 + s.op2


   def line_trace( s ):
      op1 = "OP1:{} ".format( s.op1)
      op2 = "OP2:{} ".format( s.op2)
      result = "Result:{} ".format(s.result)
      return op1 + op2 + result
