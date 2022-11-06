import time
from random import shuffle
#start time count
begin = time.time()

#creating stack and queue data structure for DFS and BFS algorithm
class DFS:                       
    def __init__(self):
        self.frontier = []
    def add(self, state):
        self.frontier.append(state)
    def remove(self):
        state = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return state

class BFS(DFS):
    def remove(self):
        state = self.frontier[0]
        self.frontier = self.frontier[1:]
        return state

#Function to get blank position for given state
def blank_position(state):
    for i in range(9):
        if state[i] == "B":
            return i

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

#Solving the puzzle
def solve(start):
    #start count of state explored
    state_explored = 0   
    #Declare algorithm to be used for solving the puzzle
    frontier = BFS()
    frontier.add(start)
    while True:
        state = frontier.remove()
        state_explored += 1
        if (state == goal):
            print("End state : ")
            printstate(state)
            print("congratulation, you reached to the goal state!")
            print("steps count = ",state_explored)
            return
        for child in substates(state):
            #check wheathwer state is already stored
            if tuple(child) not in store:
                frontier.add(child)
                store.add(tuple(child))

start = [3,2,1,4,5,6,8,7,"B"]
shuffle(start)
print("Random start state: " )
printstate(start)
goal = [1,2,3,4,5,6,7,8,"B"]   # Goal state to be achived
store=set(tuple(start))       #set to store visited states to avoid repeatation           
solve(start)
#stop time count
end = time.time()
print("Time required for executuion = ",end-begin," seconds")