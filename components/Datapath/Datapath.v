module Datapath
(input clock,
 input reset,
 input rX_address,rY_address,rZ_address,
 input alu_ctr,
 input data_s,
 input word_r);

wire clk_en;
wire rX, rY, rZ;
wire B, alu_out;
wire immediate,shifted_immediate;

reg program_counter;

mux_4 data_mux ( 
   .A(alu_out),
   .B(word_r),
   .C(program_counter),
   .D(0),
   .sel(data_s),
   .out(rZ)); 

regfile GPR (
 .clock(clock),
 .clk_en(clk_en),
 .reset(reset),
 .rX_address(rX_address),  
 .rX(rX),
 .rY_address(rY_address), 
 .rY(rY),
 .rZ_address(rZ_address), 
 .rZ(rZ));
 
mux_4 operand_mux ( 
  .A(rY),
  .B(immediate),
  .C(shifted_immediate),
  .D(0),
  .sel(alu_ctr),
  .out(B)); 

alu ALU  ( 
 .A(rX),
 .B(B),               
 .sel(alu_ctr),
 .out(rZ));

endmodule