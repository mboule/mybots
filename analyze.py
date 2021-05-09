import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
#
#
# matplotlib.pyplot.plot(backLegSensorValues, linewidth=4, label='Back')
# matplotlib.pyplot.plot(frontLegSensorValues, label='Front')
#
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

BackLegTargetAngles = numpy.load('data/BackLegTargetAngles.npy')
FrontLegTargetAngles = numpy.load('data/FrontLegTargetAngles.npy')
matplotlib.pyplot.plot(BackLegTargetAngles,  label = 'Back Leg')
matplotlib.pyplot.plot(FrontLegTargetAngles, label = 'Front Leg')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

