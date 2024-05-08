import copy 
def ac3(csp, arcs_queue = None, current_domains = None, assignment = None):
    if(arcs_queue != None): 
        arcs = set(arcs_queue)
    elif(arcs_queue == None): 
        arcs = set()
        for key in csp.adjacency:
            for nei in csp.adjacency[key]: 
                arcs.add((key, nei))
    if(current_domains == None): 
        current_domains = copy.deepcopy(csp.domains)

    if(assignment == None): 
        assignment = {} 
    
    updated_domains = copy.deepcopy(current_domains)

    while(arcs): 
        xi, xj = arcs.pop()
        if(revise(csp, current_domains, xi, xj)):
            updated_domains = copy.deepcopy(current_domains) 
            if(len(current_domains[xi]) == 0): 
                return False, updated_domains
            for var in csp.adjacency[xi]:
                if (var != xj and (var, xi) not in assignment):
                    arcs.add((var, xi))
    return True, updated_domains

def revise(csp, domains, x, y):
    revised = False
    xDomain = domains[x].copy()
    yDomain = domains[y].copy()

    for i in xDomain: 
        count = 0
        for j in yDomain: 
            if(not csp.constraint_consistent(x, i, y, j)):
                count += 1
                if(count >= len(yDomain)):
                    domains[x].remove(i)
                    revised = True

    return revised 


#https://nextjournal.com/lomin/constraint-satisfaction-problems-and-functional-backtracking-search I used this website heavily specially for backtracking.
#this as well https://github.com/aimacode/aima-python/blob/master/csp.ipynb
# lastly this http://aima.cs.berkeley.edu/python/csp.py
# it doesn't work anyway :(
def backtracking(csp): 
    return backtracking_helper(csp)

def backtracking_helper(csp, assignment = {}, current_domains = None):
    if csp.is_goal(assignment):
        return assignment
    if(current_domains == None): 
        current_domains = copy.deepcopy(csp.domains); 
    var = mrv(assignment, csp)
    domain = list(csp.domains[var])

    for value in domain: 
        assign = {}
        assign[var] = value 
        if(csp.check_partial_assignment(assign)): 
            arcs = set()
            assignment[var] = value 
            current_domains[var] = [value]
            for variable in csp.adjacency[var]:
                arcs.add((variable, var))
            check , updated = ac3(csp, arcs, copy.deepcopy(current_domains), assignment)
            if (check): 
                # print(updated)
                result = backtracking_helper(csp, assignment, copy.deepcopy(updated))
                if result !=None: 
                    return result 
                assignment[var] = None
    return None 

 

def mrv(assignment, csp):
    mrv = csp.domains.keys()[0]
    # print(mrv)
    lowest = len(csp.domains[mrv])

    for key in csp.domains.keys():
        l = len(csp.domains[key])

        if(l < lowest and key not in assignment):
            min = l 
            mrv = key
        elif(l == lowest and mrv not in assignment):
            if ((len(csp.adjacency[key]) > len(csp.adjacency[mrv]))):
                lowest = l 
                mrv = key 

    return mrv 



class SudokuCSP: 

    def __init__(self, partial_assignment = {}): 
        vars = []
        for i in range(1, 10): 
            for j in range(1, 10): 
                vars.append((i, j))
        self.variables = vars 
        self.domains = {}
        nums = [num for num in range(1,10)]
        for tup in vars: 
            self.domains[tup] = nums 
        if (partial_assignment): 
            for key in partial_assignment: 
                self.domains[key] = [partial_assignment[key]]
        self.adjacency = {} 



        

