import constants::data_s_t;
import constants::alu_func_t;

module CPU_TOP(
input clock,
input reset
);

logic [1:0] operation;
logic [2:0] funct;
logic [2:0] pc_s;
logic [2:0] operand_s;
alu_func_t alu_s;
data_s_t data_s;

logic clk_en;
logic [2:0] rX_address,rY_address,rZ_address;
logic [2:0] alu_ctr;
logic [15:0] word_r;
logic [5:0] immediate;
logic [11:0] pc;

logic write_A, write_B;
logic [9:0] Address_A, Address_B;
logic [15:0] Data_A, Data_B;
logic [15:0] Out_A, Out_B;

assign Address_B = pc;
assign write_B = 0;

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
    .data_s(data_s));
 
Datapath data_Path (
   .clock(clock),
   .reset(reset),
   .clk_en(clk_en),
   .rX_address(rX_address),
   .rY_address(rY_address),
   .rZ_address(rZ_address),
   .alu_ctr(alu_s),
   .data_s(data_s),
   .operand_s(operand_s),
   .pc_s(pc_s),
   .word_r(word_r),
   .immediate(immediate),
   .pc(pc));
   
Memory external_mem (
    .clock(clock), 
    .clk_en(clk_en),
    .write_A(write_A),
    .write_B(write_B),
    .Address_A(Address_A),
    .Address_B(Address_B),
    .Data_A(Data_A),
    .Data_B(Data_B),
    .Out_A(Out_A),
    .Out_B(Out_B));

endmodule

