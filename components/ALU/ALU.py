from pymtl import *

class ALU( Model ):

   def __init__( s, width=16 ):
      s.op1 = InPort ( Bits(width) )
      s.op2 = InPort ( Bits(width) )
      s.result = OutPort ( Bits(width) )
      s.operation = InPort ( Bits(3) )

      s.reg_op1 = Wire( Bits(width) )
      s.reg_op2 = Wire( Bits(width) )
      s.reg_operation = Wire( Bits(3) )

      @s.tick
      def logic():
         s.reg_op1.next = s.op1
         s.reg_op2.next = s.op2
         if s.reset:
            s.reg_operation.next = 0
         else:
            s.reg_operation.next = s.operation



      @s.combinational
      def block2():
         if s.reg_operation == 1: # Addition
            s.result.value = s.reg_op1 + s.reg_op2
         elif s.reg_operation == 2: # Subtraction
            s.result.value = s.reg_op1 - s.reg_op2
         elif s.reg_operation == 3: # Logic And
            s.result.value = s.reg_op1 & s.reg_op2
         elif s.reg_operation == 4: # Logic Or
            s.result.value = s.reg_op1 | s.reg_op2
         elif s.reg_operation == 5: # Less than
            s.result.value = s.reg_op1 < s.reg_op2
         elif s.reg_operation == 6: # Equal
            s.result.value = reduce_xor(s.reg_op1, s.reg_op2)
         else:
            s.result.value = Bits(width, 0)


   def line_trace( s ):
      op1 = "OP1:{} ({}) ".format( s.op1, s.reg_op1 )
      op2 = "OP2:{} ({}) ".format( s.op2, s.reg_op2 )
      operation = "Operation:{} ({}) ".format( s.operation, s.reg_operation )
      result = "Result:{} ".format(s.result)
      return op1 + op2 + operation + result
