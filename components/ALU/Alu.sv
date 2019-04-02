typedef enum logic [5:0] {
   ALU_ADD,
   ALU_SUB,
   ALU_AND,
   ALU_OR,
   ALU_GT,
   ALU_ET
} alu_func_t;

module alu
#(parameter length = 16)
 ( input [length-1:0] A,B,
   input [2:0] sel,
   output [length-1:0] out);
  
   reg [length-1:0] result;

   assign out = result;

   always_comb begin
      case(sel)
         1: // Addition
            result = A + B ; 
         2: // Subtraction
            result = A - B ;
         3: //  Logical and 
            result = A & B;
         4: //  Logical or
            result = A | B;
         5: // Greater comparison
            result = (A>B)? 1 : 0;
         6: // Equal comparison   
            result = (A==B)? 1 : 0;
         default: result = 0 ; 
      endcase
   end

endmodule
