from ast import Continue
from heapdict import heapdict
import numpy as np
from random import shuffle
import time

def main():  
    begin = time.time()            
    s = [1,2,3,4,5,7,"B",8,6]
    shuffle(s)
    start = Node(s)
    print("Random start state: ") 
    printstate(start.state)
    if is_solvable(start.state):
        solve(start)
        print("Monotoe restriction violeted:", check_monotonerest(explored))
        end = time.time()
        print("Time required for executuion = ",end-begin," seconds")
    else:
        print("Puzzle is not solvable")
 
class Node:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.g = gofn(self)
        self.h = h2ofn(self)
        self.f = self.g + self.h
              
def gofn(node):             #Defining cost function
    if node.parent == None:
        node.g =  0
    else:
        node.g = node.parent.g + 1
    return node.g
        
def h1ofn(node):            #Heuristic with uniform zero value
    node.h = 0
    return node.h

def h2ofn(node):            #Heuristic:number of tiles displaced from their destined position
    count = 0
    goal = [1,2,3,4,5,6,7,8,"B"]
    for i in range(9):
        if node.state[i] != goal[i]:
            count+=1
    return count

#Heuristic:sum of Manhattan distance of each tiles from the goal position considering blank
def h3ofn(node):       
    node = np.array(node.state)
    node = node.reshape(3,3)
    manhd = 0
    goal = np.array([1,2,3,4,5,6,7,8,"B"])
    goal = goal.reshape(3,3) 
    for i in range(3):
        for j in range(3):
            a,b = np.where(goal == node[i][j])
            x_goal,y_goal = int(a),int(b)
            manhd += abs(x_goal-i) + abs(y_goal-j)
    return manhd

#Heuristic:sum of Manhattan distance of each tiles from the goal position without blank
def hm3ofn(node):               
    node = np.array(node.state)
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
    return manhd

#Heuristic: unfavourable pairs
def h4ofn(node):
    count = 0
    temp = node.state.copy()
    pos = blank_position(temp)
    temp[pos] = 10
    for i in range(8):
        if temp[i] > temp[i+1]:
            count +=1
    return count
#Function to get blank position for given state
def blank_position(state):
    for i in range(9):
        if state[i] == "B":
            return i
#Function to get optimal path       
def optimal_path(node):
    count = 0
    path = []
    while node.parent:
        count+=1
        path.append(node.state)
        node = node.parent
    return count,path
  
#Function to check monotone restriction       
def check_monotonerest(explored): 
    mcount = 0
    for i in range(len(explored)-1):
        if explored[i+1] < explored[i] :
           mcount+=1    
    return mcount

#Function to get sub-states from the given state
def substates(state):
    substate = []
    pos = blank_position(state)
    #Dictionary to get the possible positions where blank can slide from the given position
    movedict = {0:[1,3],1:[0,2,4],2:[1,5],3:[4,0,6],
    4:[7,5,1,3],5:[2,4,8],6:[3,7],7:[6,4,8],8:[5,7]}
    for _ in movedict[pos]:
        temp = state.copy()
        temp[pos],temp[_] = temp[_],temp[pos]
        substate.append(temp)
    return substate

def printstate(state):
    for i in range (9):
        print(state[i],end = " ")
        if i==2:
            print("")
        if i == 5:
            print("")
    print("")
   
#Function to check wheather puzzle is solvable 
def is_solvable(arr):
    inv_count = 0
    empty_value = "B"
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count %2 == 0
    
#Solving the puzzle
def solve(start):
    global explored
    explored = []
    #start count of state explored
    state_explored = 0
    goal = [1,2,3,4,5,6,7,8,"B"]   # Goal state to be achived
    frontier = heapdict()
    frontier[start] = start.f
    store=set(tuple(start.state))       #set to store visited states to avoid repeatation
    while True:
        node = frontier.popitem()[0]
        explored.append(node.f)
        state_explored += 1
        if (node.state == goal):
            print("End state : ")
            printstate(node.state)
            print("congratulation, you reached to the goal state!")
            a,b = optimal_path(node)
            print("Optimal Path: ")
            while b != []:
                printstate(b.pop())
                print()
            print("Steps for optimal path = ", a)
            print("State Explored = ",state_explored)
            return
        for child in substates(node.state):
            #check wheathwer state is already stored
            if tuple(child) not in store:
                next = Node(child,node)
                frontier[next] = next.f
                store.add(tuple(child))
 

if __name__ == '__main__':
    main()