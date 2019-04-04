module regfile
#(parameter dtype = 16,
            nregs = 8,
            addr_len = $clog2(nregs))
(input clock,
 input clk_en,
 input reset,
 input [addr_len-1:0] rX_address,  
 output [dtype-1:0] rX,
 input [addr_len-1:0] rY_address, 
 output [dtype-1:0] rY,
 input [addr_len-1:0] rZ_address, 
 input [dtype-1:0] rZ);

// Register file storage
logic [dtype-1:0] registers [nregs-1:0];

// Read and write from register file
always_ff @(posedge clock)
        if (clk_en) registers[rZ_address] <= |rZ_address ? rZ : 0;

assign rX = registers[rX_address];
assign rY = registers[rY_address];
endmodule
