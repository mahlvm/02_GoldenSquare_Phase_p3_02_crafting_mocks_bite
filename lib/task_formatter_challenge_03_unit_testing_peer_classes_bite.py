class TaskFormatter:
    # task is an instance of Task
    def __init__(self, task): 
        self.task = task

# Returns the task formatted as a string.
# If the task is not complete, the format is:
### - [ ] Task title
# If the task is complete, the format is:
### - [x] Task title
    def format(self): 
        title = self.task.title
        complete = self.task.complete
        
        if complete == True:
            formated = f"-[x] {title}"
			
        else:
            formated = f"-[ ] {title}"
				
        return formated