from pymtl import *
from RegFile import RegFile

input_values = range(0, 255, 16)

#input_values.extend( [0]*3)

model = RegFile( dtype = 16, nregs = 16 )
model.elaborate()

sim = SimulationTool( model )

sim.reset()

for idx,val in enumerate(input_values):
	model.rZ_address = idx
	model.rZ = val
	sim.cycle()
	sim.print_line_trace()

model.rZ_address = 0

for idx,_ in enumerate(input_values):
	model.rX_address.value = idx
	model.rY_address.value = idx
	sim.cycle()
	sim.print_line_trace()
