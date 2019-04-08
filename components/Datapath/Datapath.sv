`include "Constants.sv"
import constants::alu_func_t;
import constants::data_s_t;
import constants::operand_s_t;
import constants::pc_s_t;

module Datapath
(input clk,
 input reset,
 input regfile_w,
 input [2:0] rX_address,rY_address,rZ_address,
 input alu_func_t alu_s,
 input data_s_t data_s,
 input operand_s_t operand_s,
 input pc_s_t pc_s,
 input [15:0] word_r,
 input [10:0] immediate,
 output [9:0] pc,
 output [15:0] word_w,
 output [9:0] word_a);

import constants::DATA_ALU;
import constants::DATA_WORD;
import constants::DATA_PC;
import constants::DATA_NOP;

import constants::PC_ADD;
import constants::PC_INC;

logic [15:0] rX, rY, rZ;
logic [15:0] alu_out;

reg [9:0] program_counter, next_pc;
assign pc = program_counter;
 
always_ff@(posedge clk) begin
   program_counter <= next_pc;
end
 
always_comb begin
    unique case (pc_s)
        PC_ADD: next_pc = program_counter + 10'(immediate);
        PC_INC: next_pc = program_counter + 10'b1;
    endcase;
end


always_comb begin
    unique case (data_s)
        DATA_ALU: rZ = alu_out;
        DATA_WORD: rZ = word_r;
        DATA_PC: rZ = 16'(program_counter);
        DATA_NOP: rZ = 16'd0;
	default: rZ = 16'bX;
    endcase
end

assign word_w = rY;

regfile GPR (
 .clock(clk),
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
assign operand_mux[1] = 16'(immediate);
assign operand_mux[2] = 16'({immediate, 8'b0});

assign word_a = 10'(alu_out);

alu ALU  ( 
 .A(rX),
 .B(operand_mux[operand_s]),               
 .sel(alu_s),
 .out(alu_out));

endmodule
