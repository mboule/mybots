import numpy

# Back Leg stuff
BackLegAmplitude = numpy.pi/4
BackLegFrequency = 20
BackLegPhaseOffset = 0

# Front Leg stuff
FrontLegAmplitude = numpy.pi/4
FrontLegFrequency = 8
FrontLegPhaseOffset = numpy.pi/2

# Max Force of legs
maxForce = 25

# Gravity
gravity = -9.8

# Refactoring stuff
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)