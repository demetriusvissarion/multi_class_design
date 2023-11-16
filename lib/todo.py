class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task = ''):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        if task != None:
            if len(task) > 0:
                self.task = task
                self.complete = False
        elif task == None:
            raise Exception("A task cannot be 'None'")
        else:
            raise Exception("A task must have at least one character")


    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True