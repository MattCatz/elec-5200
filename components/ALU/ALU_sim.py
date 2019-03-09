from pymtl import *
from ALU import ALU

input_values = range(0, 255, 16)

input_values.extend( [0]*3 )

model = ALU(16)
model.elaborate()

sim = SimulationTool( model )

sim.reset()

for input_value in input_values:
	model.op1.value = input_value
	model.op2.value = input_value
	model.operation = 0

	sim.print_line_trace()

	sim.cycle()
