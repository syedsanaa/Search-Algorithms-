import heapq
import math

class State:
    """
    Class to represent a state on grid-based pathfinding problems. The class contains two static variables:
    map_width and map_height containing the width and height of the map. Although these variables are properties
    of the map and not of the state, they are used to compute the hash value of the state, which is used
    in the CLOSED list. 

    Each state has the values of x, y, g, h, and cost. The cost is used as the criterion for sorting the nodes
    in the OPEN list for both Dijkstra's algorithm and A*. For Dijkstra the cost should be the g-value, while
    for A* the cost should be the f-value of the node. 
    """
    map_width = 0
    map_height = 0
    
    def __init__(self, x, y):
        """
        Constructor - requires the values of x and y of the state. All the other variables are
        initialized with the value of 0.
        """
        self._x = x
        self._y = y
        self._g = 0
        self._cost = 0
        self._parent = None
        
    def __repr__(self):
        """
        This method is invoked when we call a print instruction with a state. It will print [x, y],
        where x and y are the coordinates of the state on the map. 
        """
        state_str = "[" + str(self._x) + ", " + str(self._y) + "]"
        return state_str
    
    def __lt__(self, other):
        """
        Less-than operator; used to sort the nodes in the OPEN list
        """
        return self._cost < other._cost
    
    def state_hash(self):
        """
        Given a state (x, y), this method returns the value of x * map_width + y. This is a perfect 
        hash function for the problem (i.e., no two states will have the same hash value). This function
        is used to implement the CLOSED list of the algorithms. 
        """
        return self._y * State.map_width + self._x
    
    def __eq__(self, other):
        """
        Method that is invoked if we use the operator == for states. It returns True if self and other
        represent the same state; it returns False otherwise. 
        """
        return self._x == other._x and self._y == other._y

    def get_x(self):
        """
        Returns the x coordinate of the state
        """
        return self._x
    
    def set_parent(self, parent):
        """
        Sets the parent of a node in the search tree
        """
        self._parent = parent

    def get_parent(self):
        """
        Returns the parent of a node in the search tree
        """
        return self._parent
    
    def get_y(self):
        """
        Returns the y coordinate of the state
        """
        return self._y
    
    def get_g(self):
        """
        Returns the g-value of the state
        """
        return self._g
        
    def set_g(self, g):
        """
        Sets the g-value of the state
        """
        self._g = g

    def get_cost(self):
        """
        Returns the cost of a state; the cost is determined by the search algorithm
        """
        return self._cost
    
    def set_cost(self, cost):
        """
        Sets the cost of the state; the cost is determined by the search algorithm 
        """
        self._cost = cost
class Dijkstra:
    def __init__(self,map):
        self.map= map
    def reconstruct_path(self, goal):
        PathList=[]
        while goal.get_parent()!=State(None,None) :
            PathList.append(goal)
            goal=goal.get_parent()
        PathList.append(goal)
        PathList.reverse()
        return PathList
    def Algorithm(self, InitialS, GoalS):
        nodes = 0
        OpenList = []
        ClosedList = {}
        heapq.heappush(OpenList,(0,InitialS))  #(state,cost)
        ClosedList[InitialS.state_hash()]=InitialS
        InitialS.set_parent(State(None,None))   #ADDED FOR RECONSTRUCTION PATH 
        InitialS.set_g(0) #ADDED FOR COST
        while OpenList:
            nodes+=1
            g_n,n=heapq.heappop(OpenList)
            if  n==GoalS: 
                return self.reconstruct_path(n),n.get_g(),nodes,ClosedList
            for child in self.map.successors(n):
                if nodes>1:
                    if n.get_parent()==child:   # CHECKK
                        continue 
                if child.state_hash() not in ClosedList:
                    child.set_parent(n)  #ADDED FOR RECONSTRUCTION PATH 
                    #child.set_cost=n.get_g+cost(Xdifference, Ydifference)
                    heapq.heappush(OpenList,(child.get_g(),child))   # THINGS TO ADD 
                    ClosedList[child.state_hash()]= child   # THINGS TO ADD 
                if child.state_hash() in ClosedList and child.get_g()<ClosedList[child.state_hash()].get_g(): 
                   ClosedList[child.state_hash()].set_g(child.get_g()) # UPDATING G VALUE IN CLOSED 
                   child.set_parent(n)
                   heapq.heappush(OpenList,(child.get_g(),child))
        return None,-1,nodes,ClosedList
class AStar:
    def __init__(self,map):
        self.map= map
    def reconstruct_path(self, goal):
        PathList=[]
        while goal.get_parent()!=State(None,None) :
            PathList.append(goal)
            goal=goal.get_parent()
        PathList.append(goal)
        PathList.reverse()
        return PathList
    def MD(self,GOAL,child):
        DeltaY=abs((GOAL.get_y()-child.get_y()))
        DeltaX=abs((GOAL.get_x()-child.get_x()))
        return 1.5*min(DeltaY,DeltaX)+abs(DeltaX-DeltaY)
    def Algorithm(self,InitialS,GoalS):
        nodes=0
        OpenList=[]
        ClosedList={}
        InitialS.set_g(0)
        InitialS.set_cost(0+self.MD(GoalS,InitialS))
        heapq.heappush(OpenList,(InitialS.get_cost(),InitialS))  #(state,cost)
        ClosedList[InitialS.state_hash()]=InitialS
        InitialS.set_parent(State(None,None))    #ADDED FOR RECONSTRUCTION PATH 
        while OpenList:
            nodes+=1
            cost,n=heapq.heappop(OpenList)
            if  n==GoalS: 
                return self.reconstruct_path(n),n.get_g(),nodes,ClosedList    
            for child in self.map.successors(n):
                child.set_cost(child.get_g()+self.MD(GoalS,child))
                if nodes>1:
                    if n.get_parent()==child:   # CHECKK
                      continue 
                if child.state_hash() not in ClosedList:
                   child.set_parent(n)  #ADDED FOR RECONSTRUCTION PATH 
                   heapq.heappush(OpenList,(child.get_cost(),child))   
                   ClosedList[child.state_hash()]= child   
                if child.state_hash() in ClosedList and child.get_cost()<ClosedList[child.state_hash()].get_cost(): 
                   ClosedList[child.state_hash()]=child   # UPDATING G VALUE IN CLOSED 
                   child.set_parent(n)
                   heapq.heappush(OpenList,(child.get_cost(),child))
        return None,-1,nodes,ClosedList
    def AlgorithmModify(self,InitialS,GoalS):
        nodes=0
        OpenList=[]
        ClosedList={}
        InitialS.set_g(0)
        InitialS.set_cost(0+2*self.MD(GoalS,InitialS))
        heapq.heappush(OpenList,(InitialS.get_cost(),InitialS))  #(state,cost)
        ClosedList[InitialS.state_hash()]=InitialS
        InitialS.set_parent(State(None,None))    #ADDED FOR RECONSTRUCTION PATH 
        while OpenList:
            nodes+=1
            cost,n=heapq.heappop(OpenList)
            if  n==GoalS: 
                return self.reconstruct_path(n),n.get_g(),nodes,ClosedList    
            for child in self.map.successors(n):
                child.set_cost(child.get_g()+2*self.MD(GoalS,child))
                if nodes>1:
                    if n.get_parent()==child:   # CHECKK
                      continue 
                if child.state_hash() not in ClosedList:
                   child.set_parent(n)  #ADDED FOR RECONSTRUCTION PATH 
                   heapq.heappush(OpenList,(child.get_cost(),child))   
                   ClosedList[child.state_hash()]= child   
                if child.state_hash() in ClosedList and child.get_cost()<ClosedList[child.state_hash()].get_cost():
                   ClosedList[child.state_hash()]=child   # UPDATING G VALUE IN CLOSED 
                   child.set_parent(n)
                   heapq.heappush(OpenList,(child.get_cost(),child))
        return None,-1,nodes,ClosedList
    
        
    
    
    


