import pytest
from lib.todo import *
from lib.todo_list import *

"""
Given an instance of the class Todo and a todo
#add Adds the todo to the list of todos (no return)
"""
def test_if_adds_todo():
    todo_object = Todo('Complete upper body day 1 weightlifting program today')
    todo_list_object = TodoList()
    todo_list_object.add(todo_object)
    result = todo_list_object.todos_list[0].task
    assert result == 'Complete upper body day 1 weightlifting program today'


"""
Given an instance of the class Todo and some todos
#incomplete retruns a list of Todo instances representing the todos that are not complete
"""
def test_if_returns_all_incomplete_todos():
    todo1 = Todo('Complete upper body day 1 weightlifting program today')
    todo2 = Todo('Complete upper body day 2 weightlifting program tomorrow')
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    result = todo_list.incomplete()
    assert result == ['Complete upper body day 1 weightlifting program today', 'Complete upper body day 2 weightlifting program tomorrow']


"""
Given an instance of the class Todo and some todos
#complete retruns a list of Todo instances representing the todos that are complete
"""
def test_if_returns_all_complete_todos():
    todo1 = Todo('Complete upper body day 1 weightlifting program today')
    todo2 = Todo('Complete upper body day 2 weightlifting program tomorrow')
    todo3 = Todo('Complete upper body day 3 weightlifting program the day after tomorrow')
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo1.mark_complete()
    result = todo_list.complete()
    assert result == ['Complete upper body day 1 weightlifting program today']


"""
Given an instance of the class Todo and some todos
#give_up Marks all todos as complete (no return)
"""
def test_if_give_up():
    todo1 = Todo('Complete upper body day 1 weightlifting program today')
    todo2 = Todo('Complete upper body day 2 weightlifting program tomorrow')
    todo3 = Todo('Complete upper body day 3 weightlifting program the day after tomorrow')
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.give_up()
    with pytest.raises(Exception) as e: 
        todo_list.incomplete()
    error_message = str(e.value)
    assert error_message == "No incomplete todos."