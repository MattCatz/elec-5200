module Datapath
(input clock,
 input reset,
 input regfile_w,
 input [2:0] rX_address,rY_address,rZ_address,
 input alu_func_t alu_s,
 input data_s_t data_s,
 input operand_s_t operand_s,
 input pc_s_t pc_s,
 input [15:0] word_r,
 input [7:0] immediate,
 output [11:0] pc,
 output [15:0] word_w,
 output [9:0] word_a);

import constants::data_s_t;

import constants::DATA_ALU;
import constants::DATA_WORD;
import constants::DATA_PC;

logic [15:0] rX, rY, rZ;
logic [15:0] alu_out;

reg [11:0] program_counter;
assign pc = program_counter;

// Begin Program Counter Stuff

//logic [15:0] pc_mux [1:0];

//assign pc_mux[PC_ALU] = alu_out;
//assign pc_mux[PC_ADD] = program_counter + immediate;
//assign pc_mux[PC_INC] = program_counter + 1;

always_comb begin
    unique case (pc_s)
        PC_ADD: program_counter = program_counter + immediate;
        PC_INC: program_counter = program_counter + 1;
    endcase;
end

// Begin Register File stuff
//logic [15:0] data_mux [2:0];

//assign data_mux[0] = alu_out;
//assign data_mux[1] = word_r;
//assign data_mux[2] = program_counter;

always_comb begin
    unique case (data_s)
        DATA_ALU: rZ = alu_out;
        DATA_WORD: rZ = word_r;
        DATA_PC: rZ = program_counter;
        DATA_NOP: rZ = 16'd0;
    endcase
end

assign word_w = rY;

regfile GPR (
 .clock(clock),
 .we(regfile_w),
 .reset(reset),
 .rX_address(rX_address),  
 .rX(rX),
 .rY_address(rY_address), 
 .rY(rY),
 .rZ_address(rZ_address), 
 .rZ(rZ));
  
// Begin ALU stuff
logic [15:0] operand_mux [2:0];

assign operand_mux[0] = rY;
assign operand_mux[1] = immediate;
assign operand_mux[2] = immediate << 8;

assign word_a = alu_out;

alu ALU  ( 
 .A(rX),
 .B(operand_mux[operand_s]),               
 .sel(alu_s),
 .out(alu_out));

endmodule