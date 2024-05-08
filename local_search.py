#Local Search using Simulated Annleaing to solve the traveling Salesman problem, Generalization is simple once the problem formulation is done.

import numpy as np 

def tour_cost(state, adj_matrix): 
    cost = 0
    i = 0; 
    while(True): 
        if(adj_matrix[state[i]][state[i+1]] == np.nan):
            return np.nan
        cost += adj_matrix[state[i]][state[i+1]]
        i += 1 
        if(i >= len(state) - 1): 
            break
    return cost

def random_swap(state): 
    idx1, idx2 = np.random.choice(len(state), size = 2, replace = False) 
    NewState = state.copy()
    temp = NewState[idx1]
    NewState[idx1] = NewState[idx2]
    NewState[idx2] = temp
    return NewState

def simulated_annealing(initial_state, adj_matrix, initial_T = 1000): 
    T = initial_T
    curr = initial_state
    iters = 0 

    while(True): 
        T = T * 0.99 
        if(T < 10 ** -14):
            return curr, iters 
        next = random_swap(curr)
        deltaE = tour_cost(curr, adj_matrix) - tour_cost(next, adj_matrix)
        if (deltaE > 0): curr = next
        elif deltaE <= 0: 
            u = np.random.uniform() 
            e = np.exp(deltaE/T)
            if u <= e: 
                curr = next 

        iters += 1 






