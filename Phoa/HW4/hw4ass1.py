import numpy as np
import random

class PSO():
    def __init__(self, N, D, T):
        self.N = N  # Needed, Swarm size
        self.D = D  # Needed, Dimension size
        self.T = T  # Needed, Maximum Iteration times
        self.w = 1 # Given, Inertia parameter
        self.c1 = 1 # Given
        self.c2 = 1 # Given, Relative importance of the global and local
        self.r1 = random.random() # Needed
        self.r2 = random.random() # Needed, Random float between 0 and 1
        self.xmin = # Not Needed, Lower bound of X
        self.xmax = # Not Needed, Upper bound of X
        self.intX = # Not Needed, Initial position
        self.X = np.zeros((self.N, self.D)) # Needed, Particles' location list
        self.V = np.zeros((self.N, self.D)) # Needed, Particles' velocity list
        self.Pb = np.zeros((self.N, self.D))  # Needed, particle's historical best position
        self.gbest = np.zeros((1, self.D)) # Needed, Global best location of all particles
        self.p_fit = np.zeros(self.N)  # Needed, value of f(global best location)
        self.fit = 1e-10  # Needed, Bacause we want to find maximum value, so assume a samll value first to compare.

    # DEFINE FUNCTIONS
    # Objective function
    def obj_f(self, X):
        ans = # Objective function
        return ans
    # Inertia update function
    def w_update(self, W):
        w = # Inertia update function
        return w

    # INITIALIZATION
    def init_Population(self):
        for i in range(self.N):
            for j in range(self.D):
                # Initial every particles' location 
                # method 1 (given initial location): self.X[i][j] = self.intX[i]
                # method 2 (between lower and upper bound): self.X[i][j] = random.uniform(xmin, xmax)
                # Initial every particles' velocity with 0
                self.V[i][j] = 0
            self.Pb[i] = self.X[i]
            tmp = self.obj_f(self.X[i])
            self.p_fit[i] = tmp
            # If find a value larger than global best found before, update global position
            if (tmp > self.fit):
                self.fit = tmp
                self.gbest = self.X[i]

    # ITERATION AND TRY TO FIND GLOBAL BEST
    def iterator(self):
        fitness = []
        for t in range(self.T):
            for i in range(self.N):  # Update historical best and global best
                temp = self.obj_f(self.X[i])
                if (temp > self.p_fit[i]):  # For any particle, if find a value larger than historical best itself found before, update the particle's historical best
                    self.p_fit[i] = temp
                    self.Pb[i] = self.X[i]
                    if (self.p_fit[i] > self.fit):  # For any particle, if find a value larger than global best found before, update the global best
                        self.gbest = self.X[i]
                        self.fit = self.p_fit[i]
            for i in range(self.N):
                # Update particle's velocity
                self.V[i] = self.w * self.V[i] + self.c1 * self.r1 * (self.Pb[i] - self.X[i]) + self.c2 * self.r2 * (self.gbest - self.X[i]) 
                # Update particle's position
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.fit)
#             print(self.X[0], end=" ")
            print("Iteration times: ", t," | Best of objective function: ", self.fit) #OUTPUT
        return fitness

N = # Swarm size
D = # Dimension size
T = # Maximum Iteration times

my_pso = PSO(N = N, D = D, T = T)
my_pso.init_Population()
fitness = my_pso.iterator()
