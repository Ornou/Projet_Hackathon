class Task:
    def __init__(self, task_type, reward, location, deadline):
        self.task_type = task_type
        self.reward = reward
        self.location = location
        self.deadline = deadline
        self.completed = False
        self.failed = False
    
    def complete_task(self):
        self.completed = True
        
    def fail_task(self):
        self.failed = True
        
    def is_completed(self):
        return self.completed
    
    def is_failed(self):
        return self.failed
    
    def time_left(self, current_time):
        return self.deadline - current_time
    
    def get_location(self):
        return self.location
    
    def is_timed_out(self, current_time):
        return current_time > self.deadline
