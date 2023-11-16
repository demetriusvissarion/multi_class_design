class TodoList:
    def __init__(self):
        self.todos_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if todo:
            self.todos_list.append(todo)
        else:
            raise Exception("No todo set.")
        
    def complete_and_incomplete_helper(self, my_list, boolean):
        # added this method for DRY
        for object in self.todos_list:
            if object.complete == boolean:
                my_list.append(object.task)
        if len(my_list) >= 1:
            return my_list
        else:
            if my_list == self.incomplete_list:
                raise Exception("No incomplete todos.")
            if my_list == self.complete_list:
                raise Exception("No complete todos.")

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        self.incomplete_list = []
        boolean = False
        return self.complete_and_incomplete_helper(self.incomplete_list, boolean)

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        self.complete_list = []
        boolean = True
        return self.complete_and_incomplete_helper(self.complete_list, boolean)

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for object in self.todos_list:
            object.mark_complete()