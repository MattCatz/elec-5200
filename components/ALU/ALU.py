from pymtl import *

class ALU( Model ):

   def __init__( s, width=16 ):
      s.op1 = InPort ( Bits(width) )
      s.op2 = InPort ( Bits(width) )
      s.result = OutPort ( Bits(width) )
      s.operation = InPort ( Bits(3) )

      @s.combinational
      def block2():
         if s.operation == 1: # Addition
            s.result.value = s.op1 + s.op2
         elif s.operation == 2: # Subtraction
            s.result.value = s.op1 - s.op2
         elif s.operation == 3: # Logic And
            s.result.value = s.op1 & s.op2
         elif s.operation == 4: # Logic Or
            s.result.value = s.op1 | s.op2
         elif s.operation == 5: # Less than
            s.result.value = s.op1 < s.op2
         elif s.operation == 6: # Equal
            s.result.value = s.op1 == s.op2
         else:
            s.result.value = Bits(width, 0)


   def line_trace( s ):
      return "OP1:{} OP2:{} Operation:{}, Result:{}".format( s.op1, s.op2, s.operation, s.result)



class alu( VerilogModel ):

   def __init__( s, width=16 ):
      s.op1 = InPort ( Bits(width) )
      s.op2 = InPort ( Bits(width) )
      s.result = OutPort ( Bits(width) )
      s.operation = InPort ( Bits(3) )

      s.set_params({
         "width"    : width,
      })

      s.set_ports({
         'clock'       : s.clk,
         'A'           : s.op1,
         'B'           : s.op2,
         'sel'         : s.operation,
         'result'      : s.result
      })
