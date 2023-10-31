# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
 
 
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
 
import util
 
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
 
    You do not need to change anything in this class, ever.
    """
 
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()
 
    def isGoalState(self, state):
        """
          state: Search state
 
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()
 
    def expand(self, state):
        """
          state: Search state
 
        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()
 
    def getActions(self, state):
        """
          state: Search state
 
        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()
 
    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.
 
        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()
 
    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state
 
        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()
 
    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take
 
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()
 
 
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
 
 
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
 
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
 
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
 
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
 
    from util import Stack
    stacc = Stack()                # stiva de la dfs
    stacc.push(problem.getStartState()) # pun poz de start pe stiva
    visited = []                    # lista cu ce am vizitat
    tempPath=[]                     # cale temporara
    path=[]                         # calea catre final
    pathToCurrent=Stack()           # stiva care tine pathurile facute pe parcurs
    currState = stacc.pop()        # scot ultima poz din stiva ca ma pun sa o prelucrez
    while not problem.isGoalState(currState): #cat timp nu am ajuns la final
        if currState not in visited:
            visited.append(currState) # daca nu e vizitata pozitia o pun in visited
            successors = problem.expand(currState) # vecinii pozitiei curente
            for child,direction,cost in successors:
                stacc.push(child) # pun vecinul in stiva 
                tempPath = path + [direction] # path temporar ce contine directiile pe care le-am luat pana acum + directia in care se afla vecinul curnet
                pathToCurrent.push(tempPath) # pun pathul facut pana aici in stiva de pathuri
        currState = stacc.pop() # trec la pozitia urmatoare (unul dintre vecinii pusi anterior pe stiva)
        path = pathToCurrent.pop() # schimb pozitia pathului cu ultima pe care am pus-o
    return path
 
 
    #util.raiseNotDefined()
 
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
 
    from util import Queue
    coada = Queue()                        # Literalmente la fel ca la dfs dar cu coada nu stiva
    coada.push(problem.getStartState())
    visited = []                            
    tempPath=[]                             
    path=[]                                  
    pathToCurrent=Queue()                   
    currState = coada.pop()
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)    
            successors = problem.expand(currState)
            for child,direction,cost in successors:
                coada.push(child)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)
        currState = coada.pop()
        path = pathToCurrent.pop()
    return path
 
 
    util.raiseNotDefined()
 
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
 
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
 
    from util import Queue,PriorityQueue #la fel ca si celelalte dar cu priority queue (cu cat valoare de prioritate e mai mica cu atat e mai prioritar)
    fringe = PriorityQueue()                    
    fringe.push(problem.getStartState(),0)
    currState = fringe.pop()
    visited = []                                
    tempPath=[]                                 
    path=[]                                      
    pathToCurrent=PriorityQueue()               
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)
            successors = problem.expand(currState)
            for child,direction,cost in successors:
                tempPath = path + [direction]
                costToGo = problem.getCostOfActionSequence(tempPath) + heuristic(child,problem)
                if child not in visited: # la asta mai trb sa verific si copilul sa nu fie vizitat
                    fringe.push(child,costToGo)
                    pathToCurrent.push(tempPath,costToGo)
        currState = fringe.pop()
        path = pathToCurrent.pop()    
    return path
 
    util.raiseNotDefined()
 
 
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
