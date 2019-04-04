`include "Constants"

import constants::data_s_t;

import constants::DATA_ALU;
import constants::DATA_WORD;
import constants::DATA_PC;

module Datapath
(input clock,
 input reset,
 input clk_en,
 input [2:0] rX_address,rY_address,rZ_address,
 input [2:0] alu_ctr,
 input data_s_t data_s,
 input [2:0] operand_s,
 input [2:0] pc_s,
 input [15:0] word_r,
 input [5:0] immediate,
 output [11:0] pc);

logic [15:0] rX, rY, rZ;
logic [15:0] alu_out;

reg [11:0] program_counter;
assign pc = program_counter;

// Begin Program Counter Stuff

logic [15:0] pc_mux [2:0];

assign pc_mux[0] = alu_out;
assign pc_mux[1] = program_counter + immediate;
assign pc_mux[2] = program_counter + 1;

always_latch begin
    program_counter = pc_mux[pc_s];
end

// Begin Register File stuff
logic [15:0] data_mux [2:0];

assign data_mux[0] = alu_out;
assign data_mux[1] = word_r;
assign data_mux[2] = program_counter;

regfile GPR (
 .clock(clock),
 .clk_en(clk_en),
 .reset(reset),
 .rX_address(rX_address),  
 .rX(rX),
 .rY_address(rY_address), 
 .rY(rY),
 .rZ_address(rZ_address), 
 .rZ(data_mux[data_s]));
  
// Begin ALU stuff
logic [15:0] operand_mux [2:0];

assign operand_mux[0] = rY;
assign operand_mux[1] = immediate;
assign operand_mux[2] = immediate << 8;

alu ALU  ( 
 .A(rX),
 .B(operand_mux[operand_s]),               
 .sel(alu_ctr),
 .out(alu_out));

endmodule
