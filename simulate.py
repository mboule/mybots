import sys
from simulation import SIMULATION

directOrGui = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGui, solutionID)
simulation.run()
simulation.Get_Fitness()
