class SimpleACReflexAgent: 
    def __init__(self, min_threshold, max_threshold):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold


    def select_action(self, percept):
        curr_temp, state = percept
        # print(curr_temp)
        if (state):
            if (curr_temp <= self.min_threshold):
                return "TurnOff"
            else:
                return None
        else:
            if(curr_temp >= self.max_threshold):
                return "TurnOn"
            else:
                return None

class SimpleACEnvironment: 

    def __init__(self, ac_agent, starting_temp = 28):
        self.ac_agent = ac_agent
        self.temperature = starting_temp
        self.num_agent_actions = 0
        self.is_ac_on = False

    def tick(self):
        percept = [self.temperature, self.is_ac_on]
        # print(self.temperature)
        next_state = self.ac_agent.select_action(percept)
        # print(next_state)
        if(next_state != None):
            self.num_agent_actions += 1
            if(next_state == "TurnOff"):
                self.is_ac_on = False
            else:
                self.is_ac_on = True
        if(self.is_ac_on):
            self.temperature -= 1
        else: 
            self.temperature += 1 

        

    def simulate(self, num_timesteps):
        for i in range(num_timesteps):
            self.tick()