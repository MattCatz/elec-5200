import constants::alu_func_t;

import constants::ALU_ADD;
import constants::ALU_SUB;
import constants::ALU_AND;
import constants::ALU_OR;
import constants::ALU_GT;
import constants::ALU_ET;
import constants::ALU_NOP;

module alu
#(parameter length = 16)
 ( input [length-1:0] A,B,               
   input alu_func_t sel,
   output [length-1:0] out);
  
   reg [length-1:0] result;

   assign out = result;

   always_comb begin
      case(sel)
         constants::ALU_ADD: // Addition
            result = A + B ; 
         constants::ALU_SUB: // Subtraction
            result = A - B ;
         constants::ALU_AND: //  Logical and 
            result = A & B;
         constants::ALU_OR: //  Logical or
            result = A | B;
         constants::ALU_GT: // Greater comparison
            result = (A>B)? 1 : 0;
         constants::ALU_ET: // Equal comparison   
            result = (A==B)? 1 : 0;
         default: result = 0 ; 
      endcase
   end

endmodule
