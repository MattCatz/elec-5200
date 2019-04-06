`include "Constants.sv"

module CPU_TOP(
input clock,
input reset,
input logic [2:0] inr,
input debug,
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
logic [7:0] immediate;
logic [11:0] pc;

logic write_B;
logic [9:0] Address_A, Address_B;
logic [15:0] Data_A, Data_B;
logic [15:0] Out_A, Out_B;

logic [2:0] debug_mux [1:0];

assign Address_B = pc;
assign write_B = 0;
assign Data_B = 0;

assign debug_mux[0] = rX_address;
assign debug_mux[1] = inr;

assign outvalue = Data_A;

assign clk_en = 1'b1;

Decoder decoder (
    .word(Out_B),
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
   .word_r(Out_A),
   .immediate(immediate),
   .pc(pc),
   .word_w(Data_A),
   .word_a(Address_A));
   
Memory external_mem (
    .clock(clock), 
    .clk_en(clk_en),
    .write_A(data_w),
    .write_B(write_B),
    .Address_A(Address_A),
    .Address_B(Address_B),
    .Data_A(Data_A),
    .Data_B(Data_B),
    .Out_A(Out_A),
    .Out_B(Out_B));

endmodule
