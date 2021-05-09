import constants as c
import pyrosim.pyrosim
import pybullet as p
import numpy as np


class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(1000)
        self.Prepare_To_Act()



    def Prepare_To_Act(self):
        self.amplitude = c.backAmplitude
        self.frequency = c.backFrequency
        self.offset = c.backPhaseOffset

        for i in range(1000):
            if self.jointName == "FrontLeg":
                self.motorValues[i] = self.amplitude * np.sin(self.frequency * c.x[i] + self.offset)
            elif self.jointName == "BackLeg":
                self.motorValues[i] = self.amplitude * np.sin(0.5*self.frequency * c.x[i] + self.offset)


    def Set_Value(self, robot, time):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[time],
            maxForce = c.maxForce)

def Save_Values(self):
    np.save('data/motorValues.npy', self.motorValues)