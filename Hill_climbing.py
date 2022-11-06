import numpy as np
from heapdict import heapdict
from random import shuffle
import time

def main():
    begin = time.time()            
    start = [1,2,6,4,7,3,5,8,"B"]
    shuffle(start)
    current_node = node(start)
    print("Random start state: ") 
    printstate(current_node)
    solve(current_node)
    end = time.time()
    print("Time required for executuion = ",end-begin," seconds")

#------------------------------------------------------------------------------------------------------
class node:
    def __init__(self,current_state):
        self.state = current_state
        self.h1= tiles(self)
        self.h2= manhattan(self)
        
#------------------------------------------------------------------------------------------------------
def tiles(current_node):
    cost=0
    for i in range(9):
        if current_node.state[i]!= (i+1) and current_node.state[i]!="B":
            cost= cost+1
    return cost

#-----------------------------------------------------------------------------------------------------
def manhattan(current_node):
    cost=0
    current_array = np.array(current_node.state)
    current_array = current_array.reshape(3,3)
    goal_array = np.array([1,2,3,4,5,6,7,8,"B"])
    goal_array = goal_array.reshape(3,3)
    for i in range(3):
        for j in range(3):
            a,b = np.where(goal_array == current_array[i][j])            #returns a & b as a list of single element
            x_index, y_index = int(a),int(b)
            cost+= abs(x_index-i)+abs(y_index-j)
    return cost

#-----------------------------------------------------------------------------------------------------

def blank_pos(current_node):
    for i in range(9):
        if current_node.state[i]=="B":
            return i

#-----------------------------------------------------------------------------------------------------

def child_gen(current_node):

    child_state=[]

    movedict = {0:[1,3],1:[0,2,4],2:[1,5],3:[4,0,6],
    4:[7,5,1,3],5:[2,4,8],6:[3,7],7:[6,4,8],8:[5,7]}

    pos_blank = blank_pos(current_node)

    for _ in movedict[pos_blank]:
        new_child = current_node.state
        new_child[pos_blank], new_child[_]=new_child[_],new_child[pos_blank]
        child_state.append(new_child)
    
    return child_state

#-----------------------------------------------------------------------------------------------------

def printstate(current_node):
    for i in range (9):
        print(current_node.state[i],end = " ")
        if i==2:
            print("")
        if i == 5:
            print("")
    print("")

#-----------------------------------------------------------------------------------------------------

def solve(current_node):
    goal = [1, 2, 6, 4, 7, 'B', 5, 3, 8]                                     # Goal state to be achived
    frontier = heapdict()
    states_explored=[]
    explored_count=0
    plateau=0
    last_heuristic=1000000


    frontier[current_node] =current_node.h1                        #need to change here for different heuristics

    while True:
        current_node = frontier.popitem()[0]
        states_explored.append(current_node.state)
        explored_count += 1

        print("State Explore :",explored_count)
        print("Current State:")
        printstate(current_node)
        print("Current state Heuristic :",current_node.h1)

        if last_heuristic == current_node.h1:
           plateau +=1
           if plateau ==20:
            print("A plateau is forund")
            print(f"Total states Explored: {explored_count}")
            print("Last State")
            print(last_state)
            return
        else:
            plateau=0

        if last_heuristic < current_node.h1 and goal!=current_node.state:
            print("local maxima is found")
            print(f"Total states Explored: {explored_count}")
            print("Last State")
            print(last_state) 
            return

        if goal==current_node.state:
            print("Goal state reached")
            print(f"Total states Explored: {explored_count}")
            frontier.clear()
            return
        
        last_heuristic = current_node.h1                                 #need to change here for differnt heuristics
        last_state = current_node.state

        frontier.clear()

        for child in child_gen(current_node):                                         #to create and put all childs in frontier
            current_child=node(child)
            frontier[current_child] =current_child.h1                           #need to change here for different heuristics   
            

if __name__ == '__main__':
    main()
    