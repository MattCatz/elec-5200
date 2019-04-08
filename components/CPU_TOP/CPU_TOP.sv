`include "Constants.sv"

module CPU_TOP(
input clock,
input reset,
input logic [2:0] inr,
input debug,
input logic [15:0] instruction,
input logic [15:0] memory_fetch,
output logic [9:0] pc,
output logic [9:0] memory_address,
output logic [15:0] outvalue
);

import constants::data_s_t;
import constants::alu_func_t;
import constants::pc_s_t;
import constants::operand_s_t;

logic [1:0] operation;
logic [2:0] funct;
pc_s_t pc_s;
operand_s_t operand_s;
logic data_w;
alu_func_t alu_s;
data_s_t data_s;

logic clk_en;
logic [2:0] rX_address,rY_address,rZ_address;
logic [2:0] alu_ctr;
logic [10:0] immediate;

logic [2:0] debug_mux [1:0];

assign debug_mux[0] = rX_address;
assign debug_mux[1] = inr;

assign clk_en = 1'b1;

Decoder decoder (
    .word(instruction),
    .opcode(operation),
    .rX(rX_address),
    .rY(rY_address),
    .rZ(rZ_address),
    .func(funct),
    .kk(immediate));

ControlUnit control_Unit (
    .operation(operation),
    .funct(funct),
    .pc_s(pc_s),
    .operand_s(operand_s),
    .alu_s(alu_s),
    .data_s(data_s),
    .data_w(data_w));
 
Datapath data_Path (
   .clk(clock),
   .reset(reset),
   .regfile_w(clk_en),
   .rX_address(debug_mux[debug]),
   .rY_address(rY_address),
   .rZ_address(rZ_address),
   .alu_s(alu_s),
   .data_s(data_s),
   .operand_s(operand_s),
   .pc_s(pc_s),
   .word_r(memory_fetch),
   .immediate(immediate),
   .pc(pc),
   .word_w(outvalue),
   .word_a(memory_address));
endmodule
