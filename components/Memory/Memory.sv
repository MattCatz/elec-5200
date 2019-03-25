module Memory
#(parameter dtype = 16,
            lines = 1000,
            addr_len = $clog2(lines))
(input  logic clock, clk_en,
 input  logic write_A, write_B,
 input  logic [addr_len-1:0] Address_A, Address_B,
 input  logic [dtype-1:0] Data_A, Data_B,
 output logic [dtype-1:0] Out_A, Out_B);

reg [dtype-1:0] memory [lines-1:0];

assign Out_A = memory[Address_A];
assign Out_B = memory[Address_B];

always_ff @(posedge clock) begin
    if (write_A) begin
        memory[Address_A] <= Data_A;
    end
end

always @(posedge clock) begin
    if (write_B)
        memory[Address_B] <= Data_B;
end
endmodule
