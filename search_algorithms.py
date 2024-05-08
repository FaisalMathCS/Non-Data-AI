import heapq

class Node: 
    def __init__(self, state, parent_node = None, action_from_parent = None, path_cost = 0): 
        self.state = state
        self.parent_node = parent_node
        self.action_from_parent = action_from_parent
        self.path_cost = path_cost
        self.depth = 0 if self.parent_node == None else (self.parent_node.depth + 1)
    
    def __lt__(self, other):
        return self.state < other.state
    
class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
    # add the items to the PQ
        for item in items:
            self.add(item)
    """
    Add item to PQ with priority-value given by call to priority_function
    """
    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)
    """
    pop and return item from PQ with min priority-value
    """
    def pop(self):
        return heapq.heappop(self.pqueue)[1]
    """
    gets number of items in PQ
    """
    def __len__(self):
        return len(self. pqueue)

#same as the slides 

def expand(problem, node): 
    s = node.state 
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(state = s1, parent_node = node, action_from_parent = action, path_cost = cost)
    

def get_path_actions(node): 
    if (node == None or node.parent_node == None): 
        return [] 
    else: 
        actions = [] 
        actions.append(node.action_from_parent)
        node = node.parent_node
        while node.parent_node != None: 
            actions.append(node.action_from_parent)
            node = node.parent_node
        # return actions.reverse() 
        return actions[::-1]

def get_path_states(node):
    if (node == None): 
        return [] 
    else: 
        states = []
        states.append(node.state)
        node = node.parent_node
        while(node != None): 
            states.append(node.state)
            node = node.parent_node
        return states[::-1] 
        # return states.reverse() 

def best_first_search(problem, f):
    node = Node(state = problem.initial_state)
    frontier = PriorityQueue((node, ), f)
    reached = {node.state : node} 

    while len(frontier) > 0: 
        curr = frontier.pop()

        if problem.is_goal(curr.state):
            return curr

        for child in expand(problem, curr):
            child_state = child.state
            if child_state not in reached or child.path_cost < reached[child_state].path_cost:
                frontier.add(child)
                reached[child_state] = child 
    return None



def best_first_search_treelike(problem, f): 
    node = Node(state = problem.initial_state)
    frontier = PriorityQueue((node, ), f)

    while len(frontier) > 0: 
        curr = frontier.pop()

        if problem.is_goal(curr.state):
            return curr

        for child in expand(problem, curr):
            child_state = child.state
            frontier.add(child)

    return None

def breadth_first_search(problem, treelike = False): 
    f = (lambda n: n.depth)
    if(not treelike):
        return best_first_search(problem, f)
    else:
        return best_first_search_treelike(problem, f)
    

def depth_first_search(problem, treelike= False):
    f = (lambda n: - n.depth)
    if (treelike):
        return best_first_search_treelike(problem, f)
    else: 
        return best_first_search(problem, f)

def uniform_cost_search(problem, treelike = False): 
    f = (lambda n: n.path_cost)
    if(not treelike): 
        best_first_search(problem, f)
    else: 
        best_first_search_treelike(problem, f)

def greedy_search(problem, h, treelike = False):
    f = (lambda n: h(n))
    if (treelike): 
        best_first_search_treelike(problem, f)
    else:
       return best_first_search(problem, f)
    

def astar_search(problem, h, treelike = False):
    f = (lambda n: n.path_cost + h(n))
    if (treelike): 
        return best_first_search_treelike(problem, f)
    else: 
        return best_first_search(problem, f)
    return None
