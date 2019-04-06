`include "Constants.sv"
import constants::alu_func_t;
import constants::data_s_t;
import constants::operand_s_t;
import constants::pc_s_t;

module ControlUnit 
(input  [1:0] operation,
 input  [2:0] funct,
 output pc_s_t pc_s,
 output operand_s_t operand_s,
 output alu_func_t alu_s,
 output data_s_t data_s,
 output logic data_w);

import constants::*;
 
logic [4:0] instruction;

assign instruction = {operation,funct};

assign data_w = ({operation,funct} ^ ISA_STOR) ? 0 : 1;

always_comb begin
    unique case (operation)
        OP_RR: pc_s = PC_INC;
        OP_RI: pc_s = PC_INC;
        OP_JP: pc_s = PC_ADD;
        OP_BR: pc_s = PC_ADD;
    endcase
 end
 
 always_comb begin
    unique case (operation)
        OP_RR: operand_s = OPERAND_RY;
        OP_RI: operand_s = OPERAND_KK;
        OP_BR: operand_s = OPERAND_RY;
        OP_JP: operand_s = OPERAND_NOP;
    endcase
 end
 
 always_comb begin
    unique case (operation)
        OP_RR: data_s = DATA_ALU;
        OP_RI: data_s = (funct ^ RI_LOAD) ? DATA_ALU : DATA_WORD;
        OP_JP: data_s = DATA_PC;
        OP_BR: data_s = DATA_PC;
        default: data_s = DATA_NOP;
    endcase
 end
 
always_comb begin
    unique casex (instruction)
        ISA_ADD: alu_s = ALU_ADD;
        ISA_SUB: alu_s = ALU_SUB;
        ISA_AND: alu_s = ALU_AND;
        ISA_OR: alu_s = ALU_OR;
        ISA_SLT: alu_s = ALU_GT;
        ISA_ADDI: alu_s = ALU_ADD;
        ISA_LOAD: alu_s = ALU_ADD;
        ISA_STOR: alu_s = ALU_ADD;
        ISA_LUI: alu_s = ALU_ADD;
        ISA_JAL: alu_s = ALU_ADD;
        ISA_BEQ: alu_s = ALU_ADD;
        default: alu_s = ALU_NOP;
    endcase
end

endmodule