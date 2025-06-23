class Memory: 
    def __init__(self):
        self.history = []

    def add_interaction(self, user_input: str, agent_response: str):
        self.history.append({"user": user_input, "agent": agent_response})

    def get_recent(self, n: int = 5): 
        return self.history[-n:]
    
    def clear(self):
        self.history= []

    def clear(self): 
        self.history = []
    
    def __str__(self):
        return "\n".join([f"User: {entry['user']}\nAgent: {entry['agent']}" for entry in self.history])
