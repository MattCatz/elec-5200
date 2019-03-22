module Control_Unit 
(input operation,
 input funct,
 output pc_s,
 output operand_s,
 output reg alu_s,
 output data_s);

always_comb begin
    case (operation)
        0: //Add
            assign alu_s = 1;
        1: //Subtraction
            assign alu_s = 2;
        2: //Logical and 
            assign alu_s = 3;
        3: //Logical or
            assign alu_s = 4;
        4: //Set Less than
            assign alu_s = 3;
        8: //Load Word
            assign alu_s = 4;
        default:
            assign alu_s = 0;
        endcase
end

endmodule