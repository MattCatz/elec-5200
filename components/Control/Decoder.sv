module Decoder(
    input  logic [15:0] word,
    output logic [1:0] opcode,
    output logic [2:0] rX, rY, rZ,
    output logic [2:0] func,
    output logic [10:0] kk);
    
    assign opcode = word[1:0];
    
    assign rX = word[10:8];
    assign rY = word[13:11];
    assign rZ = word[4:2];
    
    assign func = word[7:5];
    
    always_comb begin
        unique case (opcode)
            1: kk = 11'(word[15:11]);
            2: kk = 11'(word[15:5]);
            3: kk = 11'({word[15:14], word[7:2] });
            default: kk = 11'0;
        endcase
    end
endmodule

