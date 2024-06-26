from random import randint; 

class ServerAgent: 

    def __init__(self, small_count = 10, medium_count = 10, large_count = 10): 
        self.small_count = small_count
        self.medium_count = medium_count
        self.large_count = large_count

    def select_action(self, percept):
        if(percept >= 100): 
            return None
        if(percept in range(0,34) and self.large_count > 0):
            self.large_count -= 1
            return "large"
        elif(percept in range(34, 67) and self.medium_count > 0):
            self.medium_count -= 1
            return "medium"
        elif(percept in range(67,100) and self.small_count > 0):
            self.small_count -= 1 
            return "small"
        else:
            return None 
    
    def storage_empty(self): 
        return self.small_count == self.medium_count == self.large_count == 0


class ServerEnvironment:

    def __init__(self, server_agent): 
        self.server_agent = server_agent
        self.num_agent_actions = 0


    def tick(self): 
        
        self.server_agent.select_action(randint(a = 0, b = 130))
        self.num_agent_actions += 1
        
    
    def simulate(self):
        while(not self.server_agent.storage_empty()):
            self.tick()
        