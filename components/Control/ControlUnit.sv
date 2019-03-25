import constants::alu_func_t;

import constants::*;
//import constants::ALU_SUB;
//import constants::ALU_AND;
//import constants::ALU_OR;
//import constants::ALU_GT;
//import constants::ALU_ET;
//import constants::ALU_NOP;

import constants::data_s_t;

import constants::DATA_ALU;
import constants::DATA_WORD;
import constants::DATA_PC;
import constants::DATA_NOP;

module ControlUnit 
(input  [1:0] operation,
 input  [2:0] funct,
 output [2:0] pc_s,
 output [2:0] operand_s,
 output alu_func_t alu_s,
 output data_s_t data_s);

always_comb begin // ALU control
    case (operation)
        ISA_SUB: alu_s = ALU_SUB;
        ISA_AND: alu_s = ALU_AND;
        ISA_OR:  alu_s = ALU_OR;
        ISA_SLT: alu_s = ALU_GT;
        ISA_BEQ: alu_s = ALU_ET;
        default:
            alu_s = ALU_ADD;
        endcase
end

always_comb begin // Data Control
    case (operation)
    0: data_s = DATA_ALU;
    default:
        data_s = DATA_NOP;
    endcase
end

endmodule
