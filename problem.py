class ConstrainedRouteProblem: 
    def __init__(self, initial_agent_loc, goal_loc, map_edges, map_coords, must_visit):
        self.initial_agent_loc = initial_agent_loc
        self.goal_loc = goal_loc 
        self.map_edges = map_edges
        self.map_coords = map_coords
        self.must_visit = must_visit
        arr = [initial_agent_loc, False, False]
        for i in range(len(must_visit)):
            arr.append(False)
        self.initial_state = tuple(arr)

    
    def actions(self, state):
        actions = [] 
        for loc in self.map_edges.keys():
            if (state[0] == loc[0]):
                actions.append(loc[1])
            elif(state[0] == loc[1]):
                actions.append(loc[0])

        return actions 
    
    def result(self, state, action): 
        mylist = list(state)
        mylist[0] = action
        if(action in self.must_visit): 
            if(self.goal_loc != action):
                mylist[3 + self.must_visit.index(action)] = True
            else: 
                if(mylist[1] == True):
                    mylist[2] = True
                else: 
                    mylist[1] = True
        return tuple(mylist)
    
    def action_cost(self, state1, action, state2): 
        loc1 = state1[0]
        loc2 = action 
        if(self.map_edges.get((loc1, loc2)) == None):
            return self.map_edge.get(loc2, loc1)
        else: 
            return self.map_edges.get(loc1, loc2)
        
    def is_goal(self, state): 
        loc = state[0]
        reach = self.goal_loc == loc 
        goal = state[1]
        goal2 = state[2]
        if reach and goal and not goal2:
            flag = True 
            for i in range(3, len(self.must_visit)):
                flag = state[3] and flag
            return flag
        return False 
    def h(self, node): 
        if (self.is_goal(node.state)):
            return 0 
        else: 
            loc = self.map_coords.get(node.state[0]) 
            goal = self.map_coords.get(self.goal_loc)
            x = abs(loc[0] - goal[0]) ** 2
            y = abs(loc[1] - goal[1]) ** 2
            return ((x + y)) ** 0.5 
        


class GridProblemWithMonsters: 
    def __init__(self, initial_agent_loc, N, monster_coords, food_coords):
        self.initial_agent_loc = initial_agent_loc
        self.N = N 
        self.monster_coords = monster_coords 
        self.food_coords = food_coords 
        t = [0]

        for i in range(0, len(self.food_coords)):
            t.append(False)
        t = tuple(t)
        self.initial_state = initial_agent_loc + t

    def actions(self, state): 
        actions = ["up", "down", "right", "left", "stay"] 
        x = state[0] 
        y = state[1] 
        # 0 = initial, 1 = left, 2 = initial, 3 = right
        MStep = (state[2] + 1) % 4
         
        if(MStep == 0 or MStep == 2):   #Monsters will return to initial spot 
            for loc in self.monster_coords: 
                if not (y + 1 <= self.N and (y + 1) not in loc[1]): 
                    try:
                        actions.remove("up")
                    except ValueError:
                        pass
                if not ((y - 1) > 0 and (y - 1) not in loc[1]):
                    try:
                        actions.remove("down")
                    except ValueError:
                        pass
                if not ((x + 1) <= self.N and (x + 1) not in loc[0]): 
                    try:
                        actions.remove("right")
                    except ValueError:
                        pass
                if not ((x - 1) > 0 and (x - 1) not in loc[0]): 
                    try:
                        actions.remove("left")
                    except ValueError:
                        pass
                if not (x not in loc[0] and y not in loc[1]):
                    try:
                        actions.remove("stay")
                    except ValueError:
                        pass
        elif(MStep == 1): 
            for loc in self.monster_coords: 
                newLoc = list(loc) 
                newLoc[0] = newLoc[0] - 1
                if not (y + 1 <= self.N and (y + 1) not in loc[1]): 
                    try:
                        actions.remove("up")
                    except ValueError:
                        pass
                if not ((y - 1) > 0 and (y - 1) not in loc[1]):
                    try:
                        actions.remove("down")
                    except ValueError:
                        pass
                if not ((x + 1) <= self.N and (x + 1) not in loc[0]): 
                    try:
                        actions.remove("right")
                    except ValueError:
                        pass
                if not ((x - 1) > 0 and (x - 1) not in loc[0]): 
                    try:
                        actions.remove("left")
                    except ValueError:
                        pass
                if not (x not in loc[0] and y not in loc[1]):
                    try:
                        actions.remove("stay")
                    except ValueError:
                        pass
        else: 
            for loc in self.monster_coords: 
                newLoc = list(loc) 
                newLoc[0] = newLoc[0] + 1
                if not (y + 1 <= self.N and (y + 1) not in loc[1]): 
                    try:
                        actions.remove("up")
                    except ValueError:
                        pass
                if not ((y - 1) > 0 and (y - 1) not in loc[1]):
                    try:
                        actions.remove("down")
                    except ValueError:
                        pass
                if not ((x + 1) <= self.N and (x + 1) not in loc[0]): 
                    try:
                        actions.remove("right")
                    except ValueError:
                        pass
                if not ((x - 1) > 0 and (x - 1) not in loc[0]): 
                    try:
                        actions.remove("left")
                    except ValueError:
                        pass
                if not (x not in loc[0] and y not in loc[1]):
                    try:
                        actions.remove("stay")
                    except ValueError:
                        pass
        return actions 
    

    def result(self, state, action): 
        x = state[0]
        y = state[1] 
        mstep = (state[2] + 1) % 4 
        r = list(state) 
        r[2] = mstep
        if(action == "up"):
            r[1] = y + 1
        elif(action == "down"): 
            r[1] = y - 1
        elif (action == "right"): 
            r[0] = x + 1
        elif (action == "left"): 
            r[0] = x - 1
        elif(action == "stay"): 
            return tuple(r)
        count = 3
        for loc in self.food_coords:
            if(r[0] == loc[0] and r[1] == loc[1]): 
                r[count] = True
            count += 1 
        
        return tuple(r)
    
    def actoin_cost(self, state1, action, state2): 
        return 1 if action != [] else 0
    
    def is_goal(self, state): 
        flag = True

        for i in range(3, len(self.food_coords)):
            flag = flag and state[i]
        
        return flag
    

    def h(self, node): 
        if(self.is_goal(node.state)):
            return 0
        x1 = node.state[0]
        y1 = node.state[1]
        min = self.N ** 2 
        for loc in self.food_coords:
            dist = abs(x1-loc[0]) + abs(y1 - loc[1])
            if (min > dist): 
                min = dist 

        return dist 

        
    
                



                
                
        


        





