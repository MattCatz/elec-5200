`ifndef CPU_CONSTANTS
`define CPU_CONSTANTS
package constants;

typedef enum logic [1:0] {
    OP_RR = 2'b00,
    OP_RI = 2'b01,
    OP_JP = 2'b10,
    OP_BR = 2'b11
} isa_op;

typedef enum logic [2:0] {
    RR_ADD = 3'b000,
    RR_SUB = 3'b001,
    RR_AND = 3'b010,
    RR_OR = 3'b011,
    RR_SLT = 3'b100
} rr_type;

typedef enum logic [2:0] {
    RI_ADDI = 3'b000,
    RI_LOAD = 3'b001,
    RI_STOR = 3'b010,
    RI_LUI = 3'b011
} ri_type;

typedef enum logic [2:0] {
   ALU_NOP = 3'b000,
   ALU_ADD = 3'b001,
   ALU_SUB = 3'b010,
   ALU_AND = 3'b011,
   ALU_OR  = 3'b100,
   ALU_GT  = 3'b101,
   ALU_ET  = 3'b110
} alu_func_t;

typedef enum logic [3:0] {
    DATA_ALU  = 4'b0001,
    DATA_WORD = 4'b0010,
    DATA_PC   = 4'b0100,
    DATA_NOP  = 4'b1000
} data_s_t;

typedef enum logic {
    PC_INC = 1'b0,
    PC_ADD = 1'b1
} pc_s_t;

typedef enum logic [1:0] {
    OPERAND_RY = 2'b00,
    OPERAND_KK = 2'b01,
    OPERAND_SHIFTED = 2'b10,
    OPERAND_NOP = 2'b11
} operand_s_t;

typedef enum logic [4:0] {
    ISA_ADD = {OP_RR, RR_ADD},
    ISA_SUB = {OP_RR, RR_SUB},
    ISA_AND = {OP_RR, RR_AND},
    ISA_OR  = {OP_RR, RR_OR},
    ISA_SLT = {OP_RR, RR_SLT},
    ISA_ADDI = {OP_RI, RI_ADDI},
    ISA_LOAD = {OP_RI, RI_LOAD},
    ISA_STOR = {OP_RI, RI_STOR},
    ISA_LUI = {OP_RI, RI_LUI},
    ISA_JAL = {OP_JP, 3'b???},
    ISA_BEQ = {OP_BR, 3'b???}
} isa_t;

endpackage
`endif
