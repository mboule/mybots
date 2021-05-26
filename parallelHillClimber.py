import solution
import constants as c
import os
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm fitness**.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0,c.populationSize):
            self.parents[i] = solution.SOLUTION(i)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
       # self.Show_Best()

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents.keys():
            if float(self.children[key].fitness < float(self.parents[key].fitness)):
                self.parents[key] = copy.deepcopy(self.children[key])

    def Print(self):
        print("\n")
        for key in self.parents.keys():
            print("Parent: " + str(self.parents[key].fitness) + ", Child: " + str(self.children[key].fitness))
        print("\n")

    def Show_Best(self):
        best = 1000
        best_key = 0
        for key in self.parents.keys():
            if float(self.parents[key].fitness) < float(best):
                best = self.parents[key].fitness
                best_key = key
        self.parents[best_key].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")
        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()