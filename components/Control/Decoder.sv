module Decoder(
    input  logic [15:0] word,
    output logic [1:0] opcode,
    output logic [2:0] rX, rY, rZ,
    output logic [2:0] func,
    output logic [7:0] kk);
    
    assign opcode = word[1:0];
    
    assign rX = word[10:8];
    assign rY = word[13:11];
    assign rZ = word[4:2];
    
    assign func = word[7:5];
    
    always_comb begin
        case (opcode)
            1: kk = word[15:11];
            2: kk = {word[15:11], word[7:5] };
            3: kk = {word[15:14], word[7:2] };
            default: kk = 0;
        endcase
    end
endmodule

