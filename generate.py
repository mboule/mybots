import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5


def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x-2, y-1, z], size=[length, width, height])
    pyrosim.End()


def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint( name = "FrontLeg_Torso" , parent= "FrontLeg" , child = "Torso" , type = "revolute", position = ".5 0 1")
    pyrosim.Send_Cube(name="Torso", pos=[x+.5, y, z], size=[length, width, height])
    pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[x+.5, y, z-1], size=[length, width, height])
    pyrosim.End()


create_world()
create_robot()
