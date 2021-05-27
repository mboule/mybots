import numpy

# Back Leg
BackLegAmplitude = numpy.pi/6
BackLegFrequency = 1/25
BackLegPhaseOffset = numpy.pi/4

# Front Leg
FrontLegAmplitude = numpy.pi/3
FrontLegFrequency = 1/25
FrontLegPhaseOffset = 0

# Max Force of legs
maxForce = 500

# Gravity
gravity = -9.8

# Refactoring stuff
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)

# For Evolve()
numberOfGenerations = 5

# For Parallel Hill Climber
populationSize = 20

# For Quadruped
numSensorNeurons = 6
numMotorNeurons = 8
motorJointRange = 0.6
