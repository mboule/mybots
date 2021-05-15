import numpy

# Back Leg stuff
BackLegAmplitude = numpy.pi/8
BackLegFrequency = 10
BackLegPhaseOffset = 0

# Front Leg stuff
FrontLegAmplitude = numpy.pi
FrontLegFrequency = 60
FrontLegPhaseOffset = numpy.pi/2

# Max Force of legs
maxForce = 80

# Gravity
gravity = -9.8

# Refactoring stuff
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)

# For Evolve()
numberOfGenerations = 10

# For Parallel Hill Climber
populationSize = 10

# For Quadruped
numSensorNeurons = 6
numMotorNeurons = 8
motorJointRange = 0.7
