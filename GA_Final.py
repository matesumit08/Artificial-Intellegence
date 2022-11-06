from random import shuffle,randint
import numpy as np

def main():
    goal =  [1,2,3,4,5,6,7,8,"B"]  
    population = generate_population()
    print('Initial Population: ') 
    pupulationstates(population)
    state_explored =0 
    while True:
        parent1 = roulletewheel(population)
        parent2 = roulletewheel(population)
        child1,child2 = crossover(parent1,parent2)
        state_explored +=1       
        if child1 == goal or child2 == goal:
            print("Goal state is successfully reached")
            print('state explored = ', state_explored)
            printstate(goal)
            return    
        population = update_population(population,child1)
        population = update_population(population,child2)
        
class Node:
    def __init__(self,state):
        self.state = state
        self.fitness = hofn(state)
        
def generate_population():
    population = []
    for i in range(9):
        s = [3,2,1,4,5,6,8,7,'B']
        shuffle(s)
        population.append(Node(s))
    population  = sorted(population,key= lambda x:x.fitness)
    return population

def h1ofn(state):            #Heuristic:number of tiles displaced from their destined position
    count = 0
    goal = [1,2,3,4,5,6,7,8,'B']
    for i in range(9):
        if state[i] != goal[i]:
            count+=1
    return 9-count

def hofn(state):               
    node = np.array(state)
    node = node.reshape(3,3)
    manhd = 0
    goal = np.array([1,2,3,4,5,6,7,8,"B"])
    goal = goal.reshape(3,3) 
    for i in range(3):
        for j in range(3):
            if node[i][j] == 'B':
                continue
            else:
                a,b = np.where(goal == node[i][j])
                x_goal,y_goal = int(a),int(b)
                manhd += abs(x_goal-i) + abs(y_goal-j)
    return 30-manhd

def roulletewheel(population):
    f =  list(map(lambda x:x.fitness, population))
    total_fitness = sum(f)
    n = randint(0,total_fitness)
    c_sum = 0
    for i in range(9):
        c_sum = c_sum + population[i].fitness
        if c_sum >= n:
            return population[i].state
        
def crossover(parent1, parent2):
    child1 = []
    child2 = []
    n = randint(2,8)
    for i in range(n):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(9):
        if(parent2[i] not in child1):
            child1.append(parent2[i])
        if(parent1[i] not in child2):
            child2.append(parent1[i])
    mutation(child1)
    mutation(child2)
    return child1,child2

def update_population(population,child1):
    population.append(Node(child1))
    population  = sorted(population,key= lambda x:x.fitness)
    population.remove(population[0])
    return population
    
def pupulationstates(population):
    for i in range(9):
        print(population[i].state,end='  ')
        if i == 2 or i ==5:
            print()
    print()

def mutation(state):
    for i in range(9):
        if state[i] == 'B' :
            state[i] = state[8]
            state[8] = 'B'
            break
    for i in range(7):
        if state[i] > state[i+1]:
            state[i],state[i+1] = state[i+1],state[i] 
            break


def printstate(state):
    for i in range (9):
        print(state[i],end = " ")
        if i==2:
            print("")
        if i == 5:
            print("")
    print("")
    
if __name__ == '__main__':
    main()