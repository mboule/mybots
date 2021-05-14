import sys
from simulation import SIMULATION

directOrGui = sys.argv[1]

simulation = SIMULATION(directOrGui)
simulation.run()
simulation.Get_Fitness()
