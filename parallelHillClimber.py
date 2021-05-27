from solution import SOLUTION
import constants as c
import copy
import os
import numpy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm fitness**.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)


    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.SaveFitnessValues(currentGeneration)

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n")
        for i in self.parents:
            print("Parent: " + str(self.parents[i].fitness) + ", Child: " + str(self.children[i].fitness))
        print("\n")

    def Show_Best(self):
        best = self.parents[0].fitness
        best_key = 0
        for key in self.parents:
            if self.parents[key].fitness < best:
                best = self.parents[key].fitness
                best_key = key
        self.parents[best_key].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in self.parents:
            solutions[i].Start_Simulation("DIRECT")
        for i in self.parents:
            solutions[i].Wait_For_Simulation_To_End()

    def SaveFitnessValues(self, generation):
        for key in self.parents:
            self.fitnessValues[key][generation] = self.parents[key].fitness

    def SaveToFile(self):
        # SAVING FITNESS VALUES TO FitnessValues.npy
        # np.save(os.path.join('data', 'FitnessValuesA.npy'), self.fitnessValues)
        numpy.save(os.path.join('data', 'FitnessValuesB.npy'), self.fitnessValues)