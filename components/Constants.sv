package constants;

typedef enum logic [3:0] {
    ISA_ADD,
    ISA_SUB,
    ISA_AND,
    ISA_OR,
    ISA_SLT,
    ISA_JAL,
    ISA_BEQ,
    ISA_LOAD,
    ISA_STOR,
    ISA_ADDI,
    ISA_LUI
} isa_op;

typedef enum logic [2:0] {
   ALU_NOP,
   ALU_ADD,
   ALU_SUB,
   ALU_AND,
   ALU_OR,
   ALU_GT,
   ALU_ET
} alu_func_t;

typedef enum logic [1:0] {
    DATA_NOP,
    DATA_ALU,
    DATA_WORD,
    DATA_PC
} data_s_t;

endpackage
