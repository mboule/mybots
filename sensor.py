import numpy
import constants as c
import pyrosim.pyrosim

class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = numpy.zeros(1000)
        pass

    def Get_Value(self, time):
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if time == (c.numLoops-1):
            print(self.values)

    def Save_Values(self):
        numpy.save('data/sensorValues.npy', self.values)
