module mux_2
#( length = 16 )
( input  [length-1:0] A,B,
  input  sel,
  output [length-1:0] out);

assign out = sel ? A : B;

endmodule

module mux_4
#( length = 16 )
( input  [length-1:0] A,B,C,D,
  input  [1:0] sel,
  output reg [length-1:0] out);

always @(*)
begin
  case (sel)
    0 : out <= A;
    1 : out <= B;
    2 : out <= C;
    default : out <= D;
  endcase
end
endmodule

module mux
#(length = 16, width = 16)
(input  logic [length-1:0] ports [width-1:0],
 input  logic [3:0] sel,
 output logic [length-1:0] out);

assign out = ports[sel];

endmodule