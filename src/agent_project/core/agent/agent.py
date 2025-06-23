class Agent: 
    def __init__(self, memory, tool_selector, executor):
        self.memory = memory
        self.tool_selector = tool_selector
        self.executor = executor
    
    def handle_query(self, user_input):
        memory_reponse = self.memory.search(user_input)
        
        if memory_reponse:
            return memory_reponse   
        
        selected_tool = self.tool_selector.select(user_input)
        result = self.executor.run(selected_tool, user_input)
        self.memory.store(user_input, result)
        
        return result 