from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import time


class SIMULATION:

    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        if self.directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def run(self):

        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGui == "GUI":
                time.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()






