# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import numpy
# import time
# import pybullet_data
# import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()












# # Creating movement
#
# BackLegAmplitude = c.BackLegAmplitude
# BackLegFrequency = c.BackLegFrequency
# BackLegPhaseOffset = c.BackLegPhaseOffset
# BackLegTargetAngles = BackLegAmplitude * numpy.sin(BackLegFrequency * numpy.linspace(-numpy.pi + BackLegPhaseOffset, numpy.pi + BackLegPhaseOffset, 1000))
# numpy.save('data/BackLegTargetAngles', BackLegTargetAngles)
#
# FrontLegAmplitude = c.FrontLegAmplitude
# FrontLegFrequency = c.FrontLegFrequency
# FrontLegPhaseOffset = c.FrontLegPhaseOffset
# FrontLegTargetAngles = FrontLegAmplitude * numpy.sin(FrontLegFrequency * numpy.linspace(-numpy.pi + FrontLegPhaseOffset, numpy.pi + FrontLegPhaseOffset, 1000))
# numpy.save('data/FrontLegTargetAngles', FrontLegTargetAngles)
#
#
#
#
#
#
#
#
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)
#
#
# # Simulation loop
#
# for i in range(1000):
#     p.stepSimulation()
#     time.sleep(1/240)
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#
#         bodyIndex = robot,
#
#         jointName = "BackLeg_Torso",
#
#         controlMode = p.POSITION_CONTROL,
#
#         targetPosition = BackLegTargetAngles[i],
#
#         maxForce = c.maxForce)
#     pyrosim.Set_Motor_For_Joint(
#
#         bodyIndex = robot,
#
#         jointName = "FrontLeg_Torso",
#
#         controlMode = p.POSITION_CONTROL,
#
#         targetPosition = -FrontLegTargetAngles[i],
#
#         maxForce = c.maxForce)
#
#
# p.disconnect()
# numpy.save('data/backLegSensorValues', backLegSensorValues)
# numpy.save('data/frontLegSensorValues', frontLegSensorValues)
