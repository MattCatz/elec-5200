`include "Constants.sv"
import constants::alu_func_t;

module alu
#(parameter length = 16)
 ( input [length-1:0] A,B,               
   input alu_func_t sel,
   output [length-1:0] out);
  
   import constants::ALU_ADD;
   import constants::ALU_SUB;
   import constants::ALU_AND;
   import constants::ALU_OR;
   import constants::ALU_GT;
   import constants::ALU_ET;
   import constants::ALU_NOP;
   
   reg [length-1:0] result;

   assign out = result;

   always_comb begin
      case(sel)
         ALU_ADD: // Addition
            result = A + B ; 
         ALU_SUB: // Subtraction
            result = A - B ;
         ALU_AND: //  Logical and 
            result = A & B;
         ALU_OR: //  Logical or
            result = A | B;
         ALU_GT: // Greater comparison
            result = (A<B)? 1 : 0;
         ALU_ET: // Equal comparison   
            result = (A==B)? 1 : 0;
         default: result = 0 ; 
      endcase
   end

endmodule
